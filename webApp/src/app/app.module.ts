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
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    RegCandidatoComponent,
    LoginCandidatoComponent,
    CandidatesComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
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
