import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { UserComponent } from './user/user.component';
import { UsersListComponent } from './users-list/users-list.component';
import { UserUpdateComponent } from './user-update/user-update.component'; // Edit user component

export const routes: Routes = [
    { path: '', component: HomeComponent }, // Default route to the homepage
    { path: 'login', component: LoginComponent },
    { path: 'dashboard', component: DashboardComponent },
    { path: 'signup', component: SignupComponent },
    {
        path: 'user', // Path for user profile
        component: UserComponent,
        // children: [
        //   {
        //     path: 'edit', // Edit path for the user profile
        //     component: UserUpdateComponent
        //   }
        // ]
    },
    { path: 'edit', component: UserUpdateComponent},
    { path: 'users_list', component: UsersListComponent },
    // If no match is found, you can redirect to home or login page
    { path: '**', redirectTo: '' } // Wildcard route to catch invalid paths
];
