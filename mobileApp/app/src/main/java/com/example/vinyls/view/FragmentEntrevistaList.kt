package com.example.vinyls.view

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.vinyls.databinding.FragmentEntrevistaListBinding
import com.example.vinyls.models.Entrevista
import com.example.vinyls.models.adapter.EntrevistasAdapter
import com.example.vinyls.viewmodels.EntrevistaListViewModel

class FragmentEntrevistaList : Fragment() {

    private var _binding: FragmentEntrevistaListBinding? = null
    private val binding get() = _binding!! // get
    private lateinit var recyclerView: RecyclerView // almacena datos
    private lateinit var viewModel: EntrevistaListViewModel // interfaz
    private var viewModelAdapter: EntrevistasAdapter? = null // llenar los datos
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?):
            View? {
                _binding = FragmentEntrevistaListBinding.inflate(inflater, container, false)
                val view = binding.root
                viewModelAdapter = EntrevistasAdapter()
                return view
            }
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        recyclerView = binding.entrevistasRv
        recyclerView.layoutManager = LinearLayoutManager(context)
        recyclerView.adapter = viewModelAdapter
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        val activity = requireNotNull(this.activity) {
            "You can only access the viewModel after onActivityCreated()"
        }
        viewModel = ViewModelProvider(this, EntrevistaListViewModel.Factory(activity.application)).get(
            EntrevistaListViewModel::class.java
        )
        viewModel.entrevistas.observe(viewLifecycleOwner, Observer<List<Entrevista>> {
            it.apply {
                viewModelAdapter!!.entrevistas = this
            }
        })
        viewModel.eventNetworkError.observe(
            viewLifecycleOwner,
            Observer<Boolean> { isNetworkError ->
                if (isNetworkError) onNetworkError()
            })
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }

    private fun onNetworkError() {
        if (!viewModel.isNetworkErrorShown.value!!) {
            Toast.makeText(activity, "Network Error", Toast.LENGTH_LONG).show()
            viewModel.onNetworkErrorShown()
        }
    }
}