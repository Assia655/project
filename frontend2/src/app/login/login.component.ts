import { Component } from '@angular/core';
import { Router, RouterModule } from '@angular/router';
import { ApiService } from '../services/api.service';  // Import du ServiceapiService
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [RouterModule, FormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  username = ''; // Variable pour stocker le nom d'utilisateur
  password = ''; // Variable pour stocker le mot de passe

  constructor(private router: Router, private apiService: ApiService) {}

  onLogin(event: Event) {
    event.preventDefault(); // Empêche le rechargement de la page par le formulaire

    // Debug pour vérifier les valeurs saisies
    console.log('Entered Username:', this.username);
    console.log('Entered Password:', this.password);

    // Appel au ServiceapiService pour la logique d'authentification via API
    this.apiService.login(this.username, this.password).subscribe(
      (response: { access_token: string, user_id: number }) => {  // Changer string en number
        if (response.access_token) {
          localStorage.setItem('access_token', response.access_token);
          localStorage.setItem('user_id', response.user_id.toString());  // Assurez-vous de convertir le user_id en string si nécessaire
          console.log('User ID stored in localStorage:', response.user_id); // Log pour vérifier
          this.router.navigate(['/dashboard']);
        } else {
          alert('Invalid credentials from API');
        }
      },
      (error: any) => {
        console.error('Error during API login:', error);
        alert('Error during login');
      }
    );
    
  }

  
}
