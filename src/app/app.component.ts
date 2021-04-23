import { Component } from '@angular/core';
import { SharedService } from './shared.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'KAD';
  logged = false;
  username = '';
  password = '';

  constructor(private sharedService:SharedService){}

  login(){
    this.sharedService.login(this.username,this.password).subscribe(data=>{
      this.logged = true;
    });
  }

  logout(){
    this.logged = false;
  }

}
