package com.example.vinyls.models

data class InfoAcademica (
    val infoAcademicaId:Int,
    val title:String,
    val institution:String,
    val beginDate:String,
    val endDate:String,
    val studyType:String,
    val candidatoId: Int
)

