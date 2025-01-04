import { Component, OnInit } from '@angular/core';
import { ApiService } from './api.service';
import { CarbonEmission } from './carbon-emission.model'; // importer l'interface pour les donnees
import { CommonModule } from '@angular/common'; // importer CommonModule
import { HttpClientModule } from '@angular/common/http';
import { ChartData, ChartOptions } from 'chart.js';
import { Chart } from 'angular-highcharts';
import { NgxChartsModule } from '@swimlane/ngx-charts';

@Component({
  selector: 'app-historique',
  standalone: true, // rendre le composant autonome
  templateUrl: './historique.component.html',
  styleUrls: ['./historique.component.css'],
  imports: [CommonModule, HttpClientModule, NgxChartsModule] // ajouter BaseChartDirective pour Chart.js
})
export class HistoriqueComponent implements OnInit {
  carbonEmissions: CarbonEmission[] = []; // tableau pour stocker les emissions de carbone
  single: { name: string, series: { name: string, value: number, strokeWidth?: number }[] }[] = []; // tableau pour les donnees du graphe

  // variables pour stocker la devise et la periode selectionnees
  selectedCurrency: string = 'EUR';  // valeur par defaut 'EUR'
  selectedTime: string = 'all';     // valeur par defaut 'all'

  // options pour le graphe
  chartOptions: any = {
    responsive: true, // responsive pour que le graphe s'adapte a la taille de l'ecran
    legend: true, // afficher la legende
    xAxis: {
      title: 'Date', // titre de l'axe x
      tickFormatting: (value: string) => value.toString(), // formatage des dates
    },
    yAxis: {
      title: 'Prix', // titre de l'axe y
    },
    colorScheme: {
      domain: ['#006600', '#77dd77'],  // couleurs des lignes
    },
    showGridLines: true, // afficher les lignes du quadrillage
  };

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    // recuperation des donnees de l'API
    this.apiService.getCarbonEmissions().subscribe(
      (data) => {
        // inverser l'ordre des donnees a la recuperation
        this.carbonEmissions = data.reverse();
        this.updateChartData(); // mettre a jour les donnees du graphe
      },
      (error) => {
        console.error('Erreur lors de la recuperation des donnees', error); // gestion des erreurs
      }
    );
  }

  // fonction pour mettre a jour les donnees du graphe
  updateChartData(): void {
    // appliquer le filtre par devise (EUR ou ETH)
    const filteredByCurrency = this.filterDataByCurrency(this.selectedCurrency);

    // appliquer le filtre par periode (7 jours ou 30 jours) sur les donnees filtrees par devise
    this.single = [
      {
        name: this.selectedCurrency === 'EUR' ? 'Prix en EUR' : 'Prix en ETH',
        series: this.filterByTimeData(filteredByCurrency),
      }
    ];
  }

  // fonction pour filtrer les donnees par devise (USD ou ETH)
  filterDataByCurrency(currency: string): { name: string, value: number }[] {
    if (currency === 'EUR') {
      // filtrer les donnees par devise USD
      return this.carbonEmissions.map(item => ({
        name: item.date,
        value: item.price !== null ? item.price : 0, // remplacer null par 0
      }));
    } else if (currency === 'ETH') {
      // filtrer les donnees par devise ETH
      return this.carbonEmissions.map(item => ({
        name: item.date,
        value: item.price_eth !== null ? item.price_eth : 0, // remplacer null par 0
      }));
    }
    return []; // retourner un tableau vide si la devise n'est pas reconnue
  }

  // fonction pour filtrer les donnees par periode
  filterByTimeData(data: { name: string, value: number }[]): { name: string, value: number }[] {
    const currentDate = new Date(); // date actuelle
    let filteredData = data; // initialiser les donnees filtrees avec toutes les donnees

    // filtrer les donnees pour les 7 derniers jours
    if (this.selectedTime === '7') {
      const lastWeek = new Date();
      lastWeek.setDate(currentDate.getDate() - 7); // calculer la date de la semaine derniere
      filteredData = filteredData.filter(item => new Date(item.name) >= lastWeek); // filtrer par date
    } 
    // filtrer les donnees pour les 30 derniers jours
    else if (this.selectedTime === '30') {
      const lastMonth = new Date();
      lastMonth.setDate(currentDate.getDate() - 30); // calculer la date du mois dernier
      filteredData = filteredData.filter(item => new Date(item.name) >= lastMonth); // filtrer par date
    }

    return filteredData; // retourner les donnees filtrees
  }

  // fonction pour mettre a jour la devise selectionnee
  filterData(type: string): void {
    this.selectedCurrency = type; // sauvegarder la devise selectionnee
    this.updateChartData(); // mettre a jour les donnees du graphe avec les filtres appliques
  }

  // fonction pour filtrer par periode
  filterByTime(event: Event): void {
    const selectedValue = (event.target as HTMLSelectElement).value; // recuperer la valeur de la periode selectionnee
    this.selectedTime = selectedValue; // sauvegarder la periode selectionnee
    this.updateChartData(); // mettre a jour les donnees du graphe avec les filtres appliques
  }
}
