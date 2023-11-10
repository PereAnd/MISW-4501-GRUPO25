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
import com.example.vinyls.databinding.FragmentAgregarInfoAcademicaBinding
import com.example.vinyls.viewmodels.AgregarInfoAcademicaViewModel
import com.google.android.material.snackbar.Snackbar
import kotlinx.android.synthetic.main.fragment_agregar_info_academica.*
import kotlinx.coroutines.async
import kotlinx.coroutines.launch
import org.json.JSONObject
import java.util.*


class FragmentAgregarInfoAcademica : Fragment(R.layout.fragment_agregar_info_academica) {

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

    //    val buttonNextTecnic = requireView().findViewById<Button>(R.id.btnNextTecnic)

     //   buttonNextTecnic.setOnClickListener {
   //         findNavController().navigate(R.id.action_fragment_infoAcademica_fragment_infoTecnica)
    //    }
    }




    private var _binding: FragmentAgregarInfoAcademicaBinding? = null
    private val binding get() = _binding!!  // get
    private lateinit var viewModel: AgregarInfoAcademicaViewModel


    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?):
            View? {
        _binding = FragmentAgregarInfoAcademicaBinding.inflate(inflater, container, false)
        val view = binding.root
        return view
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        var i:Int=0
        val activity = requireNotNull(this.activity) {
            "You can only access the viewModel after onActivityCreated()"
        }
        viewModel = ViewModelProvider(this, AgregarInfoAcademicaViewModel.Factory(activity.application)).get(
            AgregarInfoAcademicaViewModel::class.java)

        createButton()
    }

    private var currentState: Boolean = false
    private fun createButton() {
        binding.btnNextTecnic.setOnClickListener {
            sendDataToServer()

            if (currentState) {
                findNavController().navigate(R.id.action_fragment_infoAcademica_fragment_infoTecnica)
            }
            else {
                //
            }


        }
    }

    private fun sendDataToServer() {
        var i:Int=0
        if(validateForm()){
            var strInfoAcademica = "{\n \"title\": \"" +
                    binding.etTitle.text.toString() +
                    "\",\n  \"institution\":\"" +
                    binding.etInstitution.text.toString() +
                    "\",\n  \"beginDate\": \"" +
                    binding.etBeginDate.text.toString() +
                    "\",\n  \"endDate\": \"" +
                    binding.etEndDate.text.toString() +
                    "\",\n  \"studyType\": \"" +
                    binding.etStudyType.text.toString() +
                    "\"\n}"
            Log.i("data Captured",strInfoAcademica)

            lifecycleScope.launch{
                val idAgregarInfoAcademica = async { viewModel.agregarInfoAcademicaFromNetwork(JSONObject(strInfoAcademica)) }
                i = idAgregarInfoAcademica.await()
            }

        }
    }

    private fun validateForm(): Boolean {
        var isValid = true

        with(binding){
            if(etTitle.text.toString().isEmpty()){
                isValid = false
                tiTitle.error = "Campo requerido"
            }else{
                tiTitle.error = null
            }

            if(etInstitution.text.toString().isEmpty()){
                isValid = false
                tiInstitution.error = "Campo requerido"
            }else{
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

            if(etStudyType.text.toString().isEmpty()){
                isValid = false
                tiStudyType.error = "Campo requerido"
            }else{
                tiStudyType.error = null
            }
        }
        currentState = isValid
        return currentState
    }


}