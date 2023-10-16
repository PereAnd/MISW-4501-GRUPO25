package com.uniandes.smartfeedmobile

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View

class LoginActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)
    }

    fun goToRegister(view: View?) {
        val intent = Intent(this, InformacionPersonalActivity::class.java)
        startActivity(intent)
    }

    fun goToEnterview(view: View?) {
        val intent = Intent(this, EntrevistaActivity::class.java)
        startActivity(intent)
    }
}