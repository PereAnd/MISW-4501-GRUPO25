import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DashboardAbcComponent } from './dashboard-abc.component';
import { AppModule } from 'src/app/app.module';

describe('DashboardAbcComponent', () => {
  let component: DashboardAbcComponent;
  let fixture: ComponentFixture<DashboardAbcComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DashboardAbcComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(DashboardAbcComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'DashboardAbcComponent'", () => {
    expect(component).toBeTruthy();
  });
});
