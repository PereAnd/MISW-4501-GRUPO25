import { TestBed } from '@angular/core/testing';

import { RegEmpresaService } from './reg-empresa.service';

describe('RegEmpresaService', () => {
  let service: RegEmpresaService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RegEmpresaService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
