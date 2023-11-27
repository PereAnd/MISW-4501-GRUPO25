import { Component, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { RegCandidatoService } from 'src/app/candidates/services/reg-candidato.service';
import { DetailCandComponent } from './detail-cand/detail-cand.component';
import { Candidato } from 'src/app/candidates/models/candidato';

@Component({
  selector: 'app-busqueda-cand',
  templateUrl: './busqueda-cand.component.html',
  styleUrls: ['./busqueda-cand.component.css']
})
export class BusquedaCandComponent {
  empresaId: number;
  displayedColumns: string[] = ['id', 'nombre', 'palabrasClave', 'actions']
  dataSource = new MatTableDataSource<any>;
  candidatos: any[] = [];

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(
    private candidatosService: RegCandidatoService,
    public dialog: MatDialog
  ) {
    this.empresaId = +localStorage.getItem('empresaId')!;
  }

  ngOnInit(): void {
    this.candidatosService.getListCandidatos()
    .subscribe({
      next: data => {
        data.forEach(candidato => {
          let nombre = `${candidato.names} ${candidato.lastNames}`;
          let palabrasClave = '';
          candidato.informacionTecnica!.forEach(infoTecnica => {
            palabrasClave += `${infoTecnica.description}, `;
          })
          candidato.informacionAcademica!.forEach(infoAcademica => {
            palabrasClave += `${infoAcademica.studyType} en ${infoAcademica.title}, `;
          })
          let newCandidato = {...candidato, nombre: nombre, palabrasClave: palabrasClave};
          this.candidatos.push(newCandidato);
        })
        this.dataSource = new MatTableDataSource(this.candidatos);
        return data;
      },
      error: error => console.log(error),
      complete: () => {
        this.dataSource.paginator = this.paginator;
        this.dataSource.sort = this.sort;
      }
    })
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }

  detalleCandidato(candidate: Candidato){
    this.candidatosService.setCandidateForDetail(candidate);
    const dialogRef = this.dialog.open(DetailCandComponent, { width: '1000px' });
    dialogRef.afterClosed().subscribe(result => {
      //console.log(`Dialog result: ${result}`);
    });
  }
}
