import { Component } from '@angular/core';
import { Router, RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  imports: [RouterModule,FormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  username = ''; // Variable pour stocker le nom d'utilisateur
  password = ''; // Variable pour stocker le mot de passe

  // Données statiques pour la validation
  private staticUser = {
    username: 'admin',
    password: '1234'
  };

  constructor(private router: Router) {}

  onLogin(event: Event) {
    event.preventDefault(); // Empêche le rechargement de la page par le formulaire

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
}
