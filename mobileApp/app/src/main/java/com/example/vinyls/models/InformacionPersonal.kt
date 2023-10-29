package com.example.vinyls.models

import java.util.Date

data class InformacionPersonal (
    val id:Int,
    val names:String,
    val lastNames:String,
    val mail:String,
    val password:String,
    val docType:String,
    val docNumber:String,
    val phone:String,
    val address:String,
    val birthDate:String,
    val country:String,
    val city:String,
    val language:String
)