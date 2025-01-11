import { Component } from '@angular/core';
import { Router, RouterModule } from '@angular/router';
import { ApiService } from '../services/api.service';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css'],
  imports: [FormsModule, RouterModule, CommonModule],

})
export class SignupComponent {
  username: string = '';  // Add username property
  email: string = '';
  password: string = '';
  confirmPassword: string = '';

  constructor(private apiService: ApiService, private router: Router) {}

  onSignup() {
    if (this.password !== this.confirmPassword) {
      alert('Passwords do not match');
      return;
    }

    // Now you include username, email, and password in the object
    const user = {
      username: this.username,  // Ensure this is included
      email: this.email,
      password: this.password
    };

    this.apiService.signup(user).subscribe({
      next: (response: any) => {
        console.log('Signup successful:', response);
        this.router.navigate(['/login']);  // Redirect after successful signup
      },
      error: (err: any) => {
        console.error('Signup error:', err);
      }
    });
  }
}
