import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EntrevistasEmpComponent } from './entrevistas-emp.component';
import { AppModule } from 'src/app/app.module';

describe('EntrevistasEmpComponent', () => {
  let component: EntrevistasEmpComponent;
  let fixture: ComponentFixture<EntrevistasEmpComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [EntrevistasEmpComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(EntrevistasEmpComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'EntrevistasEmpComponent'", () => {
    expect(component).toBeTruthy();
  });
});
