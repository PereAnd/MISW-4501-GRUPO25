package com.example.vinyls.viewmodels

import android.app.Application
import androidx.lifecycle.*
import com.example.vinyls.models.InfoTecnica
import com.example.vinyls.models.repository.InfoTecnicaRepository
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import org.json.JSONObject

class AgregarInfoTecnicaViewModel(application: Application) :  AndroidViewModel(application)  {
    private val infoTecnicaRepository = InfoTecnicaRepository(application)

    private val _infoTecnica = MutableLiveData<InfoTecnica>()

    val infoTecnica: LiveData<InfoTecnica>
        get() = _infoTecnica

    private var _eventNetworkError = MutableLiveData<Boolean>(false)

    val eventNetworkError: LiveData<Boolean>
        get() = _eventNetworkError

    private var _isNetworkErrorShown = MutableLiveData<Boolean>(false)

    val isNetworkErrorShown: LiveData<Boolean>
        get() = _isNetworkErrorShown

    suspend fun agregarInfoTecnicaFromNetwork(infoTecnica: JSONObject): Int {
        var id: Int = 0 // Inicializar id fuera del bloque try
        try {
            viewModelScope.launch(Dispatchers.Default) {
                withContext(Dispatchers.IO) {
                    var data = infoTecnicaRepository.agregarInfoTecnica(infoTecnica)
                    _infoTecnica.postValue(data)
                    id = data.infoTecnicaId
                }
                _eventNetworkError.postValue(false)
                _isNetworkErrorShown.postValue(false)
            }
        } catch (e: Exception) {
            _eventNetworkError.postValue(true)
        }
        return id // Devolver id, que tendrá 0 si no se pudo completar el registro
    }


    class Factory(val app: Application) : ViewModelProvider.Factory {
        override fun <T : ViewModel> create(modelClass: Class<T>): T {
            if (modelClass.isAssignableFrom(AgregarInfoTecnicaViewModel::class.java)) {
                @Suppress("UNCHECKED_CAST")
                return AgregarInfoTecnicaViewModel(app) as T
            }
            throw IllegalArgumentException("Unable to construct viewmodel")
        }
    }
}