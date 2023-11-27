import { Component } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { Candidato } from 'src/app/candidates/models/candidato';
import { RegCandidatoService } from 'src/app/candidates/services/reg-candidato.service';
import { CreateApplComponent } from '../create-appl/create-appl.component';
import { PerfilesService } from 'src/app/companies/services/perfiles.service';

@Component({
  selector: 'app-detail-cand',
  templateUrl: './detail-cand.component.html',
  styleUrls: ['./detail-cand.component.css']
})
export class DetailCandComponent {
  candidatoDetail: Candidato;
  empresaId: number;
  aplicaciones: number[] = [];

  constructor(
    private candidatosService: RegCandidatoService,
    private perfilesService: PerfilesService,
    public dialog: MatDialog
  ){
    this.empresaId = +localStorage.getItem('empresaId')!;
  }

  ngOnInit(): void {
    this.candidatoDetail = this.candidatosService.getCandidateForDetail()
    this.perfilesService.listAplicacionesEmpresa(this.empresaId).subscribe({
      next: listAplicaciones => {
        listAplicaciones.forEach(aplicacion => {
          this.aplicaciones.push(aplicacion.candidatoId)
        })
      }
    })
  }
  createAplicacion(candidatoId: number){
    // this.candidatosService.setCandidateForDetail(candidate);
    const dialogRef = this.dialog.open(CreateApplComponent, { width: '600' });
    dialogRef.afterClosed().subscribe(result => {
      this.ngOnInit();
    });
  }
}
