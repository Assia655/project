import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
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
  imports: [RouterOutlet, SignupComponent, HeaderComponent,LeftSideBarComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'my-frontend-app';
}
