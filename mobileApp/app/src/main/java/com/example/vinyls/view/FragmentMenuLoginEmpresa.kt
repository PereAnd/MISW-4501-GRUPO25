package com.example.vinyls.view

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.View
import android.widget.Button
import androidx.navigation.fragment.findNavController
import com.example.vinyls.R

class FragmentMenuLoginEmpresa : Fragment(R.layout.fragment_menu_login_empresas) {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val buttonEntrevista = requireView().findViewById<Button>(R.id.buttonEntrevista)


        buttonEntrevista.setOnClickListener {
            findNavController().navigate(R.id.action_fragment_menu_login_to_fragment_entrevista)
        }

    }


}