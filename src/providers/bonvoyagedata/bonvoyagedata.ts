import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs/add/operator/map';


/*
  Generated class for the BonvoyagedataProvider provider.

  See https://angular.io/docs/ts/latest/guide/dependency-injection.html
  for more info on providers and Angular 2 DI.
*/
@Injectable()
export class BonvoyagedataProvider {
 
  constructor(public http: Http) {
    console.log('Hello BonvoyagedataProvider Provider');
  }
 getRemoteData(){
   this.http.get('https://api.myjson.com/bins/w1qto').map(res => res.json()).subscribe(data => {
     console.log(data);
    
   });
  }
}
