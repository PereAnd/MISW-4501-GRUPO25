import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  countryAndCity: any;

  constructor(
    private httpClient: HttpClient
  ) {
    this.countryAndCity = [
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
  }

  getCountriesAndCities(): Observable<any>{
    return new Observable( observer => {
      observer.next(this.countryAndCity)
    })
  }
}
