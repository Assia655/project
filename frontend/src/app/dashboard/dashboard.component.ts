import { Component, OnInit } from '@angular/core';
import { Chart, ChartConfiguration } from 'chart.js/auto';
import { SidebarComponent } from '../sidebar/sidebar.component';


@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css'],
  imports: [SidebarComponent]
})
export class DashboardComponent implements OnInit {
  // Chart.js configuration
  chartData: ChartConfiguration['data'] = {
    labels: [], // Dynamic labels
    datasets: [
      {
        label: 'Carbon Price in USD',
        data: [], // Dynamic data
        backgroundColor: 'rgba(75, 192, 192, 0.2)', // Fill color
        borderColor: 'rgba(75, 192, 192, 1)', // Line color
        borderWidth: 2,
        tension: 0.4
      },
      {
        label: 'Carbon Price in ETH',
        data: [], // Dynamic data
        backgroundColor: 'rgba(153, 102, 255, 0.2)',
        borderColor: 'rgba(153, 102, 255, 1)',
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

  constructor() {}

  ngOnInit(): void {
    this.initializeChart();
    this.updateChart();
  }

  initializeChart(): void {
    const ctx = document.getElementById('salesChart') as HTMLCanvasElement;
    this.chartInstance = new Chart(ctx, {
      type: 'line',
      data: this.chartData,
      options: this.chartOptions
    });
  }

  updateChart(): void {
    // Simulate fetching data
    const simulatedData = this.getSimulatedData();

    // Update chart labels and datasets
    this.chartData.labels = simulatedData.dates;
    this.chartData.datasets[0].data = simulatedData.usdPrices; // USD Prices
    this.chartData.datasets[1].data = simulatedData.ethPrices; // ETH Prices

    // Update the chart instance
    this.chartInstance.update();
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
