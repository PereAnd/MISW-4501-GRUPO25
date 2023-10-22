import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InfoAcademicaComponent } from './info-academica.component';
import { AppModule } from 'src/app/app.module';

describe('InfoAcademicaComponent', () => {
  let component: InfoAcademicaComponent;
  let fixture: ComponentFixture<InfoAcademicaComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [InfoAcademicaComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(InfoAcademicaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'InfoAcademicaComponent", () => {
    expect(component).toBeTruthy();
  });
});
