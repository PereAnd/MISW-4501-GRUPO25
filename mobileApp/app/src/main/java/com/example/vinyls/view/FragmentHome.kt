package com.example.vinyls.view

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import androidx.navigation.fragment.findNavController
import com.example.vinyls.R


class FragmentHome : Fragment(R.layout.fragment_home) {
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?):
            View? {
                val view = inflater.inflate(R.layout.fragment_home, container, false);
                val buttonMenuColeccionista: Button = view.findViewById(R.id.btnColeccionista)
                val buttonMenuLogin: Button = view.findViewById(R.id.btnLogin)

                buttonMenuColeccionista.setOnClickListener {
                    findNavController().navigate(R.id.action_fragment_home_to_fragment_menu_coleccionista)
                        }

                buttonMenuLogin.setOnClickListener {
                    findNavController().navigate(R.id.action_fragment_home_to_fragment_menu_login)
                        }
                return view
                }

}