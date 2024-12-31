import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { LeftSideBarComponent } from './left-side-bar/left-side-bar.component';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { WalletsComponent } from './wallets/wallets.component';

// export const routes: Routes = [{ path: '', component: HomeComponent },];
export const routes: Routes = [
    { path: '', component: HomeComponent }, // Route par défaut pour la page d'accueil
    { path: 'login', component: LoginComponent }, 
    {
      path: 'dashboard',
      component: DashboardComponent, // Tableau de bord avec Side Bar
      children: [
        { path: 'wallets', component: WalletsComponent }, // Composant enfant 1 // Composant enfant 2
      ]
    },
  
    { path: 'signup', component: SignupComponent}// Route vers Signup
  ];
