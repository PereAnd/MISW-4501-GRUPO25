package com.example.vinyls.viewmodels

import android.app.Application
import androidx.lifecycle.*
import com.example.vinyls.models.InfoAcademica
import com.example.vinyls.models.repository.InfoAcademicaRepository
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import org.json.JSONObject

class AgregarInfoAcademicaViewModel(application: Application) :  AndroidViewModel(application)  {
    private val infoAcademicaRepository = InfoAcademicaRepository(application)

    private val _infoAcademica = MutableLiveData<InfoAcademica>()

    val infoAcademica: LiveData<InfoAcademica>
        get() = _infoAcademica

    private var _eventNetworkError = MutableLiveData<Boolean>(false)

    val eventNetworkError: LiveData<Boolean>
        get() = _eventNetworkError

    private var _isNetworkErrorShown = MutableLiveData<Boolean>(false)

    val isNetworkErrorShown: LiveData<Boolean>
        get() = _isNetworkErrorShown

    suspend fun agregarInfoAcademicaFromNetwork(infoAcademica: JSONObject): Int {
        var id: Int = 0 // Inicializar id fuera del bloque try
        try {
            viewModelScope.launch(Dispatchers.Default) {
                withContext(Dispatchers.IO) {
                    var data = infoAcademicaRepository.agregarInfoAcademica(infoAcademica)
                    _infoAcademica.postValue(data)
                    id = data.infoAcademicaId
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
            if (modelClass.isAssignableFrom(AgregarInfoAcademicaViewModel::class.java)) {
                @Suppress("UNCHECKED_CAST")
                return AgregarInfoAcademicaViewModel(app) as T
            }
            throw IllegalArgumentException("Unable to construct viewmodel")
        }
    }
}