import { Component, OnInit } from '@angular/core';
import { ShopService } from '../shop.service';

@Component({
  selector: 'app-nearby',
  templateUrl: './nearby.component.html',
  styleUrls: ['./nearby.component.css']
})
export class NearbyComponent implements OnInit {

  preferredShops: any = [];

  constructor(private _shopService: ShopService) { }

  ngOnInit() {
    this.getPreferredshop();
  }

  getPreferredshop() {
    this._shopService.getPreferredShops().subscribe(
      res => this.preferredShops = res,
      err => console.log(err)
    );
  }

  dislikeShop(shop_id) {
    this._shopService.dislikeShop(shop_id).subscribe(
      res => this.preferredShops = res,
      err => console.log(err));
  }
}


