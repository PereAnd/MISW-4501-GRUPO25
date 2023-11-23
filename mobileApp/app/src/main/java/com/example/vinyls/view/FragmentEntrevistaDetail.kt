package com.example.vinyls.view

import android.os.Build
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.annotation.RequiresApi
import androidx.core.net.toUri
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.navArgs
import com.example.vinyls.R
import com.example.vinyls.databinding.FragmentEntrevistaDetailBinding
import com.squareup.picasso.Picasso


class FragmentEntrevistaDetail : Fragment() {

    private var _binding: FragmentEntrevistaDetailBinding? = null
    private val binding get() = _binding!!

    @RequiresApi(Build.VERSION_CODES.O)
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        _binding = FragmentEntrevistaDetailBinding.inflate(inflater, container, false)
        val args: FragmentEntrevistaDetailArgs by navArgs()
        val view = inflater.inflate(R.layout.fragment_entrevista_detail, container, false);
        val tvNameCandidato: TextView = view.findViewById(R.id.tvNameCandidato)
        val tvLastNameCandidato: TextView = view.findViewById(R.id.tvLastNameCandidato)
        val tvFecha: TextView = view.findViewById(R.id.tvFecha)
        val tvHora: TextView = view.findViewById(R.id.tvHora)
        val tvReclutador: TextView = view.findViewById(R.id.tvReclutador)
        val tvDirecction: TextView = view.findViewById(R.id.tvDirecction)
        val tvStatus: TextView = view.findViewById(R.id.tvStatus)
        val tvObservations: TextView = view.findViewById(R.id.tvObservations)



        tvNameCandidato.text = args.nameCandidato
        tvLastNameCandidato.text = args.lastNameCandidato
        tvFecha.text = args.fecha
        tvHora.text = args.hora
        tvReclutador.text = args.reclutador
        tvDirecction.text = args.direcction
        tvStatus.text = args.status
        tvObservations.text = args.observations

       // val imgUrl: String? = args.cover
        //Picasso.get().load(imgUrl).into(ivCover);
        return view
    }


}

