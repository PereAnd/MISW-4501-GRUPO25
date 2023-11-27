import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateEntrevistaComponent } from './create-entrevista.component';
import { AppModule } from 'src/app/app.module';

describe('CreateEntrevistaComponent', () => {
  let component: CreateEntrevistaComponent;
  let fixture: ComponentFixture<CreateEntrevistaComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CreateEntrevistaComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(CreateEntrevistaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'CreateEntrevistaComponent'", () => {
    expect(component).toBeTruthy();
  });
});
