import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BusquedaCandComponent } from './busqueda-cand.component';
import { AppModule } from 'src/app/app.module';

describe('BusquedaCandComponent', () => {
  let component: BusquedaCandComponent;
  let fixture: ComponentFixture<BusquedaCandComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [BusquedaCandComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(BusquedaCandComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'BusquedaCandComponent'", () => {
    expect(component).toBeTruthy();
  });
});
