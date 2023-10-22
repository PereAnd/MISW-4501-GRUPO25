import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CandidatesComponent } from './candidates.component';
import { RouterModule } from '@angular/router';

describe('CandidatesComponent', () => {
  let component: CandidatesComponent;
  let fixture: ComponentFixture<CandidatesComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CandidatesComponent],
      imports: [RouterModule]
    });
    fixture = TestBed.createComponent(CandidatesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'CandidatesComponent'", () => {
    expect(component).toBeTruthy();
  });
});
