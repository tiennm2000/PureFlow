import { Component, Input } from '@angular/core';
import InputField from '../../../interface/input.interface';

@Component({
  selector: 'app-input',

  templateUrl: './input.component.html',
  styleUrl: './input.component.css',
  standalone: false,
})
export class InputComponent {
  @Input() inputField: InputField = {
    type: 'text',
    placeholder: 'Enter text here',
  };
}
