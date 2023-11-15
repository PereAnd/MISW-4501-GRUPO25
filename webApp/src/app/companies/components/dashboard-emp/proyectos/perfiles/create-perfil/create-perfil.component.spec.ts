import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreatePerfilComponent } from './create-perfil.component';
import { AppModule } from 'src/app/app.module';

describe('CreatePerfilComponent', () => {
  let component: CreatePerfilComponent;
  let fixture: ComponentFixture<CreatePerfilComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CreatePerfilComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(CreatePerfilComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'CreatePerfilComponent'", () => {
    expect(component).toBeTruthy();
  });
});
