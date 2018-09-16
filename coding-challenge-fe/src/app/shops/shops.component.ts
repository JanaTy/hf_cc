import { Component, OnInit } from '@angular/core';
import { ShopService } from '../shop.service';

@Component({
  selector: 'app-shops',
  templateUrl: './shops.component.html',
  styleUrls: ['./shops.component.css']
})
export class ShopsComponent implements OnInit {

  shops: any = [];
  constructor(private _shopService: ShopService) { }

  ngOnInit() {
    this.getShop();
  }

  getShop() {
    this._shopService.getShops().subscribe(
      res => this.shops = res,
      err => console.log(err)
    );
  }

  likeShop(shop_id) {
    this._shopService.likeShop(shop_id).subscribe(
      res => console.log(res),
      err => console.log(err)
    );
    this._shopService.getShops();
  }

}
