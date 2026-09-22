from common.Enums.Employee_status import EmployeeStatus

class Employee:
    def __init__(self,Id,FirstName,LastName,UserName,Password,EmployeeStatus_Id):
        self.Id = Id
        self.FirstName = FirstName
        self.LastName = LastName
        self.UserName = UserName
        self.Password = Password
        self.EmployeeStatus = EmployeeStatus(EmployeeStatus_Id)


    def Get_full_name(self):
        return f'{self.FirstName} {self.LastName}'
