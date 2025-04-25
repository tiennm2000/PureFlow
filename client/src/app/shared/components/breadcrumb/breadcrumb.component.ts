import { Component, Input } from '@angular/core';

import BreadcrumbItem from '../../../interface/breadcrumb.interface';

@Component({
  selector: 'app-breadcrumb',

  templateUrl: './breadcrumb.component.html',
  styleUrl: './breadcrumb.component.css',
  standalone: false,
})
export class BreadcrumbComponent {
  @Input() breadcrumbItem: BreadcrumbItem = {
    imageUrl: '',
    title: '',
    currentPage: '',
    description: '',
  };
}
