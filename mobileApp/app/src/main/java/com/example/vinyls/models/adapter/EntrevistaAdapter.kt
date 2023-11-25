package com.example.vinyls.models.adapter

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.annotation.LayoutRes
import androidx.core.net.toUri
import androidx.databinding.DataBindingUtil
import androidx.navigation.findNavController
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.bumptech.glide.load.engine.DiskCacheStrategy
import com.bumptech.glide.request.RequestOptions
import com.example.vinyls.R
import com.example.vinyls.databinding.EntrevistaItemBinding
import com.example.vinyls.models.Entrevista
import com.example.vinyls.view.FragmentEntrevistaListDirections



class EntrevistasAdapter : RecyclerView.Adapter<EntrevistasAdapter.EntrevistaViewHolder>(){

    var entrevistas :List<Entrevista> = emptyList()
        set(value) {
            field = value
            notifyDataSetChanged()
        }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): EntrevistaViewHolder {
        val withDataBinding: EntrevistaItemBinding = DataBindingUtil.inflate(
            LayoutInflater.from(parent.context),
            EntrevistaViewHolder.LAYOUT,
            parent,
            false)
        return EntrevistaViewHolder(withDataBinding)
    }

    override fun onBindViewHolder(holder: EntrevistaViewHolder, position: Int) {
        holder.viewDataBinding.also {
            it.entrevista = entrevistas[position]
        }
        holder.bind(entrevistas[position])
        // acceder al detalle de entrevista
        holder.viewDataBinding.root.setOnClickListener {
            val action = FragmentEntrevistaListDirections.actionFragmentEntrevistaListToFragmentEntrevistaDetail(
                entrevistas[position].nameCandidato,
                entrevistas[position].lastNameCandidato,
                entrevistas[position].fecha,
                entrevistas[position].hora,
                entrevistas[position].reclutador,
                entrevistas[position].direcction,
                entrevistas[position].status,
                entrevistas[position].observatios)
            // Navigate using that action
            holder.viewDataBinding.root.findNavController().navigate(action)
        }

    }

    override fun getItemCount(): Int {
        return entrevistas.size
    }


    class EntrevistaViewHolder(val viewDataBinding: EntrevistaItemBinding) :
        RecyclerView.ViewHolder(viewDataBinding.root) {
        companion object {
            @LayoutRes
            val LAYOUT = R.layout.entrevista_item
        }

        fun bind(album: Entrevista) {
            // Glide.with(itemView)
            //   .load(album.cover.toUri().buildUpon().scheme("https").build())
            //.apply(
                    //       RequestOptions()
            //            .placeholder(R.drawable.loading_animation)
            //                .diskCacheStrategy(DiskCacheStrategy.ALL)
            //                  .error(R.drawable.ic_broken_image))
      //          .into(viewDataBinding.imageCover)
        }


    }


}
