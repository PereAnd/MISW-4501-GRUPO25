import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UbicacionesComponent } from './ubicaciones.component';
import { AppModule } from 'src/app/app.module';

describe('UbicacionesComponent', () => {
  let component: UbicacionesComponent;
  let fixture: ComponentFixture<UbicacionesComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [UbicacionesComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(UbicacionesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'UbicacionesComponent'", () => {
    expect(component).toBeTruthy();
  });
});
