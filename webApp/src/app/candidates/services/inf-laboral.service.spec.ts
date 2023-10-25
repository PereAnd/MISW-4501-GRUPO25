import { TestBed } from '@angular/core/testing';

import { InfLaboralService } from './inf-laboral.service';

describe('InfLaboralService', () => {
  let service: InfLaboralService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(InfLaboralService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
