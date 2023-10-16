import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegCandidatoComponent } from './reg-candidato.component';

describe('RegCandidatoComponent', () => {
  let component: RegCandidatoComponent;
  let fixture: ComponentFixture<RegCandidatoComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [RegCandidatoComponent]
    });
    fixture = TestBed.createComponent(RegCandidatoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
