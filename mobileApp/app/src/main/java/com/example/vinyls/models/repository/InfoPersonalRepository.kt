package com.example.vinyls.models.repository

import android.app.Application
import com.example.vinyls.models.InfoPersonal
import com.example.vinyls.models.networkAdapter.NetworkServiceAdapter
import org.json.JSONObject


class InfoPersonalRepository (val application: Application){

    suspend fun agregarInfoPersonal(infoPersonal: JSONObject): InfoPersonal{
        return NetworkServiceAdapter.getInstance(application).agregarInfoPersonal(infoPersonal)
    }
}