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


    suspend fun getCandidatos() = suspendCoroutine<List<Candidato>>{ cont ->
        requestQueue.add(getRequest("candidato",
            { response ->
                val resp = JSONArray(response)
                val list = mutableListOf<Candidato>()
                var item:JSONObject? = null
                for (i in 0 until resp.length()) {
                    item = resp.getJSONObject(i)
                    list.add(i, Candidato(candidatoId = item.getInt("id"),
                        names = item.getString("names"),
                        lastNames = item.getString("lastNames"),
                        password = item.getString("password"),
                        confirmPassword = item.getString("confirmPassword"),
                        mail = item.getString("mail"))
                    )
                }
                cont.resume(list)
            },
            {
                cont.resumeWithException(it)
            }))
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