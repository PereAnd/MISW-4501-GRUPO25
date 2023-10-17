import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginCandidatoComponent } from './core/auth/login-candidato/login-candidato.component';
import { RegCandidatoComponent } from './candidates/components/reg-candidato/reg-candidato.component';
import { InicioComponent } from './shared/components/inicio/inicio.component';
import { DashboardCandComponent } from './candidates/components/dashboard-cand/dashboard-cand.component';
import { CreateInfoAcadComponent } from './candidates/components/dashboard-cand/info-academica/create-info-acad/create-info-acad.component';
import { ListInfoAcadComponent } from './candidates/components/dashboard-cand/info-academica/list-info-acad/list-info-acad.component';

const routes: Routes = [
  { path: '', component: InicioComponent },
  { path: 'candidatos/login', component: LoginCandidatoComponent },
  { path: 'candidatos/register', component: RegCandidatoComponent },
  { path: 'candidatos/dashboard/:id', component: DashboardCandComponent,
    children: [
      { path: 'info-academica', component: ListInfoAcadComponent },
      { path: 'add-info-academica/:idia', component: CreateInfoAcadComponent }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
