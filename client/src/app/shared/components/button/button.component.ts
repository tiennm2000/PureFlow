import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-button',

  templateUrl: './button.component.html',
  styleUrl: './button.component.css',
  standalone: false,
})
export class ButtonComponent {
  @Input() text: string = '';
}
