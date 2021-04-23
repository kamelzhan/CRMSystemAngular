import { Component, OnInit, Input } from '@angular/core';
import {SharedService} from 'src/app/shared.service';
@Component({
  selector: 'app-add-edit-dep',
  templateUrl: './add-edit-dep.component.html',
  styleUrls: ['./add-edit-dep.component.css']
})
export class AddEditDepComponent implements OnInit {

  constructor(private service:SharedService) {
    this.DepId = "";
    this.DepName = "";
   }
  @Input() dep:any;
  DepId:string;
  DepName:string;
  ngOnInit(): void {
    this.DepId = this.dep.DepartmentId;
    this.DepName = this.dep.DepartmentName;
  }

  addDepartment(){
    var val = {DepartmentId:this.DepId,
                DepartmentName:this.DepName}
    this.service.addDepartment(val).subscribe(res=>{
      alert(res.toString());
    });
  }

  updateDepartment(){
    var val = {DepartmentId:this.DepId,
      DepartmentName:this.DepName}
    this.service.updateDepartment(val).subscribe(res=>{
      alert(res.toString());
    });
  }

}
