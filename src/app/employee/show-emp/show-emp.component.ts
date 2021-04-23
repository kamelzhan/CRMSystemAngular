import { Component, OnInit } from '@angular/core';
import {SharedService} from 'src/app/shared.service';
@Component({
  selector: 'app-show-emp',
  templateUrl: './show-emp.component.html',
  styleUrls: ['./show-emp.component.css']
})
export class ShowEmpComponent implements OnInit {

  constructor(private service:SharedService) { 
    this.Title = "";
  }
  EmployeeList:any=[];
  Title:string;
  ActivateEmpComp:boolean = false;
  emp:any;
  EmployeeIdFilter:string = "";
  EmployeeNameFilter:string = "";
  EmployeeDepartmentFilter:string = "";
  EmployeeListFilter:any=[];
  ngOnInit(): void {
    this.refreshEmpList();
  }

  edit(item:any){
    this.emp = item;
    this.Title = "Edit Employee";
    this.ActivateEmpComp = true;
  }

  add(){
    this.emp = {
      EmployeeId:0,
      EmployeeName:"",
      Department:"",
      DateOfJoint:"",
      PhotoFileName:"anonymous.png"
    }
    this.Title="Add Employee";
    this.ActivateEmpComp = true;
  }

  delete(item:any){
    if (confirm('Are you sure?')){
      this.service.deleteEmployee(item.EmployeeId).subscribe(data=>{
        alert(data.toString())
        this.refreshEmpList();
      });
    }
  }

  close(){
    this.ActivateEmpComp = false;
    this.refreshEmpList();
  }

  refreshEmpList(){
    this.service.getEmpList().subscribe(data=> {
      this.EmployeeList = data;
      this.EmployeeListFilter = data;
    });
  }

  filter(){
    var EmployeeNameFilter = this.EmployeeNameFilter;
    var EmployeeIdFilter = this.EmployeeIdFilter;
    var EmployeeDepartmentFilter = this.EmployeeDepartmentFilter;
    this.EmployeeList = this.EmployeeListFilter.filter(function (el:any){
      return el.EmployeeId.toString().toLowerCase().includes(
        EmployeeIdFilter.toString().trim().toLowerCase()
      ) && 
      el.EmployeeName.toString().toLowerCase().includes(
        EmployeeNameFilter.toString().trim().toLowerCase()
      ) &&
      el.Department.toString().toLowerCase().includes(
        EmployeeDepartmentFilter.toString().trim().toLowerCase()
      ) 
    });
  }

}
