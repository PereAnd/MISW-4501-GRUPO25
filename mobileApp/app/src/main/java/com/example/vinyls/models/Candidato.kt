package com.example.vinyls.models

import java.util.Date

data class Candidato(
    val id: Int,
    val names: String,
    val lastNames: String,
    val mail: String,
    val password: String,
    val confirmPassword: String
) {
    constructor(id: Int, names: String, lastNames: String, mail: String) : this(id, names, lastNames, mail, "", "")
}
