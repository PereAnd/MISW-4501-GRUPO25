import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InfoGeneralComponent } from './info-general.component';
import { AppModule } from 'src/app/app.module';

describe('Componente InfoGeneralComponent', () => {
  let component: InfoGeneralComponent;
  let fixture: ComponentFixture<InfoGeneralComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [InfoGeneralComponent],
      imports: [AppModule]
    });
    fixture = TestBed.createComponent(InfoGeneralComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it("Crear instancia de 'InfoGeneralComponent'", () => {
    expect(component).toBeTruthy();
  });
});
