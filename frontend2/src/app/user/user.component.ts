import { Component } from '@angular/core';
import { NgModule } from '@angular/core';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { CommonModule } from '@angular/common';
import { SidebarComponent } from '../sidebar/sidebar.component';

@Component({
  selector: 'app-user',  // The selector that you will use to display this component in the parent template
  templateUrl: './user.component.html',  // HTML template for the user component
  styleUrls: ['./user.component.css'],   // Styles for the user component
  imports: [
    CommonModule,
    MatProgressBarModule,
    SidebarComponent
  ],
})
export class UserComponent {
  // Sample user data
  user = {
    profilePicture: 'avatar.jpg',  // Replace with actual user profile picture URL
    name: 'Company 1',
    role: 'Seller',
    location: 'Bay Area, San Francisco, CA',
    email: 'company1@example.com',
    phone: '(123) 456-7890',
    mobile: '(098) 765-4321',
    address: '1234 Main St, San Francisco, CA',
    projects: [
      { name: 'Web Design', progress: 60 },
      { name: 'Website Markup', progress: 50 },
      { name: 'One Page', progress: 30 },
      { name: 'Mobile Template', progress: 20 },
      { name: 'Backend API', progress: 10 }
    ]
  };
}
