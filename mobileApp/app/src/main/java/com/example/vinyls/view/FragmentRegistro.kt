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
import com.example.vinyls.databinding.FragmentRegistroBinding
import com.example.vinyls.viewmodels.RegistroViewModel
import com.google.android.material.snackbar.Snackbar
import kotlinx.android.synthetic.main.fragment_registro.*
import kotlinx.coroutines.async
import kotlinx.coroutines.launch
import org.json.JSONObject
import java.util.*
class FragmentRegistro : Fragment(R.layout.fragment_menu_login) {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val buttonNextAcademic = requireView().findViewById<Button>(R.id.btnNextAcademic)

        buttonNextAcademic.setOnClickListener {
            findNavController().navigate(R.id.action_fragment_registro_login_to_fragment_infoAcademica)
        }
    }



    private var _binding: FragmentRegistroBinding? = null
    private val binding get() = _binding!!  // get
    private lateinit var viewModel: RegistroViewModel
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?):
            View? {
        _binding = FragmentRegistroBinding.inflate(inflater, container, false)
        val view = binding.root
        return view
    }


    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        var i:Int=0
        val activity = requireNotNull(this.activity) {
            "You can only access the viewModel after onActivityCreated()"
        }
        viewModel = ViewModelProvider(this, RegistroViewModel.Factory(activity.application)).get(
            RegistroViewModel::class.java)

        createButton()
    }

    private fun createButton() {
        binding.btnSendCandidato.setOnClickListener {
            sendDataToServer()
        }
    }

    private fun sendDataToServer() {
        var i:Int=0
        if(validateForm()){
            var strCandidato = "{\n \"names\": \"" +
                    binding.etNamesRegistro.text.toString() +
                    "\",\n  \"lastNames\":\"" +
                    binding.etLastNamesRegistro.text.toString() +
                    "\",\n  \"password\": \"" +
                    binding.etPasswordRegistro.text.toString() +
                    "\",\n  \"confirmPassword\": \"" +
                    binding.etConfirmPasswordRegistro.text.toString() +
                    "\",\n  \"mail\": \"" +
                    binding.etMailRegistro.text.toString() +
                    "\"\n}"
            Log.i("data Captured",strCandidato)

            lifecycleScope.launch{
                val idRegistrod = async { viewModel.registroFromNetwork(JSONObject(strCandidato)) }
                i = idRegistrod.await()
            }

            Snackbar.make(binding.root, "Datos enviados exitosamente.", Snackbar.LENGTH_LONG)
                .setAction("¿Salir?"){
                activity?.finish()
            }.show()
            
        }
    }

    private fun validateForm(): Boolean {
        var isValid = true

        with(binding){
            if(etNamesRegistro.text.toString().isEmpty()){
                isValid = false
                tiNamesRegistro.error = "Campo requerido"
            }else{
                tiNamesRegistro.error = null
            }

            if(etLastNamesRegistro.text.toString().isEmpty()){
                isValid = false
                tiLastNamesRegistro.error = "Campo requerido"
            }else{
                tiLastNamesRegistro.error = null
            }


            if (etPasswordRegistro.text.toString().isEmpty()) {
                isValid = false
                tiPasswordRegistro.error = "Campo requerido"
            } else {
                tiPasswordRegistro.error = null
            }

            if (etConfirmPasswordRegistro.text.toString().isEmpty()) {
                isValid = false
                tiConfirmPasswordRegistro.error = "Campo requerido"
            } else {
                tiConfirmPasswordRegistro.error = null
            }

            if(etMailRegistro.text.toString().isEmpty()){
                isValid = false
                tiMailRegistro.error = "Campo requerido"
            }else{
                tiMailRegistro.error = null
            }
        }

        return isValid

    }


}