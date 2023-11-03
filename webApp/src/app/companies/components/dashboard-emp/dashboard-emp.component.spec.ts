import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DashboardEmpComponent } from './dashboard-emp.component';
import { AppModule } from 'src/app/app.module';

describe('Componente DashboardEmpComponent', () => {
  let component: DashboardEmpComponent;
  let fixture: ComponentFixture<DashboardEmpComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DashboardEmpComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(DashboardEmpComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'DashboardEmpComponent'", () => {
    expect(component).toBeTruthy();
  });
});
