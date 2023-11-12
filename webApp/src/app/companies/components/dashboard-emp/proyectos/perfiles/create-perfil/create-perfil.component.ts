import { LiveAnnouncer } from '@angular/cdk/a11y';
import { Component, ElementRef, ViewChild, inject } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Observable, map, startWith } from 'rxjs';
import { Perfil } from 'src/app/companies/models/perfil';
import { PerfilesService } from 'src/app/companies/services/perfiles.service';
import {COMMA, ENTER} from '@angular/cdk/keycodes';
import { MatAutocompleteSelectedEvent } from '@angular/material/autocomplete';
import { MatChipInputEvent } from '@angular/material/chips';

@Component({
  selector: 'app-create-perfil',
  templateUrl: './create-perfil.component.html',
  styleUrls: ['./create-perfil.component.css']
})
export class CreatePerfilComponent {
  indexProyecto: number;
  empresaId: number;
  longText: string = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptatum.';

  formPerfiles: FormGroup = new FormGroup({
    name: new FormControl('', Validators.required),
    role: new FormControl('', Validators.required),
    location: new FormControl('', Validators.required),
    years: new FormControl('', Validators.required),
    conocimientos: new FormControl('', Validators.required),
    habilidades: new FormControl('', Validators.required),
    idiomas: new FormControl('', Validators.required),
  });

  get name() { return this.formPerfiles.get('name') }
  get role() { return this.formPerfiles.get('role') }
  get location() { return this.formPerfiles.get('location') }
  get years() { return this.formPerfiles.get('years') }
  get conocimientos() { return this.formPerfiles.get('conocimientos') }
  get habilidades() { return this.formPerfiles.get('habilidades') }
  get idiomas() { return this.formPerfiles.get('idiomas') }

  constructor(
    private perfilesService: PerfilesService,
    private router: Router,
    private route: ActivatedRoute
  ) {
    this.empresaId = +localStorage.getItem('empresaId')!;
  }

  ngOnInit(): void {
    // this.indexProyecto = this.route.snapshot.params['idp'];
    // if (this.indexProyecto) {
    //   this.perfilesService.addPerfil(this.empresaId, this.indexProyecto).subscribe({
    //     next: (data) => {
    //       this.formProyectos.setValue({
    //         proyecto: data.proyecto,
    //         description: data.description,
    //       });
    //     },
    //     error: (error) =>
    //       console.error('Error obteniendo el proyecto seleccionado', error),
    //   });
    // }
  }

  registrarProyecto() {
    const newPerfil = new Perfil(
      this.formPerfiles.value.name,
      this.formPerfiles.value.role,
      this.formPerfiles.value.location,
      this.formPerfiles.value.years,
      this.formPerfiles.value.conocimientos,
      this.formPerfiles.value.habilidades,
      this.formPerfiles.value.idiomas,
    );
    if (!this.indexProyecto) {
      this.perfilesService.addPerfil(this.indexProyecto, this.empresaId, newPerfil).subscribe({
        next: (data) => {
          console.log('Perfil registrado');
          this.formPerfiles.reset();
        },
        error: (error) => {
          console.log('Error registrando el perfil', error);
          alert('Error registrando el perfil');
        },
        complete: () => {
          this.router.navigate(['..'], { relativeTo: this.route });
        },
      });
    }
    // else {
    //   this.perfilesService
    //     .editProyecto(newProyecto, this.indexProyecto, this.empresaId)
    //     .subscribe({
    //       next: (data) => {
    //         console.log('Proyecto actualizado');
    //         this.formProyectos.reset();
    //       },
    //       error: (error) => {
    //         console.log('Error editando el proyecto', error);
    //         alert('Error editando el proyecto');
    //       },
    //       complete: () => {
    //         this.router.navigate(['..'], { relativeTo: this.route });
    //       },
    //     });
    // }
  }

  cancelarCreacion() {
    this.formPerfiles.reset();
  }
}
