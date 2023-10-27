package com.example.vinyls.models.repository

import android.app.Application
import com.example.vinyls.models.Candidato
import com.example.vinyls.models.networkAdapter.NetworkServiceAdapter
import org.json.JSONObject


class CandidatoRepository (val application: Application){

    suspend fun refreshData(): List<Candidato>{
        return NetworkServiceAdapter.getInstance(application).getCandidatos()
    }
    suspend fun registro(candidato: JSONObject): Candidato{
        return NetworkServiceAdapter.getInstance(application).registro(candidato)
    }
}