import { Component } from '@angular/core';
import { SharedModule } from '../../shared/shared.module';
import { ButtonComponent } from '../../shared/components/button/button.component';

@Component({
  selector: 'app-footer',
  imports: [SharedModule],
  templateUrl: './footer.component.html',
  styleUrl: './footer.component.css',
})
export class FooterComponent {}
