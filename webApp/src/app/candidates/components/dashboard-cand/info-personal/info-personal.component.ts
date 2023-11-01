import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { Candidato } from 'src/app/candidates/models/candidato';
import { RegCandidatoService } from 'src/app/candidates/services/reg-candidato.service';

@Component({
  selector: 'app-info-personal',
  templateUrl: './info-personal.component.html',
  styleUrls: ['./info-personal.component.css']
})
export class InfoPersonalComponent {
  candidato: Candidato;
  isEditMode: boolean;
  formInfoPersonal: FormGroup;

  idiomasPreferidos: string[] = ['Español', 'Inglés']
  tiposDocumento = [
    { nameDoc: 'Cédula de ciudadanía', value: 'CC' },
    { nameDoc: 'Cédula de extranjería', value: 'CE' },
    { nameDoc: 'Pasaporte', value: 'PP' }
  ]

  constructor(
    private regCandidatoService: RegCandidatoService,
    private router: Router,
    private route: ActivatedRoute
  ){
    this.isEditMode = false;
    this.formInfoPersonal = new FormGroup({
      names: new FormControl('', Validators.required),
      lastNames: new FormControl('', Validators.required),
      mail: new FormControl('', Validators.required),
      docType: new FormControl('', Validators.required),
      docNumber: new FormControl('', Validators.required),
      phone: new FormControl('', Validators.required),
      address: new FormControl('', Validators.required),
      birthDate: new FormControl(null, Validators.required),
      country: new FormControl('', Validators.required),
      city: new FormControl('', Validators.required),
      language: new FormControl('', Validators.required)
    })
  }

  get names() { return this.formInfoPersonal.get('names') }
  get lastNames() { return this.formInfoPersonal.get('lastNames') }
  get mail() { return this.formInfoPersonal.get('mail') }
  get docType() { return this.formInfoPersonal.get('docType') }
  get docNumber() { return this.formInfoPersonal.get('docNumber') }
  get phone() { return this.formInfoPersonal.get('phone') }
  get address() { return this.formInfoPersonal.get('address') }
  get birthDate() { return this.formInfoPersonal.get('birthDate') }
  get country() { return this.formInfoPersonal.get('country') }
  get city() { return this.formInfoPersonal.get('city') }
  get language() { return this.formInfoPersonal.get('language') }

  ngOnInit(): void {
    const idCandidato: number = 1;
    this.isEditMode ? this.formInfoPersonal.enable() : this.formInfoPersonal.disable();
    this.regCandidatoService.getDatosCandidato(idCandidato).subscribe({
      next: data => {
        this.candidato = data;
        this.formInfoPersonal.setValue({
          names: data.names,
          lastNames: data.lastNames,
          mail: data.mail,
          docType: data.docType,
          docNumber: data.docNumber,
          phone: data.phone,
          address: data.address,
          birthDate: data.birthDate ? new Date(data.birthDate) : null,
          country: data.country,
          city: data.city,
          language: data.language
        })
      },
      error: error => {
        console.log("Error obteniendo los datos del candidato", error)
      }
    })
  }

  guardarInfoPersonal(){
    this.candidato.names = this.formInfoPersonal.value.names;
    this.candidato.lastNames = this.formInfoPersonal.value.lastNames;
    this.candidato.mail = this.formInfoPersonal.value.mail;
    this.candidato.docType = this.formInfoPersonal.value.docType;
    this.candidato.docNumber = this.formInfoPersonal.value.docNumber;
    this.candidato.phone = this.formInfoPersonal.value.phone;
    this.candidato.address = this.formInfoPersonal.value.address;
    this.candidato.birthDate = this.formInfoPersonal.value.birthDate;
    this.candidato.country = this.formInfoPersonal.value.country;
    this.candidato.city = this.formInfoPersonal.value.city;
    this.candidato.language = this.formInfoPersonal.value.language;

    this.regCandidatoService.updateDatosCandidato(this.candidato).subscribe({
      next: data => {
        console.log("Datos del candidato actualizados")
      },
      error: error => {
        console.log("Error actualizando los datos del candidato")
      }
    })
    this.changeEditMode()
  }

  changeEditMode(){
    this.isEditMode = !this.isEditMode;
    this.isEditMode ? this.formInfoPersonal.enable() : this.formInfoPersonal.disable();
  }

  cancelarCreacion(){
    this.formInfoPersonal.reset()
  }
}
