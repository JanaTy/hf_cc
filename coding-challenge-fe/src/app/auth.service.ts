import { Injectable } from '@angular/core';
import {Headers, Http, RequestOptions } from '@angular/http';
import {HttpClient, HttpHeaders} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private _loginUrl = 'http://localhost:5000/auth';
  constructor(private _http: HttpClient) { }

  getToken(user) {
    return this._http.get(
      this._loginUrl, {
        headers: new HttpHeaders().append('Authorization', 'Basic ' + btoa(user.username + ':' + user.password))
      }
    );
  }

  loggedIn() {
    return !!localStorage.getItem('token');
  }
}
