import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ShopService {
  private _shopsUrl = 'http://localhost:5000/get_shops';
  private _preferredShopsUrl = 'http://localhost:5000/preferred';
  private  _likeShopUrl = 'http://localhost:5000/like';
  private _dislikeShopUrl = 'http://localhost:5000/dislike';

  constructor(private http: HttpClient) { }

  getShops() {
    return this.http.get(this._shopsUrl, {
      headers: new HttpHeaders().append(
        'Authorization', 'JWT ' + localStorage.getItem('token'))
    });
  }

  getPreferredShops() {
    return this.http.get(
      this._preferredShopsUrl, {
        headers: new HttpHeaders().append(
          'Authorization', 'JWT ' + localStorage.getItem('token'))
      }
    );
  }

  likeShop(shop_id) {
    const params = new HttpParams().set('shop_id', shop_id).set('jwt', localStorage.getItem('token'));
    return this.http.get(this._likeShopUrl, {params: params});
  }

  dislikeShop(shop_id) {
    const params = new HttpParams().set('shop_id', shop_id).set('jwt', localStorage.getItem('token'));
    return this.http.get(this._dislikeShopUrl, {params: params});
  }
}



