import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DetailPerfilComponent } from './detail-perfil.component';

describe('DetailPerfilComponent', () => {
  let component: DetailPerfilComponent;
  let fixture: ComponentFixture<DetailPerfilComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DetailPerfilComponent]
    });
    fixture = TestBed.createComponent(DetailPerfilComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
