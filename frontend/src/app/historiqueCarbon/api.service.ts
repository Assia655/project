import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { CarbonEmission } from './carbon-emission.model';



@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private apiUrl = 'http://localhost:8000/carbon_emissions';  // URL de votre API FastAPI

  constructor(private http: HttpClient) { }

  // Fonction pour récupérer les données des émissions de carbone
  getCarbonEmissions(): Observable<CarbonEmission[]> {
    return this.http.get<CarbonEmission[]>(this.apiUrl);
  }

  getData(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

}
