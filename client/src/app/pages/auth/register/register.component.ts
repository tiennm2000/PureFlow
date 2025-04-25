import { Component } from '@angular/core';
import BreadcrumbItem from '../../../interface/breadcrumb.interface';

@Component({
  selector: 'app-register',

  templateUrl: './register.component.html',
  styleUrl: './register.component.css',
  standalone: false,
})
export class RegisterComponent {
  title = 'Sign-Up for a Radiant Experience';
  description = "Fill out the form below, and let's get started.";
  imageUrl = 'assets/images/login_banner.jpeg';
  currentPage = 'Register';
  breadcrumbItem: BreadcrumbItem = {
    imageUrl: this.imageUrl,
    title: this.title,
    currentPage: this.currentPage,
    description: this.description,
  };
}
