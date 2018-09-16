import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { ShopsComponent } from './shops/shops.component';
import { NearbyComponent } from './nearby/nearby.component';
import { LoginComponent } from './login/login.component';
import { Routes, RouterModule} from '@angular/router';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import {AuthService} from './auth.service';
import {ShopService} from './shop.service';
import {AuthGuard} from './auth.guard';

const appRoutes: Routes = [
  {path: 'login', component: LoginComponent},
  {path: 'preferred', component: NearbyComponent, canActivate: [AuthGuard]},
  {path: 'nearby', component: ShopsComponent, canActivate: [AuthGuard]},
  {path: '', redirectTo: '/login', pathMatch: 'full'},
];

@NgModule({
  declarations: [
    AppComponent,
    ShopsComponent,
    NearbyComponent,
    LoginComponent
  ],
  imports: [
    RouterModule.forRoot(
      appRoutes,
      {enableTracing: true}
    ),
    BrowserModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [AuthService, ShopService, AuthGuard],
  bootstrap: [AppComponent]
})
export class AppModule { }
