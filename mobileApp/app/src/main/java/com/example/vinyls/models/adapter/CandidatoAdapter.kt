package com.example.vinyls.models.adapter

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.annotation.LayoutRes
//import androidx.core.net.toUri
import androidx.databinding.DataBindingUtil
//import androidx.navigation.findNavController
import androidx.recyclerview.widget.RecyclerView
//import com.bumptech.glide.Glide
//import com.bumptech.glide.load.engine.DiskCacheStrategy
//import com.bumptech.glide.request.RequestOptions
import com.example.vinyls.R
import com.example.vinyls.databinding.CandidatoItemBinding
import com.example.vinyls.models.Candidato


class CandidatosAdapter : RecyclerView.Adapter<CandidatosAdapter.CandidatoViewHolder>(){
    var candidatos :List<Candidato> = emptyList()
        set(value) {
            field = value
            notifyDataSetChanged()
        }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CandidatoViewHolder {
        val withDataBinding: CandidatoItemBinding = DataBindingUtil.inflate(
            LayoutInflater.from(parent.context),
            CandidatoViewHolder.LAYOUT,
            parent,
            false)
        return CandidatoViewHolder(withDataBinding)
    }

    override fun onBindViewHolder(holder: CandidatoViewHolder, position: Int) {
        holder.viewDataBinding.also {
            it.candidato = candidatos[position]
        }

    }

    override fun getItemCount(): Int {
        return candidatos.size
    }


    class CandidatoViewHolder(val viewDataBinding: CandidatoItemBinding) :
        RecyclerView.ViewHolder(viewDataBinding.root) {
        companion object {
            @LayoutRes
            val LAYOUT = R.layout.candidato_item
        }


    }


}