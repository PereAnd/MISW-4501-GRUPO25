import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EntrevistasCandComponent } from './entrevistas-cand.component';
import { AppModule } from 'src/app/app.module';

describe('EntrevistasCandComponent', () => {
  let component: EntrevistasCandComponent;
  let fixture: ComponentFixture<EntrevistasCandComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [EntrevistasCandComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(EntrevistasCandComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'EntrevistasCandComponent'", () => {
    expect(component).toBeTruthy();
  });
});
