package com.example.vinyls.models.repository

import android.app.Application
import com.example.vinyls.models.Entrevista
import com.example.vinyls.models.networkAdapter.NetworkServiceAdapter
import org.json.JSONObject


class EntrevistaRepository (val application: Application){

    suspend fun refreshData(): List<Entrevista>{
        return NetworkServiceAdapter.getInstance(application).getEntrevistas()
    }

}