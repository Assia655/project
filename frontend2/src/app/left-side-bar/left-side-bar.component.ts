import { Component,computed, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatListModule } from '@angular/material/list';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-left-side-bar',
  standalone: true,
  imports: [CommonModule,RouterModule,MatSidenavModule,MatListModule,MatIconModule],
  templateUrl: './left-side-bar.component.html',
  styleUrl: './left-side-bar.component.css'
})
export class LeftSideBarComponent {
collapsed=signal(false);

sidenavWidth=computed(()=>this.collapsed()?'65px':'250px');

profilePicSize=computed(()=> this.collapsed() ? '32': '100')
  

 }


