import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginCandidatoComponent } from './core/auth/login-candidato/login-candidato.component';
import { RegCandidatoComponent } from './candidates/components/reg-candidato/reg-candidato.component';
import { InicioComponent } from './shared/components/inicio/inicio.component';
import { DashboardCandComponent } from './candidates/components/dashboard-cand/dashboard-cand.component';
import { CreateInfoAcadComponent } from './candidates/components/dashboard-cand/info-academica/create-info-acad/create-info-acad.component';
import { InfoAcademicaComponent } from './candidates/components/dashboard-cand/info-academica/info-academica.component';
import { InfoTecnicaComponent } from './candidates/components/dashboard-cand/info-tecnica/info-tecnica.component';
import { CreateInfoTecComponent } from './candidates/components/dashboard-cand/info-tecnica/create-info-tec/create-info-tec.component';
import { InfoPersonalComponent } from './candidates/components/dashboard-cand/info-personal/info-personal.component';

const routes: Routes = [
  { path: '', component: InicioComponent },
  { path: 'candidatos/login', component: LoginCandidatoComponent },
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
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
