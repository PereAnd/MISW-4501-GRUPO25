package com.example.vinyls.view

import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import androidx.fragment.app.Fragment
import androidx.fragment.app.viewModels
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.lifecycleScope
import androidx.navigation.fragment.findNavController
import com.example.vinyls.R
import com.example.vinyls.databinding.FragmentAgregarInfoTecnicaBinding
import com.example.vinyls.viewmodels.AgregarInfoTecnicaViewModel
import com.google.android.material.snackbar.Snackbar
import kotlinx.android.synthetic.main.fragment_agregar_info_tecnica.*
import kotlinx.coroutines.async
import kotlinx.coroutines.launch
import org.json.JSONObject
import java.util.*
import android.widget.TextView
import android.widget.ArrayAdapter

class FragmentAgregarInfoTecnica : Fragment(R.layout.fragment_agregar_info_tecnica) {
    private var _binding: FragmentAgregarInfoTecnicaBinding? = null
    private val binding get() = _binding!!  // get
    private lateinit var viewModel: AgregarInfoTecnicaViewModel
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?):
            View? {
        _binding = FragmentAgregarInfoTecnicaBinding.inflate(inflater, container, false)
        val view = binding.root
        return view
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        var i:Int=0
        val activity = requireNotNull(this.activity) {
            "You can only access the viewModel after onActivityCreated()"
        }
        viewModel = ViewModelProvider(this, AgregarInfoTecnicaViewModel.Factory(activity.application)).get(
            AgregarInfoTecnicaViewModel::class.java)

        createButton()
        setupSkillSpinner()
    }

    private var currentState: Boolean = false
    private fun createButton() {
        binding.btnNextLabor.setOnClickListener {
            sendDataToServer()

            if (currentState) {
                findNavController().navigate(R.id.action_fragment_infoTecnica_fragment_infoLaboral)
            }
            else {
                //
            }
        }
    }


    private fun setupSkillSpinner() {
        val spinner = binding.spinnerSkillType
        val adapter = ArrayAdapter.createFromResource(
            requireContext(),
            R.array.skill_types,
            android.R.layout.simple_spinner_item
        )
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        spinner.adapter = adapter
    }

    private fun sendDataToServer() {
        var i:Int=0
        if(validateForm()){
            val selectedSkill= binding.spinnerSkillType.selectedItem.toString()

            var strInfoTecnica = "{\n \"description\": \"" +
                    binding.etDescriptionType.text.toString() +
                    "\",\n  \"type\": \"" +
                    selectedSkill +
                    "\"\n}"
            Log.i("data Captured",strInfoTecnica)

            lifecycleScope.launch{
                val idAgregarInfoTecnica = async { viewModel.agregarInfoTecnicaFromNetwork(JSONObject(strInfoTecnica)) }
                i = idAgregarInfoTecnica.await()
            }
            
        }
    }

    private fun validateForm(): Boolean {
        var isValid = true

        with(binding){

            if (etDescriptionType.text.toString().isEmpty()) {
                isValid = false
                tiDescriptionType.error = "Campo requerido"
            } else {
                tiDescriptionType.error = null
            }

            val selectedSkill= spinnerSkillType.selectedItem.toString()
            if (selectedSkill == resources.getString(R.string.choose_skill)) {
                isValid = false

                llSkillType.findViewById<TextView>(R.id.tvSkillError).apply {
                    visibility = View.VISIBLE
                    text = "Selecciona una habilidad!"
                }
            } else {
                llSkillType.findViewById<TextView>(R.id.tvSkillError).visibility = View.GONE
            }

        }
        currentState = isValid
        return currentState
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }


}