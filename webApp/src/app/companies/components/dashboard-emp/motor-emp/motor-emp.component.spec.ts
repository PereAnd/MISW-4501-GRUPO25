import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MotorEmpComponent } from './motor-emp.component';
import { AppModule } from 'src/app/app.module';

describe('MotorEmpComponent', () => {
  let component: MotorEmpComponent;
  let fixture: ComponentFixture<MotorEmpComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [MotorEmpComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(MotorEmpComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'MotorEmpComponent'", () => {
    expect(component).toBeTruthy();
  });
});
