package com.example.vinyls.models.repository

import android.app.Application
import com.example.vinyls.models.InfoAcademica
import com.example.vinyls.models.networkAdapter.NetworkServiceAdapter
import org.json.JSONObject


class InfoAcademicaRepository (val application: Application){

   // suspend fun refreshData(): List<InfoAcademica>{
     //   return NetworkServiceAdapter.getInstance(application).getInfoAcademica()
  //  }
    suspend fun agregarInfoAcademica(infoAcademica: JSONObject): InfoAcademica{
        return NetworkServiceAdapter.getInstance(application).agregarInfoAcademica(infoAcademica)
    }
}