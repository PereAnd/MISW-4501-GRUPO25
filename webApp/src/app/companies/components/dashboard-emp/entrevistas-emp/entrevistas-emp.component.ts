import { Component, OnInit, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { faker } from '@faker-js/faker';
import { Observable, forkJoin } from 'rxjs';
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
  candidatos: any[] = [];
  proyectos: any[] = [];
  perfiles: any[] = [];
  responseApplications: any[] = []

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
      this.perfilesService.listAplicacionesEmpresa(this.empresaId)
    ]).subscribe({
      next: ([listCandidatos, listProyectos, listAplicaciones]) => {
        this.candidatos.push(...listCandidatos)
        this.proyectos.push(...listProyectos)
        this.responseApplications.push(...listAplicaciones)

        const requests: Observable<any>[] = this.proyectos.map( proyecto =>
          this.perfilesService.listPerfiles(this.empresaId, proyecto.id)
        );

        forkJoin(requests).subscribe({
          next: (responses) => {
            this.perfiles.push(...responses.flat());

            this.responseApplications.forEach(responseApplicacion => {
              let candidate = this.candidatos.find(candidato => candidato.id === responseApplicacion.candidatoId)
              let project = this.proyectos.find(proyecto => proyecto.id === responseApplicacion.proyectoId)
              let profile = this.perfiles.find(perfil => perfil.id === responseApplicacion.perfilId)
              let enterviewDate = responseApplicacion.entrevistas[0] ? responseApplicacion.entrevistas[0].enterviewDate : 'No programada'
              let status = responseApplicacion.status
              let done = responseApplicacion.entrevistas[0] ? responseApplicacion.entrevistas[0].done : false
              this.interviews.push({
                id: responseApplicacion.id,
                project: project.proyecto,
                profile: profile.name,
                candidate: candidate.names + ' ' + candidate.lastNames,
                enterviewDate: enterviewDate,
                done: done ? 'Sí - ' + status : 'No - ' + status,
              })
            })
            this.dataSource = new MatTableDataSource(this.interviews);
            this.dataSource.paginator = this.paginator;
            this.dataSource.sort = this.sort;
          }
        })


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

