import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateInfoAcadComponent } from './create-info-acad.component';
import { AppModule } from 'src/app/app.module';

describe('CreateInfoAcadComponent', () => {
  let component: CreateInfoAcadComponent;
  let fixture: ComponentFixture<CreateInfoAcadComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CreateInfoAcadComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(CreateInfoAcadComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
