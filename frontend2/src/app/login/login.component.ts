import { Component } from '@angular/core';
<<<<<<< HEAD
import { Router, RouterModule } from '@angular/router';
import { ApiService } from '../services/api.service';  // Import du ServiceapiService
=======
import { SignupComponent } from '../signup/signup.component';
import { Router, RouterModule } from '@angular/router';
>>>>>>> 8a1cd5e9c565bbcc395a5f340cef8368eb332fa1
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
<<<<<<< HEAD
  imports: [RouterModule, FormsModule],
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
=======
  imports: [RouterModule,FormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
>>>>>>> 8a1cd5e9c565bbcc395a5f340cef8368eb332fa1
})
export class LoginComponent {
  username = ''; // Variable pour stocker le nom d'utilisateur
  password = ''; // Variable pour stocker le mot de passe

<<<<<<< HEAD
  constructor(private router: Router, private apiService: ApiService) {}
=======
  // Données statiques pour la validation
  private staticUser = {
    username: 'admin',
    password: '1234'
  };

  constructor(private router: Router) {}
>>>>>>> 8a1cd5e9c565bbcc395a5f340cef8368eb332fa1

  onLogin(event: Event) {
    event.preventDefault(); // Empêche le rechargement de la page par le formulaire

<<<<<<< HEAD
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

  
=======
    // Debug pour vérifier les valeurs saisies et les valeurs attendues
    console.log('Entered Username:', this.username);
    console.log('Entered Password:', this.password);
    console.log('Expected Username:', this.staticUser.username);
    console.log('Expected Password:', this.staticUser.password);

    // Comparaison entre les valeurs saisies et les données statiques
    if (this.username.trim() === this.staticUser.username && this.password.trim() === this.staticUser.password) {
      alert('Login successful!');
      this.router.navigate(['/dashboard']); // Redirection vers le tableau de bord
    } else {
      alert('Invalid username or password');
    }
  }
>>>>>>> 8a1cd5e9c565bbcc395a5f340cef8368eb332fa1
}
