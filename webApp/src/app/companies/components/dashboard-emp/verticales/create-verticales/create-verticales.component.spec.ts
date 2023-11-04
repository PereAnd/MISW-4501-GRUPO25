import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateVerticalesComponent } from './create-verticales.component';
import { AppModule } from 'src/app/app.module';

describe('Component CreateVerticalesComponent', () => {
  let component: CreateVerticalesComponent;
  let fixture: ComponentFixture<CreateVerticalesComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CreateVerticalesComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(CreateVerticalesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'CreateVerticalesComponent'", () => {
    expect(component).toBeTruthy();
  });
});
