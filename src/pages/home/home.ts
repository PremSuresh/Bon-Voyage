import { Component, ViewChild, ElementRef, assertPlatform } from '@angular/core';
import { IonicPage } from 'ionic-angular';
import { NavController } from 'ionic-angular';
import { BonvoyagedataProvider } from '../../providers/bonvoyagedata/bonvoyagedata';
import { Http, Headers } from '@angular/http';
import 'rxjs/add/operator/map';
import { stringify } from '../../../node_modules/@angular/core/src/util';

declare var google;

@IonicPage()
@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  
  @ViewChild('map') mapElement: ElementRef;
  @ViewChild('directionsPanel') directionsPanel: ElementRef;
  map: any;
  start = 'chicago, il';
  end = 'chicago, il';
  directionsService = new google.maps.DirectionsService;
  directionsDisplay = new google.maps.DirectionsRenderer;


  
  constructor(public navCtrl: NavController,public bonvoyageService: BonvoyagedataProvider,public http: Http) {
    
  }
  




  btnClicked(){
    let headers = new Headers();
    headers.append('Content-Type','application/json');
    let parameters =[{
          "drowsybutton": 1,
          "alarm": 0,
      "accident": 0,
      "sos": 0
        }]
    this.http.put('https://api.myjson.com/bins/ph58c',JSON.stringify(parameters),{headers: headers})
    .map(res => res.json())
    .subscribe(data => {
      console.log(data);
    });
    alert("Drowsiness Detection activated");
  }
  btnClicked1(){
    let headers = new Headers();
    headers.append('Content-Type','application/json');
    let body = [{
      "drowsybutton": 0,
      "alarm": 0,
  "accident": 0,
  "sos": 1
    }]
    this.http.put('https://api.myjson.com/bins/ph58c',JSON.stringify(body),{headers: headers})
    .map(res => res.json())
    .subscribe(data => {
      console.log(data);
    });
    alert("your soul is being saved");
  }

  ionViewDidLoad(){
    this.bonvoyageService.getRemoteData();
    this.initMap();
    this.loadMap();
        this.startNavigating();
  }
  
  loadMap(){
 
    let latLng = new google.maps.LatLng(13.0500, 80.282);

    let mapOptions = {
      center: latLng,
      zoom: 15,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    }

    this.map = new google.maps.Map(this.mapElement.nativeElement, mapOptions);

  }

  startNavigating(){
 
  let directionsService = new google.maps.DirectionsService;
  let directionsDisplay = new google.maps.DirectionsRenderer;

  directionsDisplay.setMap(this.map);
  directionsDisplay.setPanel(this.directionsPanel.nativeElement);

  directionsService.route({
      origin: 'ssn college of engineering',
      destination: 'marina beach',
      travelMode: google.maps.TravelMode['DRIVING']
  }, (res, status) => {

      if(status == google.maps.DirectionsStatus.OK){
          directionsDisplay.setDirections(res);
      } else {
          console.warn(status);
      }

  })
}
  

  initMap() {
    this.map = new google.maps.Map(this.mapElement.nativeElement, {
      zoom: 7,
      center: {lat: 41.85, lng: -87.65}
    }
  
  );

    this.directionsDisplay.setMap(this.map);
  }

  calculateAndDisplayRoute() {
    this.directionsService.route({
      origin: this.start,
      destination: this.end,
      travelMode: 'DRIVING'
    }, (response, status) => {
      if (status === 'OK') {
        this.directionsDisplay.setDirections(response);
      } else {
        window.alert('Directions request failed due to ' + status);
      }
    });
  }


 
}
