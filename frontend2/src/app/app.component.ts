import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
<<<<<<< HEAD
import { HeaderComponent } from "./header/header.component";
import { SidebarComponent } from "./sidebar/sidebar.component";
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { ApiService } from './services/api.service';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, HeaderComponent,FormsModule,CommonModule,HttpClientModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  providers:[ApiService]
=======
import { HeaderComponent } from './header/header.component';
import { HomeComponent } from "./home/home.component";
import { SponsorsComponent } from './sponsors/sponsors.component';
import { AboutComponent } from './about/about.component';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { LeftSideBarComponent } from './left-side-bar/left-side-bar.component';


@Component({
  selector: 'app-root',
  standalone: true,
  // imports: [RouterOutlet, HeaderComponent, HomeComponent, SponsorsComponent, AboutComponent],
  // imports: [RouterOutlet, LoginComponent, HeaderComponent],
  imports: [RouterOutlet,HeaderComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
>>>>>>> 8a1cd5e9c565bbcc395a5f340cef8368eb332fa1
})
export class AppComponent {
  title = 'my-frontend-app';
}
