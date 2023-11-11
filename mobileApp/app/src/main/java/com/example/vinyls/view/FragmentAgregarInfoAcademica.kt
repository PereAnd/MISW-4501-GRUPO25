package com.example.vinyls.view

import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ArrayAdapter
import androidx.fragment.app.Fragment
import androidx.fragment.app.viewModels
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.lifecycleScope
import androidx.navigation.fragment.findNavController
import com.example.vinyls.R
import com.example.vinyls.databinding.FragmentAgregarInfoAcademicaBinding
import com.example.vinyls.viewmodels.AgregarInfoAcademicaViewModel
import com.google.android.material.snackbar.Snackbar
import kotlinx.coroutines.async
import kotlinx.coroutines.launch
import org.json.JSONObject
import java.util.*
import android.widget.TextView


class FragmentAgregarInfoAcademica : Fragment(R.layout.fragment_agregar_info_academica) {

    private var _binding: FragmentAgregarInfoAcademicaBinding? = null
    private val binding get() = _binding!!
    private lateinit var viewModel: AgregarInfoAcademicaViewModel

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?
    ): View? {
        _binding = FragmentAgregarInfoAcademicaBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)

        val activity = requireNotNull(this.activity) {
            "You can only access the viewModel after onActivityCreated()"
        }
        viewModel = ViewModelProvider(this, AgregarInfoAcademicaViewModel.Factory(activity.application)).get(
            AgregarInfoAcademicaViewModel::class.java
        )

        createButton()
        setupSpinner()
    }

    private var currentState: Boolean = false

    private fun createButton() {
        binding.btnNextTecnic.setOnClickListener {
            sendDataToServer()

            if (currentState) {
                findNavController().navigate(R.id.action_fragment_infoAcademica_fragment_infoTecnica)
            } else {
                // Handle the case when currentState is false
            }
        }
    }

    private fun setupSpinner() {
        val spinner = binding.spinnerStudyType
        val adapter = ArrayAdapter.createFromResource(
            requireContext(),
            R.array.study_types,
            android.R.layout.simple_spinner_item
        )
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        spinner.adapter = adapter
    }

    private fun sendDataToServer() {
        if (validateForm()) {
            val selectedStudyType = binding.spinnerStudyType.selectedItem.toString()
            val strInfoAcademica = """
                {
                    "title": "${binding.etTitle.text}",
                    "institution": "${binding.etInstitution.text}",
                    "beginDate": "${binding.etBeginDate.text}",
                    "endDate": "${binding.etEndDate.text}",
                    "studyType": "$selectedStudyType"
                }
            """.trimIndent()

            Log.i("data Captured", strInfoAcademica)

            lifecycleScope.launch {
                val idAgregarInfoAcademica = async {
                    viewModel.agregarInfoAcademicaFromNetwork(JSONObject(strInfoAcademica))
                }
                val i = idAgregarInfoAcademica.await()
                // Use the value of i as needed
            }
        }
    }

    private fun validateForm(): Boolean {
        var isValid = true

        with(binding) {
            if (etTitle.text.toString().isEmpty()) {
                isValid = false
                tiTitle.error = "Campo requerido"
            } else {
                tiTitle.error = null
            }

            if (etInstitution.text.toString().isEmpty()) {
                isValid = false
                tiInstitution.error = "Campo requerido"
            } else {
                tiInstitution.error = null
            }

            if (etBeginDate.text.toString().isEmpty()) {
                isValid = false
                tiBeginDate.error = "Campo requerido"
            } else {
                tiBeginDate.error = null
            }

            if (etEndDate.text.toString().isEmpty()) {
                isValid = false
                tiEndDate.error = "Campo requerido"
            } else {
                tiEndDate.error = null
            }



            val selectedStudyType = spinnerStudyType.selectedItem.toString()
            if (selectedStudyType == resources.getString(R.string.choose_study_type)) {
                    isValid = false

                llStudyType.findViewById<TextView>(R.id.tvStudyTypeError).apply {
                  visibility = View.VISIBLE
                  text = "Selecciona un Tipo de Estudio!"
                      }
                 } else {
                  llStudyType.findViewById<TextView>(R.id.tvStudyTypeError).visibility = View.GONE
            }

         //       Snackbar.make(root, "Seleccione un tipo de estudio", Snackbar.LENGTH_SHORT).show()



        }
        currentState = isValid
        return currentState
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}
