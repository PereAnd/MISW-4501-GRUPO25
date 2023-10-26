import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InfoLaboralComponent } from './info-laboral.component';
import { AppModule } from 'src/app/app.module';

describe('InfoLaboralComponent', () => {
  let component: InfoLaboralComponent;
  let fixture: ComponentFixture<InfoLaboralComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [InfoLaboralComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(InfoLaboralComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'InfoLaboralComponent", () => {
    expect(component).toBeTruthy();
  });
});
