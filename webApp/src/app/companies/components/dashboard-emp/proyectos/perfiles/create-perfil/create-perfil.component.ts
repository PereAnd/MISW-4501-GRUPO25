import { LiveAnnouncer } from '@angular/cdk/a11y';
import { Component, ElementRef, ViewChild, inject } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';
import { ActivatedRoute, Router } from '@angular/router';
import { Observable, map, startWith } from 'rxjs';
import { Competencia, Perfil } from 'src/app/companies/models/perfil';
import { PerfilesService } from 'src/app/companies/services/perfiles.service';
import { DataService } from 'src/app/shared/services/data.service';
import { CreateCompetenciaComponent } from '../create-competencia/create-competencia.component';

@Component({
  selector: 'app-create-perfil',
  templateUrl: './create-perfil.component.html',
  styleUrls: ['./create-perfil.component.css']
})
export class CreatePerfilComponent {
  indexProyecto: number;
  empresaId: number;
  countrySelected: string = '';
  citiesOfCountry: string[] = [];
  countryAndCity = [{pais: '', ciudades: ['']}];
  conocimientosTemp: Competencia[] = [];
  habilidadesTemp: Competencia[] = [];
  idiomasTemp: Competencia[] = [];

  formPerfiles: FormGroup = new FormGroup({
    name: new FormControl('', Validators.required),
    role: new FormControl('', Validators.required),
    country: new FormControl('', Validators.required),
    city: new FormControl('', Validators.required),
    years: new FormControl('', Validators.required),
    conocimientos: new FormControl(''),
    habilidades: new FormControl(''),
    idiomas: new FormControl(''),
  });

  get name() { return this.formPerfiles.get('name') }
  get role() { return this.formPerfiles.get('role') }
  get country() { return this.formPerfiles.get('country') }
  get city() { return this.formPerfiles.get('city') }
  get years() { return this.formPerfiles.get('years') }
  get conocimientos() { return this.formPerfiles.get('conocimientos') }
  get habilidades() { return this.formPerfiles.get('habilidades') }
  get idiomas() { return this.formPerfiles.get('idiomas') }

  constructor(
    private perfilesService: PerfilesService,
    private router: Router,
    private route: ActivatedRoute,
    private dataService: DataService,
    public dialog: MatDialog
  ) {
    this.empresaId = +localStorage.getItem('empresaId')!;
    dataService.getCountriesAndCities().subscribe({
      next: data => { this.countryAndCity = data }
    });
  }

  ngOnInit(): void {
    this.formPerfiles.setValue({
              name: 'Ingeniero de Software',
              role: 'Desarrollador backend',
              years: 2,
              country: null,
              city: null,
              conocimientos: [],
              habilidades: [],
              idiomas: []
            });
    // this.indexProyecto = this.route.snapshot.params['idp'];
    // if (this.indexProyecto) {
    //   this.perfilesService.addPerfil(this.empresaId, this.indexProyecto).subscribe({
    //     next: (data) => {
    //       this.formProyectos.setValue({
    //         proyecto: data.proyecto,
    //         description: data.description,
    //       });
    //     },
    //     error: (error) =>
    //       console.error('Error obteniendo el proyecto seleccionado', error),
    //   });
    // }
  }

  registrarPerfil() {
    const newPerfil = new Perfil(
      this.formPerfiles.value.name,
      this.formPerfiles.value.role,
      this.formPerfiles.value.location,
      this.formPerfiles.value.years,
      this.formPerfiles.value.conocimientos,
      this.formPerfiles.value.habilidades,
      this.formPerfiles.value.idiomas,
      // Validar cómo enviar todos estos datos, ya que van a diferentes servicios
    );
    this.perfilesService.addPerfilTemp(newPerfil);
    // if (!this.indexProyecto) {
    //   this.perfilesService.addPerfil(this.indexProyecto, this.empresaId, newPerfil).subscribe({
    //     next: (data) => {
    //       console.log('Perfil registrado');
    //       this.formPerfiles.reset();
    //     },
    //     error: (error) => {
    //       console.log('Error registrando el perfil', error);
    //       alert('Error registrando el perfil');
    //     },
    //     complete: () => {
    //       this.router.navigate(['..'], { relativeTo: this.route });
    //     },
    //   });
    // }
    // else {
    //   this.perfilesService
    //     .editProyecto(newProyecto, this.indexProyecto, this.empresaId)
    //     .subscribe({
    //       next: (data) => {
    //         console.log('Proyecto actualizado');
    //         this.formProyectos.reset();
    //       },
    //       error: (error) => {
    //         console.log('Error editando el proyecto', error);
    //         alert('Error editando el proyecto');
    //       },
    //       complete: () => {
    //         this.router.navigate(['..'], { relativeTo: this.route });
    //       },
    //     });
    // }
  }

  actualizarCiudades(){
    const paisSeleccionado = this.formPerfiles.value.country;
    this.countryAndCity.forEach(item => {
      if(item.pais === paisSeleccionado){
        this.countrySelected = item.pais;
        this.citiesOfCountry = item.ciudades;
      }
    })
  }

  addCompetencia(tipo: string){
    const dialogRef = this.dialog.open(CreateCompetenciaComponent, { width: '500px' });
    this.perfilesService.setCompetenciaSelected(tipo);
    dialogRef.afterClosed().subscribe(result => {
      if(result){
        this.perfilesService.getConocimientosTemp().subscribe({ next: data => this.conocimientosTemp = data });
        this.perfilesService.getHabilidadesTemp().subscribe({ next: data => this.habilidadesTemp = data });
        this.perfilesService.getIdiomasTemp().subscribe({ next: data => this.idiomasTemp = data });
      }
    });
  }

  cancelarCreacion() {
    this.formPerfiles.reset();
  }
}
