export interface Employee{
    EmployeeId:number;
    EmployeeName:string;
    Department:string;
    DateOfJoint:string;
}

export interface Department{
    DepartmentId:number;
    DepartmentName:string;
}

export interface AuthToken{
    token:string;
}