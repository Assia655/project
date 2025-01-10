import { Component } from '@angular/core';
<<<<<<< HEAD
import { SponsorsComponent } from "../sponsors/sponsors.component";
import { AboutComponent } from "../about/about.component";
import { ContactComponent } from "../contact/contact.component";

@Component({
  selector: 'app-home',
  imports: [SponsorsComponent, AboutComponent, ContactComponent],
=======
import { CommonModule } from '@angular/common';
import { MatButtonModule } from '@angular/material/button';
import { SponsorsComponent } from "../sponsors/sponsors.component";
import { AboutComponent } from '../about/about.component';
import { FooterComponent } from '../footer/footer.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, MatButtonModule, SponsorsComponent, AboutComponent, FooterComponent],
>>>>>>> 8a1cd5e9c565bbcc395a5f340cef8368eb332fa1
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {

}
