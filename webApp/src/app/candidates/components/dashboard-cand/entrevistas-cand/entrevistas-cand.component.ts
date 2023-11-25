import { Component, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Observable, forkJoin, map, mergeMap, of, switchMap } from 'rxjs';
import { RegCandidatoService } from 'src/app/candidates/services/reg-candidato.service';
import { PerfilesService } from 'src/app/companies/services/perfiles.service';
import { ProyectosService } from 'src/app/companies/services/proyectos.service';
import { RegEmpresaService } from 'src/app/companies/services/reg-empresa.service';

@Component({
  selector: 'app-entrevistas-cand',
  templateUrl: './entrevistas-cand.component.html',
  styleUrls: ['./entrevistas-cand.component.css']
})
export class EntrevistasCandComponent {
  candidatoId: number;
  empresas: any[] = [];
  proyectos: any[] = [];
  perfiles: any[] = [];
  responseApplications: any[] = []

  interviews: any[] = []

  displayedColumns: string[] = ['id', 'company', 'project', 'profile', 'enterviewDate', 'done', 'actions']
  dataSource = new MatTableDataSource<any>;

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(
    private empresasService: RegEmpresaService,
    private perfilesService: PerfilesService,
    private proyectosService: ProyectosService,
    private candidatosService: RegCandidatoService,
    public dialog: MatDialog
  ) {
    this.candidatoId = +localStorage.getItem('candidatoId')!;
  }

  ngOnInit(): void {
    this.obtenerDatos();
  }

  obtenerDatos() {
    this.empresasService.getListEmpresas().pipe(
      switchMap(empresas => {
        this.empresas = empresas;
        const proyectosObservableArray: Observable<any>[] = [];

        // Obtener observables de proyectos para cada empresa
        for (const empresa of empresas) {
          proyectosObservableArray.push(
            this.proyectosService.listProyectos(empresa.id!).pipe(
              map(proyectos => ({ empresa, proyectos }))
            )
          );
        }

        // Combinar observables de proyectos en un único observable
        return forkJoin(proyectosObservableArray);
      }),
      switchMap(resultados => {
        this.proyectos = resultados.reduce((acc, resultado) => [...acc, ...resultado.proyectos], []);
        const perfilesObservableArray: Observable<any>[] = [];

        // Obtener observables de perfiles para cada empresa y proyecto
        for (const { empresa, proyectos } of resultados) {
          for (const proyecto of proyectos) {
            perfilesObservableArray.push(
              this.perfilesService.listPerfiles(empresa.id, proyecto.id).pipe(
                map(perfiles => ({ empresa, proyecto, perfiles }))
              )
            );
          }
        }

        // Combinar observables de perfiles en un único observable
        return forkJoin(perfilesObservableArray);
      })
    ).subscribe(resultados => {
      this.perfiles = resultados.reduce((acc, resultado) => [...acc, ...resultado.perfiles], []);

      // Ahora que tienes las empresas, proyectos y perfiles, puedes realizar otras operaciones
      this.obtenerAplicaciones();
    });
  }

  obtenerAplicaciones() {
    this.candidatosService.getListApplications(this.candidatoId).subscribe(aplicaciones => {
      this.responseApplications = aplicaciones;

      // Asociar aplicaciones con empresas, proyectos y perfiles
      for (const aplicacion of this.responseApplications) {
        const empresa = this.empresas.find(empresa => empresa.id === aplicacion.empresaId);
        const proyecto = this.proyectos.find(proyecto => proyecto.id === aplicacion.proyectoId);
        const perfil = this.perfiles.find(perfil => perfil.id === aplicacion.perfilId);

        this.interviews.push({
          id: aplicacion.id,
          company: empresa.name,
          project: proyecto.proyecto,
          profile: perfil.name,
          enterviewDate: aplicacion.entrevistas[0].enterviewDate,
          done: aplicacion.entrevistas[0].done ? 'Sí' : 'No'
        })
        this.dataSource = new MatTableDataSource(this.interviews);
          this.dataSource.paginator = this.paginator;
          this.dataSource.sort = this.sort;
      }
    });
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }
}

// const empresasObs = this.empresasService.getListEmpresas().subscribe({
    //   next: listEmpresas => {
    //     this.empresas.push(...listEmpresas);
    //     this.empresas.map( empresa =>
    //       this.proyectosService.listProyectos(empresa.id).subscribe(
    //         listProyectos => {
    //           this.proyectos.push(...listProyectos)
    //           listProyectos.map( (proyecto: { id: number; }) =>
    //             this.perfilesService.listPerfiles(empresa.id, proyecto.id).subscribe({
    //               next: listPerfiles => {
    //                 this.perfiles.push(...listPerfiles)
    //               }
    //             })
    //           )
    //         }
    //       )
    //     )
    //   }
    // })
    // forkJoin([
    //   this.candidatosService.getListApplications(this.candidatoId),
    // ]).subscribe({
    //   next: ([listAplicaciones]) => {
    //     console.log(listAplicaciones)
    //     console.log(this.empresas)
    //     console.log(this.proyectos)
    //     console.log(this.perfiles)
    //   }
    // })
