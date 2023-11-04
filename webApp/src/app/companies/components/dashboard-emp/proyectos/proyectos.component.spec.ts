import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProyectosComponent } from './proyectos.component';
import { AppModule } from 'src/app/app.module';

describe('Component ProyectosComponent', () => {
  let component: ProyectosComponent;
  let fixture: ComponentFixture<ProyectosComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ProyectosComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(ProyectosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'ProyectosComponent'", () => {
    expect(component).toBeTruthy();
  });
});
