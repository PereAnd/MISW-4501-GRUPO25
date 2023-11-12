import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PerfilesComponent } from './perfil.component';
import { AppModule } from 'src/app/app.module';

describe('PerfilesComponent', () => {
  let component: PerfilesComponent;
  let fixture: ComponentFixture<PerfilesComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PerfilesComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(PerfilesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'PerfilesComponent'", () => {
    expect(component).toBeTruthy();
  });
});
