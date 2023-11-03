package com.example.vinyls.models.adapter

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.annotation.LayoutRes
import androidx.databinding.DataBindingUtil
import androidx.recyclerview.widget.RecyclerView
import com.example.vinyls.R
import com.example.vinyls.databinding.InfoacademicaItemBinding
import com.example.vinyls.models.InfoAcademica


class InfoAcademicasAdapter : RecyclerView.Adapter<InfoAcademicasAdapter.InfoAcademicaViewHolder>(){
    var infoAcademicas :List<InfoAcademica> = emptyList()
        set(value) {
            field = value
            notifyDataSetChanged()
        }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): InfoAcademicaViewHolder {
        val withDataBinding: InfoacademicaItemBinding = DataBindingUtil.inflate(
            LayoutInflater.from(parent.context),
            InfoAcademicaViewHolder.LAYOUT,
            parent,
            false)
        return InfoAcademicaViewHolder(withDataBinding)
    }

    override fun onBindViewHolder(holder: InfoAcademicaViewHolder, position: Int) {
        holder.viewDataBinding.also {
            it.infoAcademica = infoAcademicas[position]
        }

    }

    override fun getItemCount(): Int {
        return infoAcademicas.size
    }


    class InfoAcademicaViewHolder(val viewDataBinding: InfoacademicaItemBinding) :
        RecyclerView.ViewHolder(viewDataBinding.root) {
        companion object {
            @LayoutRes
            val LAYOUT = R.layout.infoacademica_item
        }


    }


}