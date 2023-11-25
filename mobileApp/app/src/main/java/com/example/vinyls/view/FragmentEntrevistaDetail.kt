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
        val tvFullName: TextView = view.findViewById(R.id.tvFullName)
        val tvApplicationDate: TextView = view.findViewById(R.id.tvApplicationDate)
        val tvStatus: TextView = view.findViewById(R.id.tvStatus)
        val tvEnterviewDate: TextView = view.findViewById(R.id.tvEnterviewDate)
        val tvResult: TextView = view.findViewById(R.id.tvResult)
        val tvFeedback: TextView = view.findViewById(R.id.tvFeedback)


        tvFullName.text = args.fullName
        tvApplicationDate.text = args.applicationDate
        tvStatus.text = args.status
        tvEnterviewDate.text = args.enterviewDate
        tvResult.text = args.result
        tvFeedback.text = args.feedback

       // val imgUrl: String? = args.cover
        //Picasso.get().load(imgUrl).into(ivCover);
        return view
    }


}

