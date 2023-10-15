import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AngularMaterialModule } from './angular-material/angular-material.module';
import { RegCandidatoComponent } from './candidates/components/reg-candidato/reg-candidato.component';
import { LoginCandidatoComponent } from './core/auth/login-candidato/login-candidato.component';
import { RegCandidatoService } from './candidates/services/reg-candidato.service';
import { CandidatesComponent } from './candidates/candidates.component';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { HeaderComponent } from './shared/components/header/header.component';
import { SidebarComponent } from './shared/components/sidebar/sidebar.component';
import { InfoAcademicaComponent } from './candidates/components/info-academica/info-academica.component';
import { CreateInfoAcadComponent } from './candidates/components/info-academica/create-info-acad/create-info-acad.component';
import { ListInfoAcadComponent } from './candidates/components/info-academica/list-info-acad/list-info-acad.component';

@NgModule({
  declarations: [
    AppComponent,
    RegCandidatoComponent,
    LoginCandidatoComponent,
    CandidatesComponent,
    HeaderComponent,
    SidebarComponent,
    InfoAcademicaComponent,
    CreateInfoAcadComponent,
    ListInfoAcadComponent,
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
    RegCandidatoService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
