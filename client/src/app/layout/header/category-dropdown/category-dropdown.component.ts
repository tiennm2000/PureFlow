// category-dropdown.component.ts
import { Component, ElementRef, HostListener } from '@angular/core';

interface Category {
  imageUrl: string;
  name: string;
  link: string;
}

@Component({
  selector: 'app-category-dropdown',
  templateUrl: './category-dropdown.component.html',
  standalone: true,
})
export class CategoryDropdownComponent {
  isDropdownActive = false;

  categories: Category[] = [
    {
      imageUrl: 'assets/images/nav-category/1.jpeg',
      name: 'New Arrivals',
      link: 'shop-catalog.html',
    },
    {
      imageUrl: 'assets/images/nav-category/2.jpeg',
      name: 'Flash Sale',
      link: 'shop-catalog-v2.html',
    },
    {
      imageUrl: 'assets/images/nav-category/3.jpeg',
      name: 'Special Offer!',
      link: 'shop-catalog-v3.html',
    },
    {
      imageUrl: 'assets/images/nav-category/4.jpeg',
      name: 'Skincare',
      link: 'shop-catalog.html',
    },
    {
      imageUrl: 'assets/images/nav-category/5.jpeg',
      name: 'Body Care',
      link: 'shop-catalog-v2.html',
    },
    {
      imageUrl: 'assets/images/nav-category/6.jpeg',
      name: 'Haircare',
      link: 'shop-catalog-v3.html',
    },
    {
      imageUrl: 'assets/images/nav-category/7.jpeg',
      name: 'Beauty Tools',
      link: 'shop-catalog.html',
    },
    {
      imageUrl: 'assets/images/nav-category/10.jpeg',
      name: 'Makeup',
      link: 'shop-catalog-v2.html',
    },
    {
      imageUrl: 'assets/images/nav-category/9.jpeg',
      name: 'Face Care',
      link: 'shop-catalog-v3.html',
    },
  ];

  constructor(private elementRef: ElementRef) {}

  toggleDropdown() {
    console.log('Dropdown toggled');
    this.isDropdownActive = !this.isDropdownActive;
  }
}
