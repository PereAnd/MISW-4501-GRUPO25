import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VerticalesComponent } from './verticales.component';
import { AppModule } from 'src/app/app.module';

describe('Componente VerticalesComponent', () => {
  let component: VerticalesComponent;
  let fixture: ComponentFixture<VerticalesComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [VerticalesComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(VerticalesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'VerticalesComponent'", () => {
    expect(component).toBeTruthy();
  });
});
