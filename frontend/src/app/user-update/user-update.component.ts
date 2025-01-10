import { CommonModule } from '@angular/common';
import { Component, ViewChild } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { SidebarComponent } from "../sidebar/sidebar.component";
import { NgbModal, NgbModule } from '@ng-bootstrap/ng-bootstrap'; // Import NgbModule


@Component({
  selector: 'app-user-update',
  imports: [
    CommonModule,
    FormsModule,
    SidebarComponent,
    NgbModule
],
  templateUrl: './user-update.component.html',
  styleUrl: './user-update.component.css'
})
export class UserUpdateComponent {
  @ViewChild('confirmationModal') confirmationModal: any; 
  user = {
    name: 'John Doe',
    email: 'johndoe@example.com',
    password: '',
    country: 'France',
    state: 'Cabo Verde',
    city: 'Mumbai',
    role: 'Customer',
    phone: '+212 646211526'
  };

  constructor(private modalService: NgbModal) {}

   // Submit method called when the user clicks "Submit"
   onSubmit() {
    console.log('Form Submitted', this.user);
    // Add logic to save or send the updated user data to the server
  }

  // Open the confirmation modal when the user clicks "Submit"
  openModal() {
    this.modalService.open(this.confirmationModal, { ariaLabelledBy: 'modal-basic-title' });
  }

  // Confirm the changes and close the modal
  confirmChanges(modal: any) {
    console.log('Changes confirmed:', this.user);
    modal.close();
  }
  cancel() {
    // Logic to cancel the form and navigate away or clear the fields
    console.log('Edit canceled');
  }
}
