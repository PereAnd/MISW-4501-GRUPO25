import { Component, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Router } from '@angular/router';
import { InfTecnicaService } from 'src/app/candidates/services/inf-tecnica.service';
import { UbicacionesService } from 'src/app/companies/services/ubicaciones.service';

@Component({
  selector: 'app-ubicaciones',
  templateUrl: './ubicaciones.component.html',
  styleUrls: ['./ubicaciones.component.css']
})
export class UbicacionesComponent {
  empresaId: number = 1;
  displayedColumns: string[] = ['id', 'country', 'city', 'description', 'actions']
  dataSource = new MatTableDataSource<any>;

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(
    private ubicacionService: UbicacionesService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.ubicacionService.listUbicaciones(this.empresaId)
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
}
