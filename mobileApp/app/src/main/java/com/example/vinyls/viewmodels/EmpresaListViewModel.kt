package com.example.vinyls.viewmodels

import android.app.Application
import android.util.Log
import androidx.lifecycle.*
import com.example.vinyls.models.Empresa
import com.example.vinyls.models.repository.EmpresaRepository
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
//import org.json.JSONObject

class EmpresaListViewModel (application: Application) :  AndroidViewModel(application) {
    private val empresaRepository = EmpresaRepository(application)

    private val _empresas = MutableLiveData<List<Empresa>>()

    val empresas: LiveData<List<Empresa>>
        get() = _empresas

    private var _eventNetworkError = MutableLiveData<Boolean>(false)

    val eventNetworkError: LiveData<Boolean>
        get() = _eventNetworkError

    private var _isNetworkErrorShown = MutableLiveData<Boolean>(false)

    val isNetworkErrorShown: LiveData<Boolean>
        get() = _isNetworkErrorShown

    init {
        refreshDataFromNetwork()
    }


    private fun refreshDataFromNetwork() {
        viewModelScope.launch(Dispatchers.Default) {
            try {
                withContext(Dispatchers.IO) {
                    val data = empresaRepository.refreshData()
                    _empresas.postValue(data)
                }
                _eventNetworkError.postValue(false)
                _isNetworkErrorShown.postValue(false)
            } catch (e: Exception) {
                Log.e("EmpresaListViewModel", "Error al actualizar datos desde la red", e)
                _eventNetworkError.postValue(true)
            }
        }
    }

    fun onNetworkErrorShown() {
        _isNetworkErrorShown.value = true
    }

    class Factory(val app: Application) : ViewModelProvider.Factory {
        override fun <T : ViewModel> create(modelClass: Class<T>): T {
            if (modelClass.isAssignableFrom(EmpresaListViewModel::class.java)) {
                @Suppress("UNCHECKED_CAST")
                return EmpresaListViewModel(app) as T
            }
            throw IllegalArgumentException("Unable to construct viewmodel")
        }
    }
}

