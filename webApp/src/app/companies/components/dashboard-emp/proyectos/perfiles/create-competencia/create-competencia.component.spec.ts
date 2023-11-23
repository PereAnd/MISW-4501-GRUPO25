import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateCompetenciaComponent } from './create-competencia.component';
import { AppModule } from 'src/app/app.module';

describe('Component CreateCompetenciaComponent', () => {
  let component: CreateCompetenciaComponent;
  let fixture: ComponentFixture<CreateCompetenciaComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CreateCompetenciaComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(CreateCompetenciaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'CreateCompetenciaComponent'", () => {
    expect(component).toBeTruthy();
  });
});
