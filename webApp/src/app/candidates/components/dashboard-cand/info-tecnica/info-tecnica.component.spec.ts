import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InfoTecnicaComponent } from './info-tecnica.component';
import { AppModule } from 'src/app/app.module';

describe('InfoTecnicaComponent', () => {
  let component: InfoTecnicaComponent;
  let fixture: ComponentFixture<InfoTecnicaComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [InfoTecnicaComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(InfoTecnicaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
