import { AfterViewInit, Component, OnInit, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { ListInfoAcademicaService } from 'src/app/candidates/services/list-info-academica.service';
@Component({
  selector: 'app-list-info-acad',
  templateUrl: './list-info-acad.component.html',
  styleUrls: ['./list-info-acad.component.css']
})
export class ListInfoAcadComponent implements OnInit{
  displayedColumns: string[] = ['id', 'tittle', 'institution', 'beginDate', 'endDate', 'studyType']
  dataSource = new MatTableDataSource<any>;

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(
    private listInfoAcademicaService: ListInfoAcademicaService
  ) { }

  ngOnInit(): void {
    this.listInfoAcademicaService.listInfoAcademica(1)
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
