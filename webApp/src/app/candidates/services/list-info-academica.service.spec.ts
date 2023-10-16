import { TestBed } from '@angular/core/testing';

import { ListInfoAcademicaService } from './list-info-academica.service';

describe('ListInfoAcademicaService', () => {
  let service: ListInfoAcademicaService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ListInfoAcademicaService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
