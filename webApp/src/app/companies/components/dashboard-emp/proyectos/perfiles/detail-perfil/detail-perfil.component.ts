import { Component, OnInit } from '@angular/core';
import { Perfil } from 'src/app/companies/models/perfil';
import { PerfilesService } from 'src/app/companies/services/perfiles.service';

@Component({
  selector: 'app-detail-perfil',
  templateUrl: './detail-perfil.component.html',
  styleUrls: ['./detail-perfil.component.css']
})
export class DetailPerfilComponent implements OnInit{
  profileDetail: Perfil;

  constructor(
    private perfilesService: PerfilesService
  ){}

  ngOnInit(): void {
    this.perfilesService.getProfileDetail().subscribe({
      next: profile => {
        this.profileDetail = profile;
      }
    })
  }
}
