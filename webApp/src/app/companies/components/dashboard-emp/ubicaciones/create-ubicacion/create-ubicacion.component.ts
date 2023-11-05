import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { Ubicacion } from 'src/app/companies/models/ubicacion';
import { UbicacionesService } from 'src/app/companies/services/ubicaciones.service';

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

  formUbicaciones: FormGroup = new FormGroup({
    country: new FormControl('', Validators.required),
    city: new FormControl('', Validators.required),
    description: new FormControl('', Validators.required)
  })

  countryAndCity = [
    { pais: "Argentina", ciudades: ["Buenos Aires", "Córdoba", "Rosario", "Mendoza", "Mar del Plata"] },
    { pais: "Brasil", ciudades: ["Río de Janeiro", "São Paulo", "Brasilia", "Salvador", "Recife"] },
    { pais: "Canadá", ciudades: ["Toronto", "Montreal", "Vancouver", "Ottawa", "Calgary"] },
    { pais: "China", ciudades: ["Pekín", "Shanghái", "Hong Kong", "Guangzhou", "Xi'an"] },
    { pais: "Colombia", ciudades: ["Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena", "Bucaramanga", "Pereira", "Manizales", "Cúcuta", "Santa Marta"] },
    { pais: "España", ciudades: ["Madrid", "Barcelona", "Sevilla", "Valencia", "Málaga"] },
    { pais: "Francia", ciudades: ["París", "Marsella", "Lyon", "Niza", "Toulouse"] },
    { pais: "Italia", ciudades: ["Roma", "Milán", "Florencia", "Venecia", "Nápoles"] },
    { pais: "Japón", ciudades: ["Tokio", "Kioto", "Osaka", "Hiroshima", "Nara"] },
    { pais: "México", ciudades: ["Ciudad de México", "Cancún", "Guadalajara", "Monterrey", "Puebla"] },
    { pais: "Reino Unido", ciudades: ["Londres", "Mánchester", "Edimburgo", "Birmingham", "Liverpool"] },
    { pais: "Rusia", ciudades: ["Moscú", "San Petersburgo", "Novosibirsk", "Ekaterimburgo", "Kazán"] },
    { pais: "Estados Unidos", ciudades: ["Nueva York", "Los Ángeles", "Chicago", "Miami", "San Francisco"] },
  ];

  get country() { return this.formUbicaciones.get('country') }
  get city() { return this.formUbicaciones.get('city') }
  get description() { return this.formUbicaciones.get('description') }

  constructor(
    private ubicacionesService: UbicacionesService,
    private router: Router,
    private route: ActivatedRoute
  ) {
    this.empresaId = +localStorage.getItem('empresaId')!;
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
    const pais = this.countryAndCity.find(item => item.pais === paisSeleccionado);
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
