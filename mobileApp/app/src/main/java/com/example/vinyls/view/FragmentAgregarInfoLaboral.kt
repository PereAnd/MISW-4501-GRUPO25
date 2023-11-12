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
import com.example.vinyls.databinding.FragmentAgregarInfoLaboralBinding
import com.example.vinyls.viewmodels.AgregarInfoLaboralViewModel
import com.google.android.material.snackbar.Snackbar
import kotlinx.android.synthetic.main.fragment_agregar_info_laboral.*
import kotlinx.coroutines.async
import kotlinx.coroutines.launch
import org.json.JSONObject
import java.util.*


class FragmentAgregarInfoLaboral : Fragment(R.layout.fragment_agregar_info_laboral) {

    private var _binding: FragmentAgregarInfoLaboralBinding? = null
    private val binding get() = _binding!!  // get
    private lateinit var viewModel: AgregarInfoLaboralViewModel
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?):
            View? {
        _binding = FragmentAgregarInfoLaboralBinding.inflate(inflater, container, false)
        val view = binding.root
        return view
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        var i:Int=0
        val activity = requireNotNull(this.activity) {
            "You can only access the viewModel after onActivityCreated()"
        }
        viewModel = ViewModelProvider(this, AgregarInfoLaboralViewModel.Factory(activity.application)).get(
            AgregarInfoLaboralViewModel::class.java)

        saveButton()
        createButton()
    }

    private var currentState: Boolean = false
    private fun saveButton() {
        binding.btnSaveLabor.setOnClickListener {
            sendDataToServer()


            if (currentState) {
                findNavController().navigate(R.id.action_fragment_infolaboral_fragment_infolaboral)

                Snackbar.make(binding.root, "Datos enviados exitosamente.", Snackbar.LENGTH_LONG)
                    .setAction(""){
                        //   activity?.finish()
                    }.show()
            }
            else {
                //
            }

        }
    }
    private fun createButton() {
        binding.btnLogin.setOnClickListener {
            sendDataToServer()


            if (currentState) {
                findNavController().navigate(R.id.action_fragment_infolaboral_fragment_login)
            }
            else {
                //
            }

        }
    }

    private fun sendDataToServer() {
        var i:Int=0
        if(validateForm()){
            var strInfoLaboral = "{\n \"position\": \"" +
                    binding.etPosition.text.toString() +
                    "\",\n  \"description\":\"" +
                    binding.etDescription.text.toString() +
                    "\",\n  \"type\": \"" +
                    binding.etType.text.toString() +
                    "\",\n  \"organization\": \"" +
                    binding.etOrganization.text.toString() +
                    "\",\n  \"activities\": \"" +
                    binding.etActivities.text.toString() +
                    "\",\n  \"dateFrom\": \"" +
                    binding.etDateFrom.text.toString() +
                    "\",\n  \"dateTo\": \"" +
                    binding.etDateTo.text.toString() +
                    "\"\n}"
            Log.i("data Captured",strInfoLaboral)

            lifecycleScope.launch{
                val idAgregarInfoLaboral = async { viewModel.agregarInfoLaboralFromNetwork(JSONObject(strInfoLaboral)) }
                i = idAgregarInfoLaboral.await()
            }

            Snackbar.make(binding.root, "Datos enviados exitosamente.", Snackbar.LENGTH_LONG)
                .setAction(""){
                activity?.finish()
            }.show()

        }
    }

    private fun validateForm(): Boolean {
        var isValid = true

        with(binding){
            if(etPosition.text.toString().isEmpty()){
                isValid = false
                tiPosition.error = "Campo requerido"
            }else{
                tiPosition.error = null
            }

            if(etDescription.text.toString().isEmpty()){
                isValid = false
                tiDescription.error = "Campo requerido"
            }else{
                tiDescription.error = null
            }

            if (etType.text.toString().isEmpty()) {
                isValid = false
                tiType.error = "Campo requerido"
            } else {
                tiType.error = null
            }

            if (etOrganization.text.toString().isEmpty()) {
                isValid = false
                tiOrganization.error = "Campo requerido"
            } else {
                tiOrganization.error = null
            }

            if (etActivities.text.toString().isEmpty()) {
                isValid = false
                tiActivities.error = "Campo requerido"
            } else {
                tiActivities.error = null
            }

            if (etDateFrom.text.toString().isEmpty()) {
                isValid = false
                tiDateFrom.error = "Campo requerido"
            } else {
                tiDateFrom.error = null
            }

            if(etDateTo.text.toString().isEmpty()){
                isValid = false
                tiDateTo.error = "Campo requerido"
            }else{
                tiDateTo.error = null
            }
        }
        currentState = isValid
        return currentState

    }


}