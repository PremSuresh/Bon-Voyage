import { NgModule } from '@angular/core';
import { HomePage} from './home';
import { IonicPageModule } from 'ionic-angular';
import { BonvoyagedataProvider } from '../providers/bonvoyagedata/bonvoyagedata';


@NgModule({
  declarations: [HomePage],
  imports: [IonicPageModule.forChild(HomePage)],
  entryComponents: [HomePage]
})
export class HomePageModule { }
