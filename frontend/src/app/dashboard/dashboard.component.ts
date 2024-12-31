import { Component } from '@angular/core';
import { HeaderComponent } from '../header/header.component';
import { LeftSideBarComponent } from '../left-side-bar/left-side-bar.component';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [LeftSideBarComponent,RouterOutlet],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent {

}
