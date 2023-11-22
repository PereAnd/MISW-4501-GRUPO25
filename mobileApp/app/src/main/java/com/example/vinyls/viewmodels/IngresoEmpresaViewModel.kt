package com.example.vinyls.viewmodels

import android.app.Application
import androidx.lifecycle.*
import com.example.vinyls.models.Empresa
import com.example.vinyls.models.repository.EmpresaRepository
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import org.json.JSONObject

class IngresoEmpresaViewModel (application: Application) :  AndroidViewModel(application)  {
    private val empresaRepository = EmpresaRepository(application)

    private val _empresa = MutableLiveData<Empresa>()

    val empresa: LiveData<Empresa>
        get() = _empresa

    private var _eventNetworkError = MutableLiveData<Boolean>(false)

    val eventNetworkError: LiveData<Boolean>
        get() = _eventNetworkError

    private var _isNetworkErrorShown = MutableLiveData<Boolean>(false)

    val isNetworkErrorShown: LiveData<Boolean>
        get() = _isNetworkErrorShown

    suspend fun ingresoEmpresaFromNetwork(empresa: JSONObject): Int {
        var id: Int = 0 // Inicializar id fuera del bloque try
        try {
            viewModelScope.launch(Dispatchers.Default) {
                withContext(Dispatchers.IO) {
                    var data = empresaRepository.ingresoEmpresa(empresa)
                    _empresa.postValue(data)
                    id = data.empresaId
                }
                _eventNetworkError.postValue(false)
                _isNetworkErrorShown.postValue(false)
            }
        } catch (e: Exception) {
            _eventNetworkError.postValue(true)
        }
        return id // Devolver id, que tendrá 0 si no se pudo completar el ingresoEmpresa
    }


    class Factory(val app: Application) : ViewModelProvider.Factory {
        override fun <T : ViewModel> create(modelClass: Class<T>): T {
            if (modelClass.isAssignableFrom(IngresoEmpresaViewModel::class.java)) {
                @Suppress("UNCHECKED_CAST")
                return IngresoEmpresaViewModel(app) as T
            }
            throw IllegalArgumentException("Unable to construct viewmodel")
        }
    }
}