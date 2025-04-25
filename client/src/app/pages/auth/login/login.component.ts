import { Component } from '@angular/core';
import BreadcrumbItem from '../../../interface/breadcrumb.interface';

@Component({
  selector: 'app-login',

  templateUrl: './login.component.html',
  styleUrl: './login.component.css',
  standalone: false,
})
export class LoginComponent {
  title = 'Member Login';
  description = 'Access your Glowify account to continue your beauty journey.';
  imageUrl = 'assets/images/login_banner.jpeg';
  currentPage = 'Login';
  breadcrumbItem: BreadcrumbItem = {
    imageUrl: this.imageUrl,
    title: this.title,
    currentPage: this.currentPage,
    description: this.description,
  };
}
