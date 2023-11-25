package com.example.vinyls.models

import java.util.Date

data class Entrevista(
    val entrevistaId: Int,
    val fullName: String,
    val applicationDate: String,
    val status: String,
    val enterviewDate: String,
    val result: String,
    val feedback: String
    )