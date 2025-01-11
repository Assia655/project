import { Component, OnInit, AfterViewInit } from '@angular/core';
import { Chart, ChartConfiguration } from 'chart.js/auto';
import { ApiService } from '../services/api.service';
import { SidebarComponent } from '../sidebar/sidebar.component';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css'],
  imports: [SidebarComponent, CommonModule],
  providers: [ApiService]
})
export class DashboardComponent implements OnInit, AfterViewInit {
  dates: string[] = [];
  eurPrices: number[] = [];
  ethPrices: number[] = [];
  
  ethBalance: number = 0; 
  eurBalance: number = 0; 

  chartData: ChartConfiguration['data'] = {
    labels: [], // Liste des dates
    datasets: [
      {
        label: 'Price in EUR',
        data: [],
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgb(75, 192, 134)',
        borderWidth: 2,
        tension: 0.4
      },
      {
        label: 'Price in ETH',
        data: [],
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
  
  activeAnnouncements: { id: number; credit_amount: Number; seller_id: Number; }[] = [];
  transactions: any[] = []; // To store the transactions

  constructor(private apiService: ApiService) {}
  userId: number = 0;  
  ngOnInit(): void {
    this.fetchActiveAnnouncements(); 

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

  
    const storedUserId = localStorage.getItem('user_id');
    if (storedUserId) {
      this.userId = Number(storedUserId);
      console.log('Current User ID from localStorage:', this.userId);
    }    console.log('Current User ID from localStorage:', this.userId); // Vérifiez l'ID de l'utilisateur

    if (this.userId) {
      this.getWalletBalance(this.userId, 'ETH');
      this.getWalletBalance(this.userId, 'EURO');
      this.apiService.getTransactions(this.userId).subscribe(response => {
        if (Array.isArray(response)) {
          this.transactions = response;
        } else if (response) {
          this.transactions = [response];  // transforme un objet unique en tableau
        } else {
          this.transactions = [];  // Aucune transaction, assignez un tableau vide
        }
      }, error => {
        console.error('Erreur lors de la récupération des transactions', error);
        this.transactions = [];  
      });
    } else {
      console.error('Utilisateur non connecté');
    }
  }

  ngAfterViewInit(): void {
    if (typeof document !== 'undefined') {
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

  updateChart(): void {
    this.chartData.labels = this.dates.reverse();
    this.chartData.datasets[0].data = this.eurPrices.reverse();
    this.chartData.datasets[1].data = this.ethPrices.reverse();

    if (this.chartInstance) {
      this.chartInstance.update(); // Mettre a jour le graphique
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
      (error: any) => {
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

  getTransactionAmount(transaction: any): string {
    if (transaction.buyer_id === this.userId) {
      return `-${transaction.total_price} ${transaction.currency}`;
    } else if (transaction.seller_id === this.userId) {
      return `${transaction.total_price} ${transaction.currency}`;
    } else {
      return 'Transaction inconnue';
    }
  }
}
