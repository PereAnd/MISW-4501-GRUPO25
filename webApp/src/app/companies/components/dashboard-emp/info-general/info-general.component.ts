import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Empresa } from 'src/app/companies/models/empresa';
import { RegEmpresaService } from 'src/app/companies/services/reg-empresa.service';

@Component({
  selector: 'app-info-general',
  templateUrl: './info-general.component.html',
  styleUrls: ['./info-general.component.css']
})
export class InfoGeneralComponent implements OnInit {
  empresa: Empresa;
  isEditMode: boolean;
  formInfoGeneral: FormGroup;
  empresaId: number;

  tiposDeEmpresa: string[] = ['Startup', 'Desarrollo de Software', 'Proveedor de Servicios', 'Empresa de Ciberseguridad', 'Consultora de Tecnología', 'Tienda de Tecnología', 'Agencia de Desarrollo de Aplicaciones Móviles', 'Empresa de Análisis de Datos', 'Compañía de IA']

  tiposDeDocumento: string[] = ['NIT', 'RUC']

  constructor(
    private regEmpresaService: RegEmpresaService,
    private router: Router,
    private route: ActivatedRoute
  ){
    this.empresaId = +localStorage.getItem('empresaId')!;
    this.formInfoGeneral = new FormGroup({
      name: new FormControl('', Validators.required),
      organizationType: new FormControl('', Validators.required),
      mail: new FormControl('', Validators.required),
      docType: new FormControl('', Validators.required),
      docNumber: new FormControl('', Validators.required),
      description: new FormControl('')
    })
  }

  get name() { return this.formInfoGeneral.get('name') }
  get organizationType() { return this.formInfoGeneral.get('organizationType') }
  get mail() { return this.formInfoGeneral.get('mail') }
  get docType() { return this.formInfoGeneral.get('docType') }
  get docNumber() { return this.formInfoGeneral.get('docNumber') }
  get description() { return this.formInfoGeneral.get('description') }

  ngOnInit(): void {
    this.isEditMode ? this.formInfoGeneral.enable() : this.formInfoGeneral.disable();
    this.regEmpresaService.getDatosEmpresa(this.empresaId).subscribe({
      next: data => {
        this.empresa = data;
        this.formInfoGeneral.setValue({
          name: data.name,
          organizationType: data.organizationType,
          mail: data.mail,
          docType: data.docType,
          docNumber: data.docNumber,
          description: data.description,
        })
      },
      error: error => {
        console.log("Error obteniendo los datos del candidato", error)
      }
    })
  }

  guardarInfoGeneral(){
    this.empresa.name = this.formInfoGeneral.value.name;
    this.empresa.organizationType = this.formInfoGeneral.value.organizationType;
    this.empresa.mail = this.formInfoGeneral.value.mail;
    this.empresa.docType = this.formInfoGeneral.value.docType;
    this.empresa.docNumber = this.formInfoGeneral.value.docNumber;
    this.empresa.description = this.formInfoGeneral.value.description;

    this.regEmpresaService.updateDatosEmpresa(this.empresa).subscribe({
      next: data => {
        console.log("Datos de la empresa actualizados")
      },
      error: error => {
        console.log("Error actualizando los datos de la empresa", error)
      }
    })
    this.changeEditMode()
  }

  changeEditMode(){
    this.isEditMode = !this.isEditMode;
    this.isEditMode ? this.formInfoGeneral.enable() : this.formInfoGeneral.disable();
  }

  cancelarCreacion(){
    this.ngOnInit();
    this.changeEditMode();
  }
}
