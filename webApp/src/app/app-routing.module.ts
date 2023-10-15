import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginCandidatoComponent } from './core/auth/login-candidato/login-candidato.component';
import { RegCandidatoComponent } from './candidates/components/reg-candidato/reg-candidato.component';
import { CreateInfoAcadComponent } from './candidates/components/info-academica/create-info-acad/create-info-acad.component';
import { ListInfoAcadComponent } from './candidates/components/info-academica/list-info-acad/list-info-acad.component';

const routes: Routes = [
  { path: 'candidato/login', component: LoginCandidatoComponent },
  { path: 'candidato/register', component: RegCandidatoComponent },
  { path: 'candidato/:id/add-info-academica', component: CreateInfoAcadComponent },
  { path: 'candidato/:id/list-info-academica', component: ListInfoAcadComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
