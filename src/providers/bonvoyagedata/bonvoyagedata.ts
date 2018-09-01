import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs/add/operator/map';

declare var count;
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
    var d = new Date();
    console.log(d);

  this.http.get('https://api.myjson.com/bins/1gx21o').map(res => res.json()).subscribe(data => {
  var alarm;
  alarm = data[0].alarm;
   console.log(data[0].alarm);
   if(alarm==1)
   {
     console.log('alarm deployed')
     var audio = new Audio("assets/audio/alarm.wav");
    audio.play();
   }
 });
}
   /*this.http.get('https://api.myjson.com/bins/ph58c').map(res => res.json()).subscribe(data => {
     console.log(data);
   
   });
    */
  }

