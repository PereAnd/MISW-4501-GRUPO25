import { Component, OnInit, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { faker } from '@faker-js/faker';

@Component({
  selector: 'app-entrevistas-emp',
  templateUrl: './entrevistas-emp.component.html',
  styleUrls: ['./entrevistas-emp.component.css'],
})
export class EntrevistasEmpComponent implements OnInit {
  empresaId: number;

  candidates: any[] = [];
  projects: any[] = [];
  profiles: any[] = [];
  applications: any[] = [];
  interviews: any[] = [];

  displayedColumns: string[] = ['id', 'proyecto', 'perfil', 'candidato', 'fecha', 'estado', 'actions']
  dataSource = new MatTableDataSource<any>;

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(
    public dialog: MatDialog
  ) {
    this.empresaId = +localStorage.getItem('empresaId')!;
  }

  ngOnInit(): void {
    let statusList = ['Pendiente', 'Aceptado', 'Rechazado'];
    for (let i = 0; i < 10; i++){
      this.interviews.push({
        id: i + 1,
        proyecto: faker.science.chemicalElement().name,
        perfil: faker.number.int({ min: 1, max: 10 }),
        candidato: faker.person.firstName() + ' ' + faker.person.lastName(),
        fecha: faker.date.future(),
        estado: statusList[faker.number.int({ min: 0, max: statusList.length - 1 })],
      })
    }
    this.dataSource = new MatTableDataSource(this.interviews);
    this.dataSource.paginator = this.paginator;
    this.dataSource.sort = this.sort;
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }
  // detalleProyecto(project: Proyecto){
  //   this.proyectoService.setProjectDetail(project);
  //   const dialogRef = this.dialog.open(DetailProyectoComponent, { width: '1000px' });
  //   dialogRef.afterClosed().subscribe(result => {
  //     //console.log(`Dialog result: ${result}`);
  //   });
  // }

}

