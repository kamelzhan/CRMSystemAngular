import { Component, OnInit } from '@angular/core';
import {SharedService} from 'src/app/shared.service';
@Component({
  selector: 'app-show-dep',
  templateUrl: './show-dep.component.html',
  styleUrls: ['./show-dep.component.css']
})
export class ShowDepComponent implements OnInit {

  constructor(private service:SharedService) { 
    this.Title = "";
  }
  DepartmentList:any=[];
  Title:string;
  ActivateDepComp:boolean = false;
  dep:any;
  DepartmentIdFilter:string = "";
  DepartmentNameFilter:string = "";
  DepartmentListFilter:any = [];
  ngOnInit(): void {
    this.refreshDepList();
  }

  edit(item:any){
    this.dep = item;
    this.Title = "Edit Department";
    this.ActivateDepComp = true;
  }

  add(){
    this.dep = {
      DepartmentId:0,
      DepartmentName:""
    }
    this.Title="Add Department";
    this.ActivateDepComp = true;
  }

  delete(item:any){
    if (confirm('Are you sure?')){
      this.service.deleteDepartment(item.DepartmentId).subscribe(data=>{
        alert(data.toString())
        this.refreshDepList();
      });
    }
  }

  close(){
    this.ActivateDepComp = false;
    this.refreshDepList();
  }

  refreshDepList(){
    this.service.getDepList().subscribe(data=> {
      this.DepartmentList = data;
      this.DepartmentListFilter = data;
    });
  }

  filter(){
    var DepartmentIdFilter = this.DepartmentIdFilter;
    var DepartmentNameFilter = this.DepartmentNameFilter;
    this.DepartmentList = this.DepartmentListFilter.filter(function (el:any){
      return el.DepartmentId.toString().toLowerCase().includes(
        DepartmentIdFilter.toString().trim().toLowerCase()
      ) && 
      el.DepartmentName.toString().toLowerCase().includes(
        DepartmentNameFilter.toString().trim().toLowerCase()
      )
    });
  }

}
