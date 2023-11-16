import { Component, Input, ViewChild } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { MatTableDataSource } from '@angular/material/table';
import { Perfil } from 'src/app/companies/models/perfil';
import { PerfilesService } from 'src/app/companies/services/perfiles.service';
import { DetailPerfilComponent } from './detail-perfil/detail-perfil.component';
import { CreatePerfilComponent } from './create-perfil/create-perfil.component';

@Component({
  selector: 'app-perfiles',
  templateUrl: './perfiles.component.html',
  styleUrls: ['./perfiles.component.css'],
})
export class PerfilesComponent {
  empresaId: number;
  @Input() proyectoId: number;
  @Input() editMode: boolean = false;

  displayedColumns: string[] = ['id', 'name', 'role', 'location', 'actions'];
  dataSource = new MatTableDataSource<Perfil>();

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(
    private perfilesService: PerfilesService,
    public dialog: MatDialog
  ) {
    this.empresaId = +localStorage.getItem('empresaId')!;
  }

  ngOnInit(): void {
    if (this.proyectoId) {
      this.perfilesService
        .listPerfiles(this.empresaId, this.proyectoId)
        .subscribe({
          next: (data) => {
            this.dataSource = new MatTableDataSource(data);
            return data;
          },
          error: (error) => console.log(error),
          complete: () => {
            this.dataSource.paginator = this.paginator;
            this.dataSource.sort = this.sort;
          },
        });
    }
  }

  applyFilter(event: Event) {
    const filterValue = (event.target as HTMLInputElement).value;
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }

  detallePerfil(profile: Perfil) {
    this.perfilesService.setProfileDetail(profile);
    const dialogRef = this.dialog.open(DetailPerfilComponent, { width: '1000px' });
    dialogRef.afterClosed().subscribe((result) => {
      //console.log(`Dialog result: ${result}`);
    });
  }

  agregarPerfil(perfilNuevo: boolean, perfilId: number = 0) {
    if (!perfilNuevo) { this.perfilesService.setProfileToCompetencies(perfilId) }
    else { this.perfilesService.setProfileToCompetencies(0) }
    const dialogRef = this.dialog.open(CreatePerfilComponent, { width: '1000px' });
    dialogRef.afterClosed().subscribe((result) => {
      if (!result && perfilNuevo && perfilId){
        this.perfilesService.getProfileToCompetencies().subscribe({
          next: data => {
            perfilId = data;
            this.perfilesService.deletePerfil(this.empresaId, this.proyectoId, perfilId).subscribe({
              next: data => {
                console.log('Creación cancelada', data)
                this.ngOnInit()
                this.perfilesService.setProfileToCompetencies(0)
              }, error: error => {
                console.log(error)
              }
            })
          }
        })
      }
      this.perfilesService.listPerfiles(this.empresaId, this.proyectoId).subscribe({
        next: data => {
          this.ngOnInit()
        }
      })
    });
  }
}
