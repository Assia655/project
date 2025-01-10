import { Component } from '@angular/core';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { NgxPaginationModule } from 'ngx-pagination';
import { SidebarComponent } from "../sidebar/sidebar.component";  // Import ngx-pagination

@Component({
  selector: 'app-users-list',
  imports: [
    CommonModule,
    NgxPaginationModule,
    SidebarComponent
],
  templateUrl: './users-list.component.html',
  styleUrl: './users-list.component.css',
  standalone: true
})
export class UsersListComponent {
  p: number = 1;  // Current page number
  itemsPerPage: number = 5;  // Set the number of items per page
  users = [
    {
      logo: 'https://via.placeholder.com/40',
      companyName: 'Company1',
      email: 'company1@example.com',
      role: 'Customer'
    },
    {
      logo: 'https://via.placeholder.com/40',
      companyName: 'Company2',
      email: 'company2@example.com',
      role: 'Seller'
    },
    {
      logo: 'https://via.placeholder.com/40',
      companyName: 'Company3',
      email: 'company3@example.com',
      role: 'Customer'
    },
    {
      logo: 'https://via.placeholder.com/40',
      companyName: 'Company4',
      email: 'company4@example.com',
      role: 'Seller'
    },
    {
      logo: 'https://via.placeholder.com/40',
      companyName: 'Company5',
      email: 'company5@example.com',
      role: 'Customer'
    },
    {
      logo: 'https://via.placeholder.com/40',
      companyName: 'Company6',
      email: 'company6@example.com',
      role: 'Seller'
    }
  ];
}
