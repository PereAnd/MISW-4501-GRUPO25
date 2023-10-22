import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateInfoTecComponent } from './create-info-tec.component';
import { AppModule } from 'src/app/app.module';

describe('CreateInfoTecComponent', () => {
  let component: CreateInfoTecComponent;
  let fixture: ComponentFixture<CreateInfoTecComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CreateInfoTecComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(CreateInfoTecComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'CreateInfoTecComponent'", () => {
    expect(component).toBeTruthy();
  });
});
