package com.example.vinyls.viewmodels

import android.app.Application
import android.util.Log
import androidx.lifecycle.*
import com.example.vinyls.models.Candidato
import com.example.vinyls.models.repository.CandidatoRepository
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
//import org.json.JSONObject

class CandidatoListViewModel (application: Application) :  AndroidViewModel(application) {
    private val candidatoRepository = CandidatoRepository(application)

    private val _candidatos = MutableLiveData<List<Candidato>>()

    val candidatos: LiveData<List<Candidato>>
        get() = _candidatos

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
                    val data = candidatoRepository.refreshData()
                    _candidatos.postValue(data)
                }
                _eventNetworkError.postValue(false)
                _isNetworkErrorShown.postValue(false)
            } catch (e: Exception) {
                Log.e("CandidatoListViewModel", "Error al actualizar datos desde la red", e)
                _eventNetworkError.postValue(true)
            }
        }
    }

    fun onNetworkErrorShown() {
        _isNetworkErrorShown.value = true
    }

    class Factory(val app: Application) : ViewModelProvider.Factory {
        override fun <T : ViewModel> create(modelClass: Class<T>): T {
            if (modelClass.isAssignableFrom(CandidatoListViewModel::class.java)) {
                @Suppress("UNCHECKED_CAST")
                return CandidatoListViewModel(app) as T
            }
            throw IllegalArgumentException("Unable to construct viewmodel")
        }
    }
}

