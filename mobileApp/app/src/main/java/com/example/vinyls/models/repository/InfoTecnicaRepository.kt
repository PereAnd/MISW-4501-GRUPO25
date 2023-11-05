package com.example.vinyls.models.repository

import android.app.Application
import com.example.vinyls.models.InfoTecnica
import com.example.vinyls.models.networkAdapter.NetworkServiceAdapter
import org.json.JSONObject


class InfoTecnicaRepository (val application: Application){

    suspend fun agregarInfoTecnica(infoTecnica: JSONObject): InfoTecnica{
        return NetworkServiceAdapter.getInstance(application).agregarInfoTecnica(infoTecnica)
    }
}