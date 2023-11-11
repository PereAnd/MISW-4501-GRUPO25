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
import com.example.vinyls.databinding.FragmentAgregarInfoPersonalBinding
import com.example.vinyls.viewmodels.AgregarInfoPersonalViewModel
import com.google.android.material.snackbar.Snackbar
import kotlinx.android.synthetic.main.fragment_agregar_info_personal.*
import kotlinx.coroutines.async
import kotlinx.coroutines.launch
import org.json.JSONObject
import java.util.*
import android.widget.TextView
import android.widget.ArrayAdapter

class FragmentAgregarInfoPersonal : Fragment(R.layout.fragment_agregar_info_personal) {

    private var _binding: FragmentAgregarInfoPersonalBinding? = null
    private val binding get() = _binding!!  // get
    private lateinit var viewModel: AgregarInfoPersonalViewModel
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?):
            View? {
        _binding = FragmentAgregarInfoPersonalBinding.inflate(inflater, container, false)
        val view = binding.root
        return view
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        var i:Int=0
        val activity = requireNotNull(this.activity) {
            "You can only access the viewModel after onActivityCreated()"
        }
        viewModel = ViewModelProvider(this, AgregarInfoPersonalViewModel.Factory(activity.application)).get(
            AgregarInfoPersonalViewModel::class.java)

        createButton()
        setupSpinner()
        setupCountrySpinner()
    }

    private var currentState: Boolean = false
    private fun createButton() {
        binding.btnNextAcademic.setOnClickListener {
            sendDataToServer()

            if (currentState) {
                findNavController().navigate(R.id.action_fragment_infoPersonal_to_fragment_infoAcademica)
            }
            else {
                //
            }

        }
    }


    private fun setupSpinner() {
        val spinner = binding.spinnerDocType
        val adapter = ArrayAdapter.createFromResource(
            requireContext(),
            R.array.doc_types,
            android.R.layout.simple_spinner_item
        )
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        spinner.adapter = adapter
    }

    private fun setupCountrySpinner() {
        val spinner = binding.spinnerCountry
        val adapter = ArrayAdapter.createFromResource(
            requireContext(),
            R.array.country_list,  // Ajusta con el nombre correcto de tu array de países
            android.R.layout.simple_spinner_item
        )
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item)
        spinner.adapter = adapter
    }


    private fun sendDataToServer() {
        if (validateForm()) {
            val selectedDocType = binding.spinnerDocType.selectedItem.toString()
            val selectedCountry = binding.spinnerCountry.selectedItem.toString()

            var strInfoPersonal = "{\n \"names\": \"" +
                    binding.etNamesInfoPersonal.text.toString() +
                    "\",\n  \"lastNames\":\"" +
                    binding.etLastNamesInfoPersonal.text.toString() +
                    "\",\n  \"mail\": \"" +
                    binding.etMailInfoPersonal.text.toString() +
                    "\",\n  \"docType\": \"" +
                    binding.etDocNumber.text.toString() +
                    "\",\n  \"docNumber\": \"" +
                    selectedDocType +
                    "\",\n  \"phone\": \"" +
                    binding.etPhone.text.toString() +
                    "\",\n  \"address\": \"" +
                    binding.etAddress.text.toString() +
                    "\",\n  \"birthDate\": \"" +
                    binding.etBirthDate.text.toString() +
                    "\",\n  \"country\": \"" +
                    selectedCountry +
                    "\",\n  \"city\": \"" +
                    binding.etCity.text.toString() +
                    "\",\n  \"language\": \"" +
                    binding.etLanguage.text.toString() +
                    "\"\n}"

            Log.i("data Captured", strInfoPersonal)

            lifecycleScope.launch {
                val idAgregarInfoPersonal = async {
                    viewModel.agregarInfoPersonalFromNetwork(JSONObject(strInfoPersonal))
                }
                val result = idAgregarInfoPersonal.await()
                // Aquí puedes hacer algo con el resultado si es necesario
            }
        }
    }




    private fun validateForm(): Boolean {
        var isValid = true

        with(binding){

            if (etNamesInfoPersonal.text.toString().isEmpty()) {
                isValid = false
                tiNamesInfoPersonal.error = "Campo requerido"
            } else {
                tiNamesInfoPersonal.error = null
            }

            if (etLastNamesInfoPersonal.text.toString().isEmpty()) {
                isValid = false
                tiLastNamesInfoPersonal.error = "Campo requerido"
            } else {
                tiLastNamesInfoPersonal.error = null
            }

            if (etMailInfoPersonal.text.toString().isEmpty()) {
                isValid = false
                tiMailInfoPersonal.error = "Campo requerido"
            } else {
                tiMailInfoPersonal.error = null
            }



            val selectedDocType = spinnerDocType.selectedItem.toString()
            if (selectedDocType == resources.getString(R.string.choose_doc_type)) {
                isValid = false

                llDocType.findViewById<TextView>(R.id.tvDocTypeError).apply {
                    visibility = View.VISIBLE
                    text = "Selecciona un Tipo de Documento!"
                }
            } else {
                // Si el tipo de documento es seleccionado correctamente, ocultamos el error
                llDocType.findViewById<TextView>(R.id.tvDocTypeError).visibility = View.GONE
            }



            if (etDocNumber.text.toString().isEmpty()) {
                isValid = false
                tiDocNumber.error = "Campo requerido"
            } else {
                tiDocNumber.error = null
            }

            if (etPhone.text.toString().isEmpty()) {
                isValid = false
                tiPhone.error = "Campo requerido"
            } else {
                tiPhone.error = null
            }

            if (etAddress.text.toString().isEmpty()) {
                isValid = false
                tiAddress.error = "Campo requerido"
            } else {
                tiAddress.error = null
            }

            if (etBirthDate.text.toString().isEmpty()) {
                isValid = false
                tiBirthDate.error = "Campo requerido"
            } else {
                tiBirthDate.error = null
            }


            val selectedCountry = spinnerCountry.selectedItem.toString()
            if (selectedCountry == resources.getString(R.string.choose_country)) {
                isValid = false

                llCountry.findViewById<TextView>(R.id.tvCountryError).apply {
                    visibility = View.VISIBLE
                    text = "Selecciona un País o Región!"
                }
            } else {
                llCountry.findViewById<TextView>(R.id.tvCountryError).visibility = View.GONE
            }



            if (etCity.text.toString().isEmpty()) {
                isValid = false
                tiCity.error = "Campo requerido"
            } else {
                tiCity.error = null
            }

            if (etLanguage.text.toString().isEmpty()) {
                isValid = false
                tiLanguage.error = "Campo requerido"
            } else {
                tiLanguage.error = null
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