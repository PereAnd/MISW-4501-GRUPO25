import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateUbicacionComponent } from './create-ubicacion.component';
import { AppModule } from 'src/app/app.module';

describe('CreateUbicacionComponent', () => {
  let component: CreateUbicacionComponent;
  let fixture: ComponentFixture<CreateUbicacionComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CreateUbicacionComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(CreateUbicacionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'CreateUbicacionComponent'", () => {
    expect(component).toBeTruthy();
  });
});
