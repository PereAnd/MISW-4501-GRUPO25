package com.example.vinyls.viewmodels

import android.app.Application
import androidx.lifecycle.*
import com.example.vinyls.models.InfoLaboral
import com.example.vinyls.models.repository.InfoLaboralRepository
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import org.json.JSONObject

class AgregarInfoLaboralViewModel(application: Application) :  AndroidViewModel(application)  {
    private val infoLaboralRepository = InfoLaboralRepository(application)

    private val _infoLaboral = MutableLiveData<InfoLaboral>()

    val infoLaboral: LiveData<InfoLaboral>
        get() = _infoLaboral

    private var _eventNetworkError = MutableLiveData<Boolean>(false)

    val eventNetworkError: LiveData<Boolean>
        get() = _eventNetworkError

    private var _isNetworkErrorShown = MutableLiveData<Boolean>(false)

    val isNetworkErrorShown: LiveData<Boolean>
        get() = _isNetworkErrorShown

    suspend fun agregarInfoLaboralFromNetwork(infoLaboral: JSONObject): Int {
        var id: Int = 0 // Inicializar id fuera del bloque try
        try {
            viewModelScope.launch(Dispatchers.Default) {
                withContext(Dispatchers.IO) {
                    var data = infoLaboralRepository.agregarInfoLaboral(infoLaboral)
                    _infoLaboral.postValue(data)
                    id = data.infoLaboralId
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
            if (modelClass.isAssignableFrom(AgregarInfoLaboralViewModel::class.java)) {
                @Suppress("UNCHECKED_CAST")
                return AgregarInfoLaboralViewModel(app) as T
            }
            throw IllegalArgumentException("Unable to construct viewmodel")
        }
    }
}