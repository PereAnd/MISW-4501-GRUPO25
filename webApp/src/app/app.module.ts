import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AngularMaterialModule } from './angular-material/angular-material.module';
import { RegCandidatoComponent } from './candidates/components/reg-candidato/reg-candidato.component';
import { RegCandidatoService } from './candidates/services/reg-candidato.service';
import { CandidatesComponent } from './candidates/candidates.component';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { InfoAcademicaComponent } from './candidates/components/dashboard-cand/info-academica/info-academica.component';
import { CreateInfoAcadComponent } from './candidates/components/dashboard-cand/info-academica/create-info-acad/create-info-acad.component';
import { DashboardCandComponent } from './candidates/components/dashboard-cand/dashboard-cand.component';
import { InicioComponent } from './shared/components/inicio/inicio.component';
import { InfoTecnicaComponent } from './candidates/components/dashboard-cand/info-tecnica/info-tecnica.component';
import { CreateInfoTecComponent } from './candidates/components/dashboard-cand/info-tecnica/create-info-tec/create-info-tec.component';
import { InfoPersonalComponent } from './candidates/components/dashboard-cand/info-personal/info-personal.component';
import { InfoLaboralComponent } from './candidates/components/dashboard-cand/info-laboral/info-laboral.component';
import { CreateInfoLaboralComponent } from './candidates/components/dashboard-cand/info-laboral/create-info-laboral/create-info-laboral.component';
import { LoginComponent } from './core/auth/login/login.component';
import { CompaniesComponent } from './companies/companies.component';
import { RegEmpresaComponent } from './companies/components/reg-empresa/reg-empresa.component';
import { DashboardEmpComponent } from './companies/components/dashboard-emp/dashboard-emp.component';
import { InfoGeneralComponent } from './companies/components/dashboard-emp/info-general/info-general.component';
import { VerticalesComponent } from './companies/components/dashboard-emp/verticales/verticales.component';
import { CreateVerticalesComponent } from './companies/components/dashboard-emp/verticales/create-verticales/create-verticales.component';
import { UbicacionesComponent } from './companies/components/dashboard-emp/ubicaciones/ubicaciones.component';
import { CreateUbicacionComponent } from './companies/components/dashboard-emp/ubicaciones/create-ubicacion/create-ubicacion.component';
import { ProyectosComponent } from './companies/components/dashboard-emp/proyectos/proyectos.component';
import { CreateProyectoComponent } from './companies/components/dashboard-emp/proyectos/create-proyecto/create-proyecto.component';
import { DetailProyectoComponent } from './companies/components/dashboard-emp/proyectos/detail-proyecto/detail-proyecto.component';
import { PerfilesComponent } from './companies/components/dashboard-emp/proyectos/perfiles/perfiles.component';
import { DetailPerfilComponent } from './companies/components/dashboard-emp/proyectos/perfiles/detail-perfil/detail-perfil.component';
import { CreatePerfilComponent } from './companies/components/dashboard-emp/proyectos/perfiles/create-perfil/create-perfil.component';
import { CreateCompetenciaComponent } from './companies/components/dashboard-emp/proyectos/perfiles/create-competencia/create-competencia.component';
import { EntrevistasEmpComponent } from './companies/components/dashboard-emp/entrevistas-emp/entrevistas-emp.component';
import { EntrevistasCandComponent } from './candidates/components/dashboard-cand/entrevistas-cand/entrevistas-cand.component';


@NgModule({
  declarations: [
    AppComponent,
    RegCandidatoComponent,
    InicioComponent,
    CandidatesComponent,
    InfoAcademicaComponent,
    CreateInfoAcadComponent,
    DashboardCandComponent,
    InfoTecnicaComponent,
    CreateInfoTecComponent,
    InfoPersonalComponent,
    InfoLaboralComponent,
    CreateInfoLaboralComponent,
    LoginComponent,
    CompaniesComponent,
    RegEmpresaComponent,
    DashboardEmpComponent,
    InfoGeneralComponent,
    VerticalesComponent,
    CreateVerticalesComponent,
    UbicacionesComponent,
    CreateUbicacionComponent,
    ProyectosComponent,
    CreateProyectoComponent,
    DetailProyectoComponent,
    PerfilesComponent,
    DetailPerfilComponent,
    CreatePerfilComponent,
    CreateCompetenciaComponent,
    EntrevistasEmpComponent,
    EntrevistasCandComponent,
  ],
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    AngularMaterialModule
  ],
  providers: [
    RegCandidatoService,
    InicioComponent
  ],
  bootstrap: [AppComponent]

})
export class AppModule { }
