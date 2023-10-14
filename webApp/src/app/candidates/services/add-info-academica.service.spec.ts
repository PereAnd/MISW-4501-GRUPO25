import { TestBed } from '@angular/core/testing';

import { AddInfoAcademicaService } from './add-info-academica.service';

describe('AddInfoAcademicaService', () => {
  let service: AddInfoAcademicaService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AddInfoAcademicaService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
