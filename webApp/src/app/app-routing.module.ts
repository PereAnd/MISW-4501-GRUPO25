import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginCandidatoComponent } from './core/auth/login-candidato/login-candidato.component';
import { RegCandidatoComponent } from './candidates/components/dashboard-cand/reg-candidato/reg-candidato.component';
import { CreateInfoAcadComponent } from './candidates/components/dashboard-cand/info-academica/create-info-acad/create-info-acad.component';
import { ListInfoAcadComponent } from './candidates/components/dashboard-cand/info-academica/list-info-acad/list-info-acad.component';


const routes: Routes = [
  { path: '', component: LoginCandidatoComponent },
  { path: 'candidato/login', component: LoginCandidatoComponent },
  { path: 'candidato/register', component: RegCandidatoComponent },
  { path: 'candidato/dashboard/:id', component: ListInfoAcadComponent },
  { path: 'candidato/dashboard/:id/list-info-academica', component: ListInfoAcadComponent },
  { path: 'candidato/dashboard/:id/add-info-academica', component: CreateInfoAcadComponent }
]

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
