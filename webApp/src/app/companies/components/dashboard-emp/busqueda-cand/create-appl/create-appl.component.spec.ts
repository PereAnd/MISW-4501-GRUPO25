import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateApplComponent } from './create-appl.component';
import { AppModule } from 'src/app/app.module';

describe('CreateApplComponent', () => {
  let component: CreateApplComponent;
  let fixture: ComponentFixture<CreateApplComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CreateApplComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(CreateApplComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'CreateApplComponent'", () => {
    expect(component).toBeTruthy();
  });
});
