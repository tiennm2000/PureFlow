import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ButtonComponent } from './components/button/button.component';
import { BreadcrumbComponent } from './components/breadcrumb/breadcrumb.component';
import { InputComponent } from './components/input/input.component';

@NgModule({
  declarations: [ButtonComponent, BreadcrumbComponent, InputComponent],
  exports: [ButtonComponent, BreadcrumbComponent],
  imports: [CommonModule],
})
export class SharedModule {}
