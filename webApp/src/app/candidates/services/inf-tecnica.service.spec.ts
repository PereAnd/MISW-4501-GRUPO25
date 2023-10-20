import { TestBed } from '@angular/core/testing';

import { InfTecnicaService } from './inf-tecnica.service';

describe('InfTecnicaService', () => {
  let service: InfTecnicaService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(InfTecnicaService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
