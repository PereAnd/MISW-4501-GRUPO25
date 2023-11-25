package com.example.vinyls.view

import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.lifecycleScope
import androidx.navigation.fragment.findNavController
import com.example.vinyls.R
import com.example.vinyls.databinding.FragmentIngresoEmpresaBinding
import com.example.vinyls.viewmodels.IngresoEmpresaViewModel
import kotlinx.coroutines.async
import kotlinx.coroutines.launch
import org.json.JSONObject
import java.util.*

class FragmentIngresoEmpresa : Fragment(R.layout.fragment_ingreso_empresa) {

    private var _binding: FragmentIngresoEmpresaBinding? = null
    private val binding get() = _binding!!
    private lateinit var viewModel: IngresoEmpresaViewModel

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
    }

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?):
            View? {
        _binding = FragmentIngresoEmpresaBinding.inflate(inflater, container, false)
        val view = binding.root
        return view
    }


    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        var i:Int=0
        val activity = requireNotNull(this.activity) {
            "You can only access the viewModel after onActivityCreated()"
        }
        viewModel = ViewModelProvider(this, IngresoEmpresaViewModel.Factory(activity.application)).get(
            IngresoEmpresaViewModel::class.java)

        createButton()
    }

    private var currentState: Boolean = false

    private fun createButton() {
        binding.buttonMenuEmpresa.setOnClickListener {
            sendDataToServer()

            if (currentState) {
                findNavController().navigate(R.id.action_fragment_menu_login_to_fragment_menu_empresa)
            } else {
                //
            }

        }
    }

    private fun sendDataToServer() {
        var i:Int=0
        if(validateForm()){
            var strEmpresa = "{\n \"mail\": \"" +
                    binding.etMailIngresoEmpresa.text.toString() +
                    "\",\n  \"password\": \"" +
                    binding.etPasswordIngresoEmpresa.text.toString() +
                    "\"\n}"
            Log.i("data Captured",strEmpresa)

            lifecycleScope.launch{
                val idIngresoEmpresad = async { viewModel.ingresoEmpresaFromNetwork(JSONObject(strEmpresa)) }
                i = idIngresoEmpresad.await()
            }



        }
    }

    private fun validateForm(): Boolean {
        var isValid = true

        with(binding){

            if(etMailIngresoEmpresa.text.toString().isEmpty()){
                isValid = false
                tiMailIngresoEmpresa.error = "Campo requerido"
            }else{
                tiMailIngresoEmpresa.error = null
            }

            if (etPasswordIngresoEmpresa.text.toString().isEmpty()) {
                isValid = false
                tiPasswordIngresoEmpresa.error = "Campo requerido"
            } else {
                tiPasswordIngresoEmpresa.error = null
            }

        currentState = isValid
        return currentState

    }


}

}