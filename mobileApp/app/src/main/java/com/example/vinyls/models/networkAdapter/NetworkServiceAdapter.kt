package com.example.vinyls.models.networkAdapter
import android.content.Context
import com.android.volley.Request
import com.android.volley.RequestQueue
import com.android.volley.Response
import com.android.volley.VolleyError
import com.android.volley.toolbox.JsonObjectRequest
import com.android.volley.toolbox.StringRequest
import com.android.volley.toolbox.Volley
import com.example.vinyls.models.Candidato
import com.example.vinyls.models.InfoAcademica
import com.example.vinyls.models.InfoPersonal
import com.example.vinyls.models.InfoTecnica
import com.example.vinyls.models.InfoLaboral
import com.example.vinyls.models.Empresa
import com.example.vinyls.models.Entrevista
import org.json.JSONArray
import org.json.JSONObject
import kotlin.coroutines.resume
import kotlin.coroutines.resumeWithException
import kotlin.coroutines.suspendCoroutine
import android.util.Log

class NetworkServiceAdapter constructor(context: Context) {
    companion object{
        const val BASE_URL = "http://candidatos.us-east-2.elasticbeanstalk.com/"
        var instance: NetworkServiceAdapter? = null
        fun getInstance(context: Context) =
            instance ?: synchronized(this) {
                instance ?: NetworkServiceAdapter(context).also {
                    instance = it
                }
            }
    }
    private val requestQueue: RequestQueue by lazy {
        // applicationContext keeps you from leaking the Activity or BroadcastReceiver if someone passes one in.
        Volley.newRequestQueue(context.applicationContext)
    }
    suspend fun getCandidatos() = suspendCoroutine<List<Candidato>> { cont ->
        requestQueue.add(getRequest("candidato",
            { response ->
                val resp = JSONArray(response)
                val list = mutableListOf<Candidato>()

                for (i in 0 until resp.length()) {
                    val item = resp.getJSONObject(i)

                    val candidatoId = item.getInt("id")
                    val names = item.getString("names")
                    val lastNames = item.getString("lastNames")
                    val mail = item.getString("mail")

                    val password = if (item.has("password")) {
                        item.getString("password")
                    } else { "nd" }
                    val confirmPassword = if (item.has("confirmPassword")) {
                        item.getString("confirmPassword")
                    } else { "nd" }

                    list.add(i, Candidato(candidatoId = candidatoId, names = names, lastNames = lastNames, password = password,
                                        confirmPassword = confirmPassword, mail = mail))
                }
                cont.resume(list)
            },
            {
                cont.resumeWithException(it)
            })
        )
    }


    private var currentCandidatoId: Int = -1 // Inicializa con un valor que no se usará en la aplicación
    suspend fun registro(body: JSONObject) = suspendCoroutine<Candidato> { cont ->
        requestQueue.add(postRequest("candidato", body,
            { response ->
                val candidatoId = response.getInt("id")
                currentCandidatoId = candidatoId // Almacena el candidatoId
                val names = response.getString("names")
                val lastNames = response.getString("lastNames")
                val mail = response.getString("mail")
                val password = response.optString("password", "Sin password") // Valor predeterminado
                val confirmPassword = response.optString("confirmPassword", "Sin confirmPassword")

                val candidato = Candidato(
                    candidatoId = candidatoId,
                    names = names,
                    lastNames = lastNames,
                    mail = mail,
                    password = password,
                    confirmPassword = confirmPassword
                )
                cont.resume(candidato)
            },
            {
                cont.resumeWithException(it)
            }
        ))
    }

