import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListInfoAcadComponent } from './list-info-acad.component';

describe('ListInfoAcadComponent', () => {
  let component: ListInfoAcadComponent;
  let fixture: ComponentFixture<ListInfoAcadComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ListInfoAcadComponent]
    });
    fixture = TestBed.createComponent(ListInfoAcadComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
