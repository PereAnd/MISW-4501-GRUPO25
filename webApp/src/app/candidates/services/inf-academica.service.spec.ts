import { TestBed } from '@angular/core/testing';

import { InfAcademicaService } from './inf-academica.service';

describe('InfAcademicaService', () => {
  let service: InfAcademicaService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(InfAcademicaService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
