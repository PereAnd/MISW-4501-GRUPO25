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
import com.example.vinyls.databinding.FragmentCandidatoListBinding
import com.example.vinyls.models.Candidato
import com.example.vinyls.models.adapter.CandidatoAdapter
import com.example.vinyls.viewmodels.CandidatoListViewModel

class FragmentCandidatoList : Fragment() {

    private var _binding: FragmentCandidatoListBinding? = null
    private val binding get() = _binding!! // get
    private lateinit var recyclerView: RecyclerView // almacena datos
    private lateinit var viewModel: CandidatoListViewModel // interfaz
    private var viewModelAdapter: CandidatoAdapter? = null // llenar los datos
    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?):
            View? {
                _binding = FragmentCandidatoListBinding.inflate(inflater, container, false)
                val view = binding.root
                viewModelAdapter = CandidatoAdapter()
                return view
            }
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        recyclerView = binding.candidatosRv
        recyclerView.layoutManager = LinearLayoutManager(context)
        recyclerView.adapter = viewModelAdapter
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)
        val activity = requireNotNull(this.activity) {
            "You can only access the viewModel after onActivityCreated()"
        }
        viewModel = ViewModelProvider(this, CandidatoListViewModel.Factory(activity.application)).get(
            CandidatoListViewModel::class.java
        )
        viewModel.candidatos.observe(viewLifecycleOwner, Observer<List<Candidato>> {
            it.apply {
                viewModelAdapter!!.candidatos = this
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