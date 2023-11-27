import { DatePipe } from '@angular/common';
import { Component, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { forkJoin } from 'rxjs';
import { RegCandidatoService } from 'src/app/candidates/services/reg-candidato.service';
import { ProyectosService } from 'src/app/companies/services/proyectos.service';
import { RegEmpresaService } from 'src/app/companies/services/reg-empresa.service';
import { CreateEntrevistaComponent } from './create-entrevista/create-entrevista.component';
import { PerfilesService } from 'src/app/companies/services/perfiles.service';

@Component({
  selector: 'app-entrevistas-abc',
  templateUrl: './entrevistas-abc.component.html',
  styleUrls: ['./entrevistas-abc.component.css']
})
export class EntrevistasAbcComponent {
  empresaId: number;
  candidatos: any[] = [];
  proyectos: any[] = [];
  perfiles: any[] = [];
  empresas: any[] = [];
  responseApplications: any[] = []
  interviews: any[] = []

  displayedColumns: string[] = ['id', 'company', 'project', 'candidate', 'enterviewDate', 'done', 'actions']
  dataSource = new MatTableDataSource<any>;

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(
    private proyectosService: ProyectosService,
    private candidatosService: RegCandidatoService,
    private empresasService: RegEmpresaService,
    private perfilesService: PerfilesService,
    private datePipe: DatePipe,
    public dialog: MatDialog
  ) { }

  ngOnInit(): void {
    this.interviews = []
    this.candidatos = []
    this.empresas = []
    this.proyectos = []
    this.responseApplications = []
    forkJoin([
      this.candidatosService.getListCandidatos(),
      this.empresasService.getListEmpresas()
    ]).subscribe({
      next: ([listCandidatos, listEmpresas]) => {
        this.candidatos.push(...listCandidatos);
        this.empresas.push(...listEmpresas);

        const proyectosObservables = this.empresas.map(empresa => this.proyectosService.listProyectos(empresa.id!));
        const aplicacionesObservables = this.candidatos.map(candidato => this.candidatosService.getListApplications(candidato.id!));

        forkJoin(proyectosObservables).subscribe({
          next: (listProyectos) => {
            listProyectos.forEach((proyectos: any) => this.proyectos.push(...proyectos))
          }
        })
        forkJoin(aplicacionesObservables).subscribe({
          next: (listApplications) => {
            this.interviews = []
            listApplications.forEach((applications: any) => this.responseApplications.push(...applications))
            this.responseApplications.forEach(responseApplicacion => {
              let company = this.empresas.find(empresa => empresa.id === responseApplicacion.empresaId)
              let candidate = this.candidatos.find(candidato => candidato.id === responseApplicacion.candidatoId)
              let project = this.proyectos.find(proyecto => proyecto.id === responseApplicacion.proyectoId)
              let enterviewDate;
              if (responseApplicacion.entrevistas.length === 0) { enterviewDate = 'No programada'}
              else { enterviewDate = this.datePipe.transform(responseApplicacion.entrevistas[0].enterviewDate, 'dd-MMM-yyyy HH:mm') }
              let done = responseApplicacion.entrevistas[0] ? responseApplicacion.entrevistas[0].done : false
              this.interviews.push({
                id: responseApplicacion.id,
                company: company.name,
                project: project.proyecto,
                candidate: candidate.names + ' ' + candidate.lastNames,
                enterviewDate: enterviewDate,
                done: done ? 'Si - ' + responseApplicacion.status : 'No - ' + responseApplicacion.status
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
  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }
  registrarEntrevista(element: any){
    let appl = this.responseApplications.find(application => application.id === element.id)
    this.proyectosService.setApplToInterview(appl)
    const dialogRef = this.dialog.open(CreateEntrevistaComponent, { width: '700px' });
    dialogRef.afterClosed().subscribe(result => {
      if(result) this.ngOnInit()
    });
  }
  // detalleProyecto(project: Proyecto){
  //   this.perfilesService.setProjectDetail(project);
  //   const dialogRef = this.dialog.open(DetailProyectoComponent, { width: '1000px' });
  //   dialogRef.afterClosed().subscribe(result => {
  //     //console.log(`Dialog result: ${result}`);
  //   });
  // }
}