    suspend fun agregarInfoAcademica(body: JSONObject): InfoAcademica {
        return suspendCoroutine { cont ->

            if (currentCandidatoId == -1) {
               // cont.resumeWithException(NoValidCandidatoIdException("No se encontró un candidatoId válido."))
              //  return@suspendCoroutine
            }

            requestQueue.add(postRequest("candidato/$currentCandidatoId/informacionAcademica", body,
                { response ->
                    val infoAcademicaId = response.getInt("id")
                    val title = response.getString("title")
                    val institution = response.getString("institution")
                    val beginDate = response.getString("beginDate")
                    val endDate = response.getString("endDate")
                    val studyType = response.getString("studyType")
                    val candidatoId = response.getInt("candidatoId")

                    val infoAcademica = InfoAcademica(
                        infoAcademicaId = infoAcademicaId,
                        title = title,
                        institution = institution,
                        beginDate = beginDate,
                        endDate = endDate,
                        studyType = studyType,
                        candidatoId = candidatoId
                    )

                    cont.resume(infoAcademica)
                },
                {
                    cont.resumeWithException(it)
                }
            ))
        }
    }


    suspend fun agregarInfoTecnica(body: JSONObject): InfoTecnica {
        return suspendCoroutine { cont ->

            if (currentCandidatoId == -1) {
                // Handle this situation appropriately, for example, by throwing an exception.
                // return@suspendCoroutine
            }

            requestQueue.add(postRequest("candidato/$currentCandidatoId/informacionTecnica", body,
                { response ->
                    val infoTecnicaId = response.getInt("id")
                    val description = response.getString("description")
                    val type = response.getString("type")
                    val candidatoId = response.getInt("candidatoId")

                    val infoTecnica = InfoTecnica(
                        infoTecnicaId = infoTecnicaId,
                        description = description,
                        type = type,
                        candidatoId = candidatoId
                    )

                    cont.resume(infoTecnica)
                },
                {
                    cont.resumeWithException(it)
                }
            ))
        }
    }



    suspend fun agregarInfoLaboral(body: JSONObject): InfoLaboral {
        return suspendCoroutine { cont ->

            if (currentCandidatoId == -1) {
                // Handle this situation appropriately, for example, by throwing an exception.
                // return@suspendCoroutine
            }

            requestQueue.add(postRequest("candidato/$currentCandidatoId/informacionLaboral", body,
                { response ->
                    val infoLaboralId = response.getInt("id")
                    val description = response.optString("description", "Sin description")
                    val type = response.optString("type",  "Sin type")
                    val position = response.getString("position")
                    val organization = response.getString("organization")
                    val activities = response.getString("activities")
                    val dateFrom = response.getString("dateFrom")
                    val dateTo = response.getString("dateTo")
                    val candidatoId = response.getInt("candidatoId")

                    val infoLaboral = InfoLaboral(
                        infoLaboralId = infoLaboralId,
                        description = description,
                        position = position,
                        type = type,
                        organization = organization,
                        activities = activities,
                        dateFrom = dateFrom,
                        dateTo = dateTo,
                        candidatoId = candidatoId
                    )

                    cont.resume(infoLaboral)
                },
                {
                    cont.resumeWithException(it)
                }
            ))
        }
    }


    suspend fun agregarInfoPersonal(body: JSONObject): InfoPersonal {
        return suspendCoroutine { cont ->

            if (currentCandidatoId == -1) {
                // Handle this situation appropriately, for example, by throwing an exception.
                // return@suspendCoroutine
            }

            requestQueue.add(patchRequest("candidato/$currentCandidatoId", body,
                { response ->
                    val infoPersonaId = response.getInt("id")
                    val names = response.getString("names")
                    val lastNames = response.getString("lastNames")
                    val mail = response.getString("mail")
                    val docType = response.getString("docType")
                    val docNumber = response.getString("docNumber")
                    val phone = response.getString("phone")
                    val address = response.getString("address")
                    val birthDate = response.getString("birthDate")
                    val country = response.getString("country")
                    val city = response.getString("city")
                    val language = response.getString("language")
                    val informacionAcademica = response.optString("informacionAcademica", "Sin información académica")
                    val informacionTecnica = response.optString("informacionTecnica", "Sin información técnica")

                    val infoPersonal = InfoPersonal(
                        infoPersonalId = infoPersonaId,
                        names = names,
                        lastNames = lastNames,
                        mail = mail,
                        docType = docType,
                        docNumber = docNumber,
                        phone = phone,
                        address = address,
                        birthDate = birthDate,
                        country = country,
                        city = city,
                        language = language,
                        informacionAcademica = informacionAcademica,
                        informacionTecnica = informacionTecnica
                    )

                    cont.resume(infoPersonal)
                },
                {
                    cont.resumeWithException(it)
                }
            ))
        }
    }


