import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EntrevistasAbcComponent } from './entrevistas-abc.component';
import { AppModule } from 'src/app/app.module';

describe('EntrevistasAbcComponent', () => {
  let component: EntrevistasAbcComponent;
  let fixture: ComponentFixture<EntrevistasAbcComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [EntrevistasAbcComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(EntrevistasAbcComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'EntrevistasAbcComponent'", () => {
    expect(component).toBeTruthy();
  });
});
