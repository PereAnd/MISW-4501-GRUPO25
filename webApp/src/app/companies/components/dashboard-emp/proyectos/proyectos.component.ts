import { Component, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Router } from '@angular/router';
import { Proyecto } from 'src/app/companies/models/proyectos';
import { ProyectosService } from 'src/app/companies/services/proyectos.service';
import { MatDialogModule, MatDialog } from '@angular/material/dialog';
import { DetailProyectoComponent } from './detail-proyecto/detail-proyecto.component';

@Component({
  selector: 'app-proyectos',
  templateUrl: './proyectos.component.html',
  styleUrls: ['./proyectos.component.css']
})
export class ProyectosComponent {
  empresaId: number;
  displayedColumns: string[] = ['id', 'proyecto', 'description', 'actions']
  dataSource = new MatTableDataSource<any>;

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(
    private proyectoService: ProyectosService,
    public dialog: MatDialog
  ) {
    this.empresaId = +localStorage.getItem('empresaId')!;
  }

  ngOnInit(): void {
    this.proyectoService.listProyectos(this.empresaId)
    .subscribe({
      next: data => {
        this.dataSource = new MatTableDataSource(data);
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
  detalleProyecto(project: Proyecto){
    this.proyectoService.setProjectDetail(project);
    const dialogRef = this.dialog.open(DetailProyectoComponent, { width: '1000px' });
    dialogRef.afterClosed().subscribe(result => {
      //console.log(`Dialog result: ${result}`);
    });
  }
}
