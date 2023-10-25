import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateInfoLaboralComponent } from './create-info-laboral.component';

describe('CreateInfoLaboralComponent', () => {
  let component: CreateInfoLaboralComponent;
  let fixture: ComponentFixture<CreateInfoLaboralComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CreateInfoLaboralComponent]
    });
    fixture = TestBed.createComponent(CreateInfoLaboralComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
