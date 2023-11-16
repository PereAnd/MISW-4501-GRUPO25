import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { Ubicacion } from 'src/app/companies/models/empresas';
import { UbicacionesService } from 'src/app/companies/services/ubicaciones.service';
import { DataService } from 'src/app/shared/services/data.service';

@Component({
  selector: 'app-create-ubicacion',
  templateUrl: './create-ubicacion.component.html',
  styleUrls: ['./create-ubicacion.component.css']
})
export class CreateUbicacionComponent {
  indexUbicacion: number;
  empresaId: number;
  countrySelected: string = '';
  citiesOfCountry: string[] = [];
  countryAndCity = [{pais: '', ciudades: ['']}];

  formUbicaciones: FormGroup = new FormGroup({
    country: new FormControl('', Validators.required),
    city: new FormControl('', Validators.required),
    description: new FormControl('', Validators.required)
  })

  get country() { return this.formUbicaciones.get('country') }
  get city() { return this.formUbicaciones.get('city') }
  get description() { return this.formUbicaciones.get('description') }

  constructor(
    private ubicacionesService: UbicacionesService,
    private router: Router,
    private route: ActivatedRoute,
    private dataService: DataService
  ) {
    this.empresaId = +localStorage.getItem('empresaId')!;
    dataService.getCountriesAndCities().subscribe({
      next: data => { this.countryAndCity = data }
    });
  }

  ngOnInit(): void {
    this.indexUbicacion = this.route.snapshot.params['idu'];
    if(this.indexUbicacion){
      this.ubicacionesService.findUbicacion(this.empresaId, this.indexUbicacion)
      .subscribe({
        next: data => {
          this.formUbicaciones.setValue({
            country: data.country,
            description: data.description,
            city: data.city,
          })
          this.countryAndCity.forEach(item => {
            if(item.pais === data.country){
              this.countrySelected = item.pais;
              this.citiesOfCountry = [data.city, ... item.ciudades.filter(city => city !== data.city)];
            }
          })
        },
        error: error => console.error('Error obteniendo la ubicación seleccionada', error),
      })
    }
  }

  registrarUbicacion(){
    const newUbicacion = new Ubicacion(
      this.formUbicaciones.value.country,
      this.formUbicaciones.value.city,
      this.formUbicaciones.value.description,
      this.empresaId
    )
    if(!this.indexUbicacion){
      this.ubicacionesService.addUbicacion(newUbicacion, this.empresaId).subscribe({
          next: data => {
            console.log("Ubicación registrada")
            this.formUbicaciones.reset();
          },
          error: error => {
            console.log("Error registrando la ubicación", error)
            alert('Error registrando la ubicación')
          },
          complete: () => {
            this.router.navigate(['..'], {relativeTo: this.route})
          }
        })
    } else {
      this.ubicacionesService.editUbicacion(newUbicacion, this.indexUbicacion, this.empresaId).subscribe({
        next: data => {
          console.log('Ubicación actualizada')
          this.formUbicaciones.reset()
        },
        error: error => {
          console.log('Error editando la ubicación', error)
          alert('Error editando la ubicación')
        },
        complete: () => {
          this.router.navigate(['..'], {relativeTo: this.route})
        }
      })
    }
  }

  actualizarCiudades(){
    const paisSeleccionado = this.formUbicaciones.value.country;
    this.countryAndCity.forEach(item => {
      if(item.pais === paisSeleccionado){
        this.countrySelected = item.pais;
        this.citiesOfCountry = item.ciudades;
      }
    })
  }

  cancelarCreacion(){
    this.formUbicaciones.reset()
  }
}
