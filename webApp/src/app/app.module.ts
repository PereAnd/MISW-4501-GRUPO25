import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AngularMaterialModule } from './angular-material/angular-material.module';
import { RegCandidatoComponent } from './core/auth/reg-candidato/reg-candidato.component';
import { LoginCandidatoComponent } from './core/auth/login-candidato/login-candidato.component';

@NgModule({
  declarations: [
    AppComponent,
    RegCandidatoComponent,
    LoginCandidatoComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    AngularMaterialModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
