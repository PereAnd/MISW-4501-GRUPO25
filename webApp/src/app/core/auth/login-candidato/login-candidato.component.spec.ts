import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LoginCandidatoComponent } from './login-candidato.component';
import { AppModule } from 'src/app/app.module';

describe('LoginCandidatoComponent', () => {
  let component: LoginCandidatoComponent;
  let fixture: ComponentFixture<LoginCandidatoComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [LoginCandidatoComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(LoginCandidatoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
