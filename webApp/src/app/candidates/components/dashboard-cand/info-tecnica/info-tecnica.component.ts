import { AfterViewInit, Component, OnInit, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Router } from '@angular/router';
import { InfTecnicaService } from 'src/app/candidates/services/inf-tecnica.service';

@Component({
  selector: 'app-info-tecnica',
  templateUrl: './info-tecnica.component.html',
  styleUrls: ['./info-tecnica.component.css']
})
export class InfoTecnicaComponent {
  displayedColumns: string[] = ['id', 'type', 'description', 'actions']
  dataSource = new MatTableDataSource<any>;
  candidatoId: number;

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(
    private infTecnicaService: InfTecnicaService,
    private router: Router
  ) {
    this.candidatoId = this.candidatoId = +localStorage.getItem('candidatoId')!;
  }

  ngOnInit(): void {
    this.infTecnicaService.listInfoTecnica(this.candidatoId)
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

  redirectCreateInfoAcad(){
    this.router.navigate(['candidato/dashboard/'+ this.candidatoId + '/add-info-academica'])
  }
}
