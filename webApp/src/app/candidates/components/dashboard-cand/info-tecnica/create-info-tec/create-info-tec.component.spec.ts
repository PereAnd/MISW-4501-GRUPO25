import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateInfoTecComponent } from './create-info-tec.component';

describe('CreateInfoTecComponent', () => {
  let component: CreateInfoTecComponent;
  let fixture: ComponentFixture<CreateInfoTecComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CreateInfoTecComponent]
    });
    fixture = TestBed.createComponent(CreateInfoTecComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
