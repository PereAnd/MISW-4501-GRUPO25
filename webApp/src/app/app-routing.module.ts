import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RegCandidatoComponent } from './candidates/components/reg-candidato/reg-candidato.component';
import { InicioComponent } from './shared/components/inicio/inicio.component';
import { DashboardCandComponent } from './candidates/components/dashboard-cand/dashboard-cand.component';
import { CreateInfoAcadComponent } from './candidates/components/dashboard-cand/info-academica/create-info-acad/create-info-acad.component';
import { InfoAcademicaComponent } from './candidates/components/dashboard-cand/info-academica/info-academica.component';
import { InfoTecnicaComponent } from './candidates/components/dashboard-cand/info-tecnica/info-tecnica.component';
import { CreateInfoTecComponent } from './candidates/components/dashboard-cand/info-tecnica/create-info-tec/create-info-tec.component';
import { InfoPersonalComponent } from './candidates/components/dashboard-cand/info-personal/info-personal.component';
import { InfoLaboralComponent } from './candidates/components/dashboard-cand/info-laboral/info-laboral.component';
import { CreateInfoLaboralComponent } from './candidates/components/dashboard-cand/info-laboral/create-info-laboral/create-info-laboral.component';
import { LoginComponent } from './core/auth/login/login.component';
import { RegEmpresaComponent } from './companies/components/reg-empresa/reg-empresa.component';
import { DashboardEmpComponent } from './companies/components/dashboard-emp/dashboard-emp.component';
import { InfoGeneralComponent } from './companies/components/dashboard-emp/info-general/info-general.component';
import { VerticalesComponent } from './companies/components/dashboard-emp/verticales/verticales.component';
import { CreateVerticalesComponent } from './companies/components/dashboard-emp/verticales/create-verticales/create-verticales.component';
import { UbicacionesComponent } from './companies/components/dashboard-emp/ubicaciones/ubicaciones.component';
import { CreateUbicacionComponent } from './companies/components/dashboard-emp/ubicaciones/create-ubicacion/create-ubicacion.component';
import { ProyectosComponent } from './companies/components/dashboard-emp/proyectos/proyectos.component';
import { CreateProyectoComponent } from './companies/components/dashboard-emp/proyectos/create-proyecto/create-proyecto.component';
import { CreatePerfilComponent } from './companies/components/dashboard-emp/proyectos/perfiles/create-perfil/create-perfil.component';
import { EntrevistasEmpComponent } from './companies/components/dashboard-emp/entrevistas-emp/entrevistas-emp.component';
import { EntrevistasCandComponent } from './candidates/components/dashboard-cand/entrevistas-cand/entrevistas-cand.component';
import { MotorEmpComponent } from './companies/components/dashboard-emp/motor-emp/motor-emp.component';
import { DashboardAbcComponent } from './employees/components/dashboard-abc/dashboard-abc.component';
import { EntrevistasAbcComponent } from './employees/components/dashboard-abc/entrevistas-abc/entrevistas-abc.component';
import { BusquedaCandComponent } from './companies/components/dashboard-emp/busqueda-cand/busqueda-cand.component';

const routes: Routes = [
  { path: '', component: InicioComponent },
  { path: 'login', component: LoginComponent },
  { path: 'candidatos/register', component: RegCandidatoComponent },
  { path: 'candidatos/dashboard/:id', component: DashboardCandComponent,
    children: [
      { path: 'info-personal', component: InfoPersonalComponent },
      { path: 'info-academica', component: InfoAcademicaComponent },
      { path: 'info-academica/add', component: CreateInfoAcadComponent },
      { path: 'info-academica/:idia', component: CreateInfoAcadComponent },
      { path: 'info-tecnica', component: InfoTecnicaComponent },
      { path: 'info-tecnica/add', component: CreateInfoTecComponent },
      { path: 'info-tecnica/:idit', component: CreateInfoTecComponent },
      { path: 'info-laboral', component: InfoLaboralComponent },
      { path: 'info-laboral/add', component: CreateInfoLaboralComponent },
      { path: 'info-laboral/:idil', component: CreateInfoLaboralComponent },
      { path: 'entrevistas-cand', component: EntrevistasCandComponent },
    ]
  },
  { path: 'empresas/register', component: RegEmpresaComponent },
  { path: 'empresas/dashboard/:id', component: DashboardEmpComponent,
    children: [
      { path: 'info-general', component: InfoGeneralComponent },
      { path: 'verticales', component: VerticalesComponent },
      { path: 'verticales/add', component: CreateVerticalesComponent },
      { path: 'verticales/:idv', component: CreateVerticalesComponent },
      { path: 'ubicaciones', component: UbicacionesComponent },
      { path: 'ubicaciones/add', component: CreateUbicacionComponent },
      { path: 'ubicaciones/:idu', component: CreateUbicacionComponent },
      { path: 'proyectos', component: ProyectosComponent },
      { path: 'proyectos/add', component: CreateProyectoComponent },
      { path: 'proyectos/:idp', component: CreateProyectoComponent },
      { path: 'entrevistas-emp', component: EntrevistasEmpComponent },
      { path: 'busqueda-cand', component: BusquedaCandComponent },
      { path: 'motor-emp', component: MotorEmpComponent }
    ]
  }, { path: 'abc/dashboard', component: DashboardAbcComponent,
   children: [
      { path: 'entrevistas-abc', component: EntrevistasAbcComponent }
   ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
