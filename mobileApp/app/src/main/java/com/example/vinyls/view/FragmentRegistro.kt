package com.example.vinyls.view

import android.os.Bundle
import android.text.Editable
import android.text.TextWatcher
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.fragment.app.viewModels
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.lifecycleScope
import com.example.vinyls.R
import com.example.vinyls.databinding.FragmentAlbumCreateBinding
import com.example.vinyls.viewmodels.AlbumCreateViewModel
import com.google.android.material.snackbar.Snackbar
import kotlinx.android.synthetic.main.fragment_album_create.*
import kotlinx.coroutines.async
import kotlinx.coroutines.launch
import org.json.JSONObject
import java.util.*
class FragmentRegistro : Fragment() {
    private var _binding: FragmentAlbumCreateBinding? = null
    private val binding get() = _binding!!  // get
    private lateinit var viewModel: AlbumCreateViewModel
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?):
            View? {
        _binding = FragmentAlbumCreateBinding.inflate(inflater, container, false)
        val view = binding.root
        return view
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        var i:Int=0
        val activity = requireNotNull(this.activity) {
            "You can only access the viewModel after onActivityCreated()"
        }
        viewModel = ViewModelProvider(this, AlbumCreateViewModel.Factory(activity.application)).get(
            AlbumCreateViewModel::class.java)

        createButton()

    }

    private fun createButton() {
        binding.btnSendAlbum.setOnClickListener {
            sendDataToServer()
        }
    }

    private fun sendDataToServer() {
        var i:Int=0
        if(validateForm()){
            var strAlbum = "{\n \"names\": \"" +
                    binding.etNameCreateAlbum.text.toString() +
                    "\",\n  \"lastNames\":\"" +
                    binding.etCoverCreateAlbum.text.toString() +
                    "\",\n  \"password\": \"" +
                    binding.etReleaseDateCreateAlbum.text.toString() +
                    "\",\n  \"confirmPassword\": \"" +
                    binding.etReleaseDateCreateAlbum.text.toString() +
                    "\",\n  \"mai\": \"" +
                    "\"\n}"
            Log.i("data Captured",strAlbum)

            lifecycleScope.launch{
                val idAlbumCreated = async { viewModel.createAlbumFromNetwork(JSONObject(strAlbum)) }
                i = idAlbumCreated.await()
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
            if(etNameCreateAlbum.text.toString().isEmpty()){
                isValid = false
                tiNameCreateAlbum.error = "Campo requerido"
            }else{
                tiNameCreateAlbum.error = null
            }
            if(tbGenre.checkedButtonId==-1){
                isValid = false
                tvGenreCreateAlbum.error = "Campo requerido"
            }else{
                tvGenreCreateAlbum.error = null
            }
            if(rgRecordLabelCreateAlbum.checkedRadioButtonId==-1){
                isValid = false
                tvRecordLabelCreateAlbum.error = "Campo requerido"
            }else{
                tvGenreCreateAlbum.error = null
            }
            if(etReleaseDateCreateAlbum.text.toString().matches(".*[A-Z].*".toRegex()) || etReleaseDateCreateAlbum.text.toString().matches(".*[a-z].*".toRegex())){
               isValid = false
                tiReleaseDateCreateAlbum.error = "Datos incorrectos de fecha"
            }
            else{
                tiReleaseDateCreateAlbum.error = null
            }
            if(etDescriptionCreateAlbum.text.toString().isEmpty()){
                isValid = false
                tiDescriptionCreateAlbum.error = "Campo requerido"
            }else{
                tiDescriptionCreateAlbum.error = null
            }

            if(etCoverCreateAlbum.text.toString().isEmpty()){
                isValid = false
                tiCoverCreateAlbum.error = "Campo requerido"
            }else{
                tiCoverCreateAlbum.error = null
            }
            if(etReleaseDateCreateAlbum.text.toString().isEmpty()){
                isValid = false
                tiReleaseDateCreateAlbum.error = "Campo requerido"
            }else{
                tiReleaseDateCreateAlbum.error = null
            }

        }

        return isValid

    }

}