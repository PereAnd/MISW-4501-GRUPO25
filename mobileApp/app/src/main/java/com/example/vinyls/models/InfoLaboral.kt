package com.example.vinyls.models

data class InfoLaboral (
    val infoLaboralId:Int,
    val description:String,
    val type:String,
    val organization:String,
    val activities:String,
    val dateFrom:String,
    val dateTo:String,
    val candidatoId: Int
)


