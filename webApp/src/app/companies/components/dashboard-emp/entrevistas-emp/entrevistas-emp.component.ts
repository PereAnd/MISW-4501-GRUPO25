import { Component, OnInit, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { faker } from '@faker-js/faker';
import { forkJoin } from 'rxjs';
import { RegCandidatoService } from 'src/app/candidates/services/reg-candidato.service';
import { PerfilesService } from 'src/app/companies/services/perfiles.service';
import { ProyectosService } from 'src/app/companies/services/proyectos.service';

@Component({
  selector: 'app-entrevistas-emp',
  templateUrl: './entrevistas-emp.component.html',
  styleUrls: ['./entrevistas-emp.component.css'],
})
export class EntrevistasEmpComponent implements OnInit {
  empresaId: number;
  proyectos: any[] = [];
  perfiles: any[] = [];
  candidatos: any[] = [];
  aplicaciones: any[] = [];

  responseInterviews: any[] = []
  interviews: any[] = []

  displayedColumns: string[] = ['id', 'project', 'profile', 'candidate', 'enterviewDate', 'done', 'actions']
  dataSource = new MatTableDataSource<any>;

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(
    private perfilesService: PerfilesService,
    private proyectosService: ProyectosService,
    private candidatosService: RegCandidatoService,
    public dialog: MatDialog
  ) {
    this.empresaId = +localStorage.getItem('empresaId')!;
  }

  ngOnInit(): void {
    forkJoin([
      this.candidatosService.getListCandidatos(),
      this.proyectosService.listProyectos(this.empresaId),
      this.perfilesService.listEntrevistas(this.empresaId)
    ]).subscribe({
      next: ([listCandidatos, listProyectos, listEntrevistas]) => {
        this.candidatos = listCandidatos
        this.proyectos = listProyectos
        this.responseInterviews = listEntrevistas

        listProyectos.forEach((proyecto: { id: number; }) => {
          this.perfilesService.listPerfiles(this.empresaId, proyecto.id).subscribe({
            next: listPerfiles => {
              this.perfiles.push(...listPerfiles)

              listPerfiles.forEach((perfil: { id: number; }) => {
                this.perfilesService.listAplicaciones(this.empresaId, proyecto.id, perfil.id).subscribe({
                  next: listAplicaciones => {
                    this.aplicaciones.push(...listAplicaciones)
                  }
                })
              })
            }
          })
        })
      }, complete: () => {
        this.responseInterviews.forEach(entrevista => {
          const application = this.aplicaciones.find(aplicacion => aplicacion.id == entrevista.aplicacionId)
          const candidateId = application.candidatoId;
          const candidate = this.candidatos.find(candidato => candidato.id === candidateId);
          this.interviews.push({
            id: entrevista.id,
            project: application.proyecto,
            profile: application.perfil,
            candidate: candidate.names + ' ' + candidate.lastNames,
            enterviewDate: entrevista.enterviewDate,
            done: entrevista.done ? 'Sí' : 'No'
          })
        })
        this.dataSource = new MatTableDataSource(this.interviews);
        this.dataSource.paginator = this.paginator;
        this.dataSource.sort = this.sort;
      }
    })
  }

  /*

  */

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }
  // detalleProyecto(project: Proyecto){
  //   this.perfilesService.setProjectDetail(project);
  //   const dialogRef = this.dialog.open(DetailProyectoComponent, { width: '1000px' });
  //   dialogRef.afterClosed().subscribe(result => {
  //     //console.log(`Dialog result: ${result}`);
  //   });
  // }

}

