import { Component, OnInit, AfterViewInit } from '@angular/core';
import { Chart, ChartConfiguration } from 'chart.js/auto';
<<<<<<< HEAD
import { ApiService } from '../services/api.service';
import { SidebarComponent } from '../sidebar/sidebar.component';
import { CommonModule } from '@angular/common';
=======
import { SidebarComponent } from '../sidebar/sidebar.component';
>>>>>>> 8a1cd5e9c565bbcc395a5f340cef8368eb332fa1

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css'],
<<<<<<< HEAD
  imports: [SidebarComponent, CommonModule],
  providers: [ApiService]
})
export class DashboardComponent implements OnInit, AfterViewInit {
  dates: string[] = [];
  eurPrices: number[] = [];
  ethPrices: number[] = [];
  
  ethBalance: number = 0; // Balance for ETH wallet
  eurBalance: number = 0; // Balance for USD wallet

  chartData: ChartConfiguration['data'] = {
    labels: [], // Liste des dates
    datasets: [
      {
        label: 'Price in EUR',
        data: [],
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgb(75, 192, 134)',
=======
  imports: [SidebarComponent]
})
export class DashboardComponent implements OnInit, AfterViewInit {
  // Chart.js configuration
  chartData: ChartConfiguration['data'] = {
    labels: [], // Dynamic labels
    datasets: [
      {
        label: 'Carbon Price in USD',
        data: [], // Dynamic data
        backgroundColor: 'rgba(75, 192, 192, 0.2)', // Fill color
        borderColor: 'rgb(75, 192, 134)', // Line color
>>>>>>> 8a1cd5e9c565bbcc395a5f340cef8368eb332fa1
        borderWidth: 2,
        tension: 0.4
      },
      {
<<<<<<< HEAD
        label: 'Price in ETH',
        data: [],
=======
        label: 'Carbon Price in ETH',
        data: [], // Dynamic data
>>>>>>> 8a1cd5e9c565bbcc395a5f340cef8368eb332fa1
        backgroundColor: 'rgba(153, 102, 255, 0.2)',
        borderColor: 'rgb(45, 87, 56)',
        borderWidth: 2,
        tension: 0.4
      }
    ]
  };

  chartOptions: ChartConfiguration['options'] = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: true,
        position: 'top'
      },
      tooltip: {
        enabled: true
      }
    },
    scales: {
      x: {
        title: {
          display: true,
          text: 'Time'
        }
      },
      y: {
        title: {
          display: true,
          text: 'Price'
        }
      }
    }
  };

  chartInstance!: Chart;
<<<<<<< HEAD
  
  activeAnnouncements: { id: number; credit_amount: Number; created_at: Date; }[] = [];

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.fetchActiveAnnouncements(); // Appel pour récupérer les annonces actives

    // Fetch market prices for chart
    this.apiService.getMarketPrices().subscribe(
      data => {
        this.dates = data.dates;
        this.eurPrices = data.eurPrices;
        this.ethPrices = data.ethPrices;
        this.updateChart();
      },
      error => {
        console.error('Erreur lors de la récupération des données :', error);
      }
    );
  
    // Récupérer l'ID de l'utilisateur actuel depuis le localStorage
    const userId = localStorage.getItem('user_id');
console.log('Current User ID from localStorage:', userId); // Vérifiez l'ID de l'utilisateur

    if (userId) {
      // Utilise userId pour récupérer les wallets
      this.getWalletBalance(parseInt(userId), 'ETH');
      this.getWalletBalance(parseInt(userId), 'EURO');
    } else {
      console.error('Utilisateur non connecté');
    }
  }
  
  

  ngAfterViewInit(): void {
    if (typeof document !== 'undefined') {
=======

  constructor() {}

  ngOnInit(): void {
    // Chart initialization will be handled in ngAfterViewInit to ensure DOM is ready
  }

  ngAfterViewInit(): void {
    if (typeof document !== 'undefined') {
      // Initialize chart after view is initialized and DOM is ready
>>>>>>> 8a1cd5e9c565bbcc395a5f340cef8368eb332fa1
      this.initializeChart();
      this.updateChart();
    }
  }

  initializeChart(): void {
    const ctx = document.getElementById('salesChart') as HTMLCanvasElement;
    if (ctx) {
      this.chartInstance = new Chart(ctx, {
        type: 'line',
        data: this.chartData,
        options: this.chartOptions
      });
    }
  }

<<<<<<< HEAD
updateChart(): void {
  this.chartData.labels = this.dates.reverse();
  this.chartData.datasets[0].data = this.eurPrices.reverse();
  this.chartData.datasets[1].data = this.ethPrices.reverse();

  if (this.chartInstance) {
    this.chartInstance.update(); // Met à jour le graphique
  }
}

  getWalletBalance(userId: number, currency: string): void {
    this.apiService.getWallets(userId, currency).subscribe(
      (wallets: any) => {
        const wallet = wallets.find((w: any) => w.currency === currency);
        if (wallet) {
          if (currency === 'ETH') {
            this.ethBalance = wallet.balance;
          } else if (currency === 'EURO') {
            this.eurBalance = wallet.balance;
          }
        }
      },
      (      error: any) => {
        console.error('Erreur lors de la récupération des wallets:', error);
      }
    );
  }
  fetchActiveAnnouncements(): void {
    this.apiService.getActiveAnnouncements().subscribe(
      data => {
        this.activeAnnouncements = data;
      },
      error => {
        console.error('Erreur lors de la récupération des annonces :', error);
      }
    );
  }
}

=======
  updateChart(): void {
    // Simulate fetching data
    const simulatedData = this.getSimulatedData();

    // Update chart labels and datasets
    this.chartData.labels = simulatedData.dates;
    this.chartData.datasets[0].data = simulatedData.usdPrices; // USD Prices
    this.chartData.datasets[1].data = simulatedData.ethPrices; // ETH Prices

    // Update the chart instance
    if (this.chartInstance) {
      this.chartInstance.update();
    }
  }

  getSimulatedData() {
    const dates: string[] = [];
    const usdPrices: number[] = [];
    const ethPrices: number[] = [];

    for (let i = 0; i < 10; i++) {
      const date = new Date();
      date.setMinutes(date.getMinutes() - i * 10);
      dates.unshift(date.toLocaleTimeString());
      usdPrices.unshift(+(Math.random() * 10 + 50).toFixed(2));
      ethPrices.unshift(+(Math.random() * 0.005 + 0.002).toFixed(4));
    }

    return { dates, usdPrices, ethPrices };
  }
}
>>>>>>> 8a1cd5e9c565bbcc395a5f340cef8368eb332fa1
