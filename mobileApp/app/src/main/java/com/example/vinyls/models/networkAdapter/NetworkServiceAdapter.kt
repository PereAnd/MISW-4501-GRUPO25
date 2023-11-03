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
import org.json.JSONArray
import org.json.JSONObject
import kotlin.coroutines.resume
import kotlin.coroutines.resumeWithException
import kotlin.coroutines.suspendCoroutine

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

                    // Verificar si la clave "password" está presente en el objeto JSON
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
    suspend fun registro(body: JSONObject) = suspendCoroutine<Candidato> { cont ->
        requestQueue.add(postRequest("candidato", body,
            { response ->
                val candidatoId = response.getInt("id")
                val names = response.getString("names")
                val lastNames = response.getString("lastNames")
                val mail = response.getString("mail")
                val password = response.optString("password", "Sin password") // Usar optString para proporcionar un valor predeterminado
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
    suspend fun agregarInfoAcademica(body: JSONObject) = suspendCoroutine<InfoAcademica> { cont ->
        requestQueue.add(postRequest("candidato/1/informacionAcademica", body,
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


    private fun getRequest(path:String, responseListener: Response.Listener<String>, errorListener: Response.ErrorListener): StringRequest {
        return StringRequest(Request.Method.GET, BASE_URL +path, responseListener,errorListener)
    }
    private fun postRequest(path: String, body: JSONObject,  responseListener: Response.Listener<JSONObject>, errorListener: Response.ErrorListener ):JsonObjectRequest{
        return  JsonObjectRequest(Request.Method.POST, BASE_URL +path, body, responseListener, errorListener)
    }
    private fun putRequest(path: String, body: JSONObject,  responseListener: Response.Listener<JSONObject>, errorListener: Response.ErrorListener ):JsonObjectRequest{
        return  JsonObjectRequest(Request.Method.PUT, BASE_URL +path, body, responseListener, errorListener)
    }
}