package com.example.vinyls.models

import java.util.Date

data class Candidato (
    val candidatoId:Int,
    val names:String,
    val lastNames:String,
    val password:String,
    val confirmPassword:String,
    val mail:String
)