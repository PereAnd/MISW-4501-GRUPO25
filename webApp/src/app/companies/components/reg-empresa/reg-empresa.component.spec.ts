import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegEmpresaComponent } from './reg-empresa.component';
import { AppModule } from 'src/app/app.module';

describe('RegEmpresaComponent', () => {
  let component: RegEmpresaComponent;
  let fixture: ComponentFixture<RegEmpresaComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [RegEmpresaComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(RegEmpresaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'RegEmpresaComponent'", () => {
    expect(component).toBeTruthy();
  });
});
