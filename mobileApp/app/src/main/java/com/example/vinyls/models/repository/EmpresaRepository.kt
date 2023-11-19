package com.example.vinyls.models.repository

import android.app.Application
import com.example.vinyls.models.Empresa
import com.example.vinyls.models.networkAdapter.NetworkServiceAdapter
import org.json.JSONObject


class EmpresaRepository (val application: Application){

    suspend fun refreshData(): List<Empresa>{
        return NetworkServiceAdapter.getInstance(application).getEmpresa()
    }

}