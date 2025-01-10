import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HTTP_INTERCEPTORS, HttpClient, HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { CommonModule } from '@angular/common';
import { MatCardModule } from '@angular/material/card';
import { DashboardComponent } from './dashboard/dashboard.component';
import { RouterModule } from '@angular/router';
import { routes } from './app.routes';
import { LoginComponent } from './login/login.component';
// import {  FormsModule, ReactiveFormsModule } from '@angular/forms';  // Import FormsModule
import { SignupComponent } from './signup/signup.component';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { ApiService } from './services/api.service';
import { SidebarComponent } from './sidebar/sidebar.component';
// import { Api2Service } from './services/api2.service';

@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    LoginComponent,
    SignupComponent,
    SidebarComponent
  ],
  imports: [
    BrowserModule,
    CommonModule,
    HttpClientModule,
    MatCardModule,
    ReactiveFormsModule,
    RouterModule.forRoot(routes),
    FormsModule,
    RouterModule

  ],
  exports: [],
  providers: [ ApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
