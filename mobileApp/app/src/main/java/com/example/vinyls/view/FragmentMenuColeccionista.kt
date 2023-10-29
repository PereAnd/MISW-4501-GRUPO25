package com.example.vinyls.view

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.View
import android.widget.Button
import androidx.navigation.fragment.findNavController
import com.example.vinyls.R

class FragmentMenuColeccionista : Fragment(R.layout.fragment_menu_coleccionista) {
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        val buttonAlbums = requireView().findViewById<Button>(R.id.buttonAlbums)
        val buttonCreateAlbum = requireView().findViewById<Button>(R.id.buttonCreateAlbum)

        buttonAlbums.setOnClickListener {
            findNavController().navigate(R.id.action_fragment_menu_coleccionista_to_fragment_album_list)
        }

        buttonCreateAlbum.setOnClickListener {
            findNavController().navigate(R.id.action_fragment_menu_coleccionista_to_fragment_album_create)
        }
    }


}