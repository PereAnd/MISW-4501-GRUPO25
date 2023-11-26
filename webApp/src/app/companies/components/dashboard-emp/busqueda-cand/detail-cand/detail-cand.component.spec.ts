import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DetailCandComponent } from './detail-cand.component';

describe('DetailCandComponent', () => {
  let component: DetailCandComponent;
  let fixture: ComponentFixture<DetailCandComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DetailCandComponent]
    });
    fixture = TestBed.createComponent(DetailCandComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