    private var currentEmpresaId: Int = -1
    suspend fun ingresoEmpresa(body: JSONObject) = suspendCoroutine<Empresa> { cont ->
        requestQueue.add(postRequest("login", body,
            { response ->
                val empresaId = response.getInt("id_empresa")
                currentEmpresaId = empresaId
                val mail = response.optString("mail", "Sin mail")
                val password = response.optString("password", "Sin password")

                val empresa = Empresa(
                    empresaId = empresaId,
                    mail = mail,
                    password = password
                )
                cont.resume(empresa)
            },
            {
                cont.resumeWithException(it)
                Log.e("NetworkServiceAdapter", "Error en la solicitud", it)
            }
        ))
    }



    suspend fun getEntrevistas() = suspendCoroutine<List<Entrevista>> { cont ->
        if (currentEmpresaId == -1) {
            // Handle this situation appropriately, for example, by throwing an exception.
            // return@suspendCoroutine
        }
        requestQueue.add(getRequest("empresa/$currentEmpresaId/entrevistas",
            { response ->
                val resp = JSONArray(response)
                val list = mutableListOf<Entrevista>()

                for (i in 0 until resp.length()) {
                    val item = resp.getJSONObject(i)

                    val entrevistaId = item.getInt("id")
                    val nameCandidato = item.getString("nameCandidato")
                    val lastNameCandidato = item.getString("lastNameCandidato")
                    val fecha = item.getString("fecha")
                    val hora = item.getString("hora")
                    val reclutador = item.getString("reclutador")
                    val direcction = item.getString("direcction")
                    val observatios = item.getString("observatios")
                    val status = item.getString("status")

                    list.add(i, Entrevista(
                        entrevistaId = entrevistaId,
                        nameCandidato = nameCandidato,
                        lastNameCandidato = lastNameCandidato,
                        fecha = fecha,
                        hora = hora,
                        reclutador = reclutador,
                        direcction = direcction,
                        observatios = observatios,
                        status = status
                    ))
                }
                cont.resume(list)
            },
            {
                cont.resumeWithException(it)
                Log.e("NetworkServiceAdapter", "Error en la solicitud", it)
            })
        )
    }

    

    private fun getRequest(path:String, responseListener: Response.Listener<String>, errorListener: Response.ErrorListener): StringRequest {
        return StringRequest(Request.Method.GET, BASE_URL +path, responseListener,errorListener)
    }
    private fun postRequest(path: String, body: JSONObject,  responseListener: Response.Listener<JSONObject>, errorListener: Response.ErrorListener ):JsonObjectRequest{
        return  JsonObjectRequest(Request.Method.POST, BASE_URL +path, body, responseListener, errorListener)
    }

    private fun patchRequest(path: String, body: JSONObject, responseListener: Response.Listener<JSONObject>, errorListener: Response.ErrorListener): JsonObjectRequest {
        return JsonObjectRequest(Request.Method.PATCH, BASE_URL + path, body, responseListener, errorListener)
    }

    private fun putRequest(path: String, body: JSONObject,  responseListener: Response.Listener<JSONObject>, errorListener: Response.ErrorListener ):JsonObjectRequest{
        return  JsonObjectRequest(Request.Method.PUT, BASE_URL +path, body, responseListener, errorListener)
    }
}