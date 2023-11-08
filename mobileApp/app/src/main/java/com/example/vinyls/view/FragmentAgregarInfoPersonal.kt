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

class FragmentAgregarInfoPersonal : Fragment(R.layout.fragment_agregar_info_personal) {

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
    }


    private var _binding: FragmentAgregarInfoPersonalBinding? = null
    private val binding get() = _binding!!  // get
    private lateinit var viewModel: AgregarInfoPersonalViewModel


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

    private fun sendDataToServer() {
        var i:Int=0
        if(validateForm()){
            var strInfoPersonal = "{\n \"names\": \"" +
                    binding.etNamesInfoPersonal.text.toString() +
                    "\",\n  \"lastNames\":\"" +
                    binding.etLastNamesInfoPersonal.text.toString() +
                    "\",\n  \"mail\": \"" +
                    binding.etMailInfoPersonal.text.toString() +
                    "\",\n  \"docType\": \"" +
                    binding.etDocType.text.toString() +
                    "\",\n  \"docNumber\": \"" +
                    binding.etDocNumber.text.toString() +
                    "\",\n  \"phone\": \"" +
                    binding.etPhone.text.toString() +
                    "\",\n  \"address\": \"" +
                    binding.etAddress.text.toString() +
                    "\",\n  \"birthDate\": \"" +
                    binding.etBirthDate.text.toString() +
                    "\",\n  \"country\": \"" +
                    binding.etCountry.text.toString() +
                    "\",\n  \"city\": \"" +
                    binding.etCity.text.toString() +
                    "\",\n  \"language\": \"" +
                    binding.etLanguage.text.toString() +
                    "\"\n}"

            Log.i("data Captured",strInfoPersonal)

            lifecycleScope.launch{
                val idAgregarInfoPersonal = async { viewModel.agregarInfoPersonalFromNetwork(JSONObject(strInfoPersonal)) }
                i = idAgregarInfoPersonal.await()
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

            if (etDocType.text.toString().isEmpty()) {
                isValid = false
                tiDocType.error = "Campo requerido"
            } else {
                tiDocType.error = null
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

            if (etCountry.text.toString().isEmpty()) {
                isValid = false
                tiCountry.error = "Campo requerido"
            } else {
                tiCountry.error = null
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


}