import { TestBed } from '@angular/core/testing';

import { RegCandidatoService } from './reg-candidato.service';

describe('RegCandidatoService', () => {
  let service: RegCandidatoService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(RegCandidatoService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
