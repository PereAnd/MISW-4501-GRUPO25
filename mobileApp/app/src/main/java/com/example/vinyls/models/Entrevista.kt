package com.example.vinyls.models

import java.util.Date

data class Entrevista(
    val entrevistaId: Int,
    val nameCandidato: String,
    val lastNameCandidato: String,
    val fecha: String,
    val hora: String,
    val reclutador: String,
    val direcction: String,
    val status: String,
    val observatios: String
    )