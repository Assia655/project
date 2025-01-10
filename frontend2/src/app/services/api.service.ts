import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders ,HttpClientModule} from '@angular/common/http';
import { map, Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private apiUrl = 'http://localhost:8004/token';  // L'URL de votre backend FastAPI

  constructor(private http: HttpClient) { }

  login(username: string, password: string): Observable<{ access_token: string; user_id: number }> {
    const body = new URLSearchParams();
    body.set('username', username);
    body.set('password', password);
  
    const headers = new HttpHeaders().set('Content-Type', 'application/x-www-form-urlencoded');
  
    return this.http.post<{ access_token: string; user_id: number }>(this.apiUrl, body.toString(), { headers });
  }
  
  
  
  getMyTransactions(token: string): Observable<any> {
    const headers = new HttpHeaders().set('Authorization', `Bearer ${token}`);
    return this.http.get('http://localhost:8004/transactions/my', { headers });
  }
  

  private apiUrl_General = 'http://localhost:8004';  // L'URL de votre backend FastAPI

  signup(user: { username: string, email: string, password: string }): Observable<any> {
    return this.http.post('http://localhost:8004/users', user);
  }

  private apiUrl2 = 'http://localhost:8003/transactions';  // Adjust the URL to your API endpoint

  // getTransactions(): Observable<any> {
  //   return this.http.get(this.apiUrl2);
  // }

  getTransactions(userId: number): Observable<any> {
    return this.http.get(`${this.apiUrl2}/${userId}`);  // Appeler l'API avec l'ID de l'utilisateur
  }

  private apiUrl3 = 'http://localhost:8002';  // URL for your FastAPI backend


  // Method to get market prices for EUR and ETH
  getMarketPrices(): Observable<any> {
    return this.http.get<any>(`${this.apiUrl3}/prices`);  // Fetch the prices from the backend
  }
  getPrices(reverse: boolean = false): Observable<any> {
    return this.http.get<any>(`${this.apiUrl3}/prices`).pipe(
      map((response: { dates: any[]; eurPrices: any[]; ethPrices: any[]; }) => {
        if (reverse) {
          response.dates.reverse();
          response.eurPrices.reverse();
          response.ethPrices.reverse();
        }
        return response;
      })
    );
  }

  getWallets(userId: number, currency:String): Observable<any> {
    return this.http.get<any>(`${this.apiUrl_General}/wallets/${userId}/${currency}`);
  }

  private apiUrl4 = 'http://localhost:8003';  // URL for your FastAPI backend

  getActiveAnnouncements(): Observable<any> {
    return this.http.get(`${this.apiUrl4}/announcements`);
  }
  
  



  
}