package com.example.vinyls.models.repository

import android.app.Application
import com.example.vinyls.models.InfoLaboral
import com.example.vinyls.models.networkAdapter.NetworkServiceAdapter
import org.json.JSONObject


class InfoLaboralRepository (val application: Application){

    suspend fun agregarInfoLaboral(infoLaboral: JSONObject): InfoLaboral{
        return NetworkServiceAdapter.getInstance(application).agregarInfoLaboral(infoLaboral)
    }
}