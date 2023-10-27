package com.example.vinyls.viewmodels

import android.app.Application
import androidx.lifecycle.*
import com.example.vinyls.models.Candidato
import com.example.vinyls.models.repository.CandidatoRepository
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.withContext
import org.json.JSONObject

class RegistroViewModel (application: Application) :  AndroidViewModel(application)  {
    private val candidatoRepository = CandidatoRepository(application)

    private val _candidato = MutableLiveData<Candidato>()

    val candidato: LiveData<Candidato>
        get() = _candidato

    private var _eventNetworkError = MutableLiveData<Boolean>(false)

    val eventNetworkError: LiveData<Boolean>
        get() = _eventNetworkError

    private var _isNetworkErrorShown = MutableLiveData<Boolean>(false)

    val isNetworkErrorShown: LiveData<Boolean>
        get() = _isNetworkErrorShown

    suspend fun registroFromNetwork(candidato: JSONObject): Int {
        var id: Int = 0
        try {
            viewModelScope.launch(Dispatchers.Default) {
                withContext(Dispatchers.IO) {
                    var data = candidatoRepository.registro(candidato)
                    _candidato.postValue(data)
                    id= data.candidatoId
                }
                _eventNetworkError.postValue(false)
                _isNetworkErrorShown.postValue(false)
            }


        }
        catch (e:Exception){
            _eventNetworkError.value = true
        }
        return id

    }

    class Factory(val app: Application) : ViewModelProvider.Factory {
        override fun <T : ViewModel> create(modelClass: Class<T>): T {
            if (modelClass.isAssignableFrom(RegistroViewModel::class.java)) {
                @Suppress("UNCHECKED_CAST")
                return RegistroViewModel(app) as T
            }
            throw IllegalArgumentException("Unable to construct viewmodel")
        }
    }
}