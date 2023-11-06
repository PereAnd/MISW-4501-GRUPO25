package com.example.vinyls.view

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.View
import android.widget.Button
import androidx.navigation.fragment.findNavController
import com.example.vinyls.R

class FragmentMenuLogin : Fragment(R.layout.fragment_menu_login) {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val buttonEntrevista = requireView().findViewById<Button>(R.id.buttonEntrevista)
        val buttonRegistro = requireView().findViewById<Button>(R.id.buttonRegistro)

        buttonEntrevista.setOnClickListener {
            findNavController().navigate(R.id.action_fragment_menu_login_to_fragment_entrevista)
        }

        buttonRegistro.setOnClickListener {
            findNavController().navigate(R.id.action_fragment_menu_login_to_fragment_registro)
        }
    }


}