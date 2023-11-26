import { Component } from '@angular/core';
import { Candidato } from 'src/app/candidates/models/candidato';
import { RegCandidatoService } from 'src/app/candidates/services/reg-candidato.service';

@Component({
  selector: 'app-detail-cand',
  templateUrl: './detail-cand.component.html',
  styleUrls: ['./detail-cand.component.css']
})
export class DetailCandComponent {
  candidatoDetail: Candidato;

  constructor(
    private candidatosService: RegCandidatoService
  ){}

  ngOnInit(): void {
    this.candidatoDetail = this.candidatosService.getCandidateForDetail()
  }
}
