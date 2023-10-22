import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegCandidatoComponent } from './reg-candidato.component';
import { AppModule } from 'src/app/app.module';

describe('RegCandidatoComponent', () => {
  let component: RegCandidatoComponent;
  let fixture: ComponentFixture<RegCandidatoComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [RegCandidatoComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(RegCandidatoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
