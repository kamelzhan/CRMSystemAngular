import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import { AuthToken, Department, Employee } from './models';
@Injectable({
  providedIn: 'root'
})
export class SharedService {
  readonly APIUrl = "http://127.0.0.1:8000";
  readonly PhotoUrl = "http://127.0.0.1:8000/media/";

  constructor(private http:HttpClient) {}

  getDepList():Observable<Department[]>{
    return this.http.get<Department[]>(this.APIUrl + '/department/');
  }
  addDepartment(val:any){
    return this.http.post(this.APIUrl + '/department/', val);
  }
  updateDepartment(val:any){
    return this.http.put(this.APIUrl + '/department/', val);
  }
  deleteDepartment(val:any){
    return this.http.delete(this.APIUrl + '/department/'+ val);
  }

  getEmpList():Observable<Employee[]>{
    return this.http.get<Employee[]>(this.APIUrl + '/employee/');
  }
  addEmployee(val:any){
    return this.http.post(this.APIUrl + '/employee/', val);
  }
  updateEmployee(val:any){
    return this.http.put(this.APIUrl + '/employee/', val);
  }
  deleteEmployee(val:any){
    return this.http.delete(this.APIUrl + '/employee/'+ val);
  }

  UploadPhoto(val:any){
    return this.http.post(this.APIUrl + '/SaveFile', val);
  }

  getAllDepartmentNames():Observable<Department[]>{
    return this.http.get<Department[]>(this.APIUrl + '/department/');
  }

  login(username:any, password:any):Observable<AuthToken[]>{
    return this.http.post<AuthToken[]>(this.APIUrl + '/login/', {
      username:username,
      password:password
    });
  }

}
