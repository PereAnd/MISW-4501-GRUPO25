import { AfterViewInit, Component, OnInit, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Router } from '@angular/router';
import { InfAcademicaService } from 'src/app/candidates/services/inf-academica.service';
import { InfLaboralService } from 'src/app/candidates/services/inf-laboral.service';

@Component({
  selector: 'app-info-laboral',
  templateUrl: './info-laboral.component.html',
  styleUrls: ['./info-laboral.component.css']
})
export class InfoLaboralComponent {
  displayedColumns: string[] = ['id', 'organization', 'position', 'activities', 'dateFrom', 'dateTo', 'actions']
  dataSource = new MatTableDataSource<any>;
  candidatoId: number;

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(
    private infLaboralService: InfLaboralService,
    private router: Router
  ) {
    this.candidatoId = this.candidatoId = +localStorage.getItem('candidatoId')!;
  }

  ngOnInit(): void {
    this.infLaboralService.listInfoLaboral(this.candidatoId)
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

  redirectCreateInfoLab(){
    this.router.navigate(['candidato/dashboard/' + this.candidatoId + '/add-info-laboral'])
  }
}
