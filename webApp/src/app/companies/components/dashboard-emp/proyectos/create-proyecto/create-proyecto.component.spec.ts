import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateProyectoComponent } from './create-proyecto.component';
import { AppModule } from 'src/app/app.module';

describe('Component CreateProyectoComponent', () => {
  let component: CreateProyectoComponent;
  let fixture: ComponentFixture<CreateProyectoComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CreateProyectoComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(CreateProyectoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'CreateProyectoComponent'", () => {
    expect(component).toBeTruthy();
  });
});
