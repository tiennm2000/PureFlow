import { Component } from '@angular/core';
import { CategoryDropdownComponent } from './category-dropdown/category-dropdown.component';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-header',
  imports: [CategoryDropdownComponent, RouterLink],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css',
  standalone: true,
})
export class HeaderComponent {}
