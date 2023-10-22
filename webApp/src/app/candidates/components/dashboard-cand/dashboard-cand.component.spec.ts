import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DashboardCandComponent } from './dashboard-cand.component';
import { AppModule } from 'src/app/app.module';

describe('DashboardCandComponent', () => {
  let component: DashboardCandComponent;
  let fixture: ComponentFixture<DashboardCandComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DashboardCandComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(DashboardCandComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
