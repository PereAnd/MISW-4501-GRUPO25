import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateInfoLaboralComponent } from './create-info-laboral.component';
import { AppModule } from 'src/app/app.module';

describe('CreateInfoLaboralComponent', () => {
  let component: CreateInfoLaboralComponent;
  let fixture: ComponentFixture<CreateInfoLaboralComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CreateInfoLaboralComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(CreateInfoLaboralComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'CreateInfoLaboralComponent'", () => {
    expect(component).toBeTruthy();
  });
});
