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
  empresaId: number;
  proyectoId: number;
  perfilId: number;

  countrySelected: string = '';
  citiesOfCountry: string[] = [];
  countryAndCity = [{pais: '', ciudades: ['']}];

  conocimientos: Competencia[] = [];
  habilidades: Competencia[] = [];
  idiomas: Competencia[] = [];

  formPerfiles: FormGroup = new FormGroup({
    name: new FormControl('', Validators.required),
    role: new FormControl('', Validators.required),
    country: new FormControl('', Validators.required),
    city: new FormControl('', Validators.required),
    years: new FormControl('', Validators.required),
    conocimientos: new FormControl(null),
    habilidades: new FormControl(null),
    idiomas: new FormControl(null),
  });

  get name() { return this.formPerfiles.get('name') }
  get role() { return this.formPerfiles.get('role') }
  get country() { return this.formPerfiles.get('country') }
  get city() { return this.formPerfiles.get('city') }
  get years() { return this.formPerfiles.get('years') }

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
    this.perfilesService.getProjectToProfile().subscribe({ next: data => { this.proyectoId = data } })
    this.perfilesService.getProfileToCompetencies().subscribe({
      next: data => {
        this.perfilId = data;
          if (this.perfilId) {
            this.perfilesService.findPerfil(this.empresaId, this.proyectoId, this.perfilId).subscribe({
              next: (data) => {
                this.formPerfiles.setValue({
                  name: data.name,
                  role: data.role,
                  country: data.location.split(',')[1].trim(),
                  city: data.location.split(',')[0].trim(),
                  years: data.years,
                  conocimientos: null,
                  habilidades: null,
                  idiomas: null
                });
                this.conocimientos = data.conocimientos!;
                this.habilidades = data.habilidades!;
                this.idiomas = data.idiomas!;
                this.countryAndCity.forEach(item => {
                  if(item.pais === data.location.split(',')[1].trim()){
                    this.countrySelected = item.pais;
                    this.citiesOfCountry = [data.location.split(',')[0].trim(), ... item.ciudades.filter(city => city !== data.location.split(',')[0].trim())];
                  }
                })
              },
              error: (error) =>
                console.error('Error obteniendo el proyecto seleccionado', error),
            });
          }
      }
     })

  }

  registrarPerfil() {
    const newPerfil = new Perfil(
      this.formPerfiles.value.name,
      this.formPerfiles.value.role,
      this.formPerfiles.value.city + ', ' + this.formPerfiles.value.country,
      this.formPerfiles.value.years
      // Validar cómo enviar todos estos datos, ya que van a diferentes servicios
    );
    this.perfilesService.addPerfil(this.proyectoId, this.empresaId, newPerfil).subscribe({
      next: (data) => {
        console.log('Perfil registrado');
        this.perfilId = data.id!;
        this.perfilesService.setProfileToCompetencies(data.id!);
      },
      error: (error) => {
        console.log('Error registrando el perfil', error);
        alert('Error registrando el perfil');
      }
    });

    // if (!this.proyectoId) {
    //   this.perfilesService.addPerfil(this.proyectoId, this.empresaId, newPerfil).subscribe({
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
    //     .editProyecto(newProyecto, this.proyectoId, this.empresaId)
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
        if (tipo == 'Conocimiento') this.perfilesService.getConocimientos(this.empresaId, this.proyectoId, this.perfilId).subscribe({ next: data => this.conocimientos = data });
        else if (tipo == 'Habilidad') this.perfilesService.getHabilidades(this.empresaId, this.proyectoId, this.perfilId).subscribe({ next: data => this.habilidades = data });
        else if (tipo == 'Idioma') this.perfilesService.getIdiomas(this.empresaId, this.proyectoId, this.perfilId).subscribe({ next: data => this.idiomas = data });
      }
    });
  }
  cancelarCreacion() {
    this.formPerfiles.reset();
    this.router.navigate(['..'], { relativeTo: this.route });
  }
}
