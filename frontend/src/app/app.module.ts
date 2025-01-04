import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HTTP_INTERCEPTORS, HttpClient, HttpClientModule } from '@angular/common/http';
import { AppComponent } from './app.component';
import { HistoriqueComponent } from './historiqueCarbon/historique.component';
import { CommonModule } from '@angular/common';
import { ApiService } from './historiqueCarbon/api.service';
// import { ChartsModule } from 'ng2-charts'; // Importez ChartsModule
// import { ChartConfiguration, ChartData, ChartType } from 'chart.js';
// import { NgChartsModule } from 'ng2-charts';
import { provideHttpClient, withFetch } from '@angular/common/http'; // avec 'provideHttpClient' et 'withFetch'
// import{ChartModule}from'angular-highcharts';
import { CharttComponent } from './chartt/chartt.component';
import { MatCardModule } from '@angular/material/card';
import { NgxChartsModule } from '@swimlane/ngx-charts';


@NgModule({
  declarations: [
    AppComponent,
    HistoriqueComponent,
    CharttComponent,
    
         
  ],
  imports: [
    BrowserModule,
    CommonModule,
    HttpClientModule,
    MatCardModule,
    NgxChartsModule
    // NgChartsModule,



  ],
  exports: [HistoriqueComponent],

  providers: [ApiService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
