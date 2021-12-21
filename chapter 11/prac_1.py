class Employee:
    def __init__(self,salary,increment) -> None:
         self.salary = salary
         self.increment = increment
    @property
    def salaryafterincrement(self):
        return self.salary * (1+self.increment)
    @salaryafterincrement.setter
    def salaryafterincrement(self):
        self.salary = self.salary * (1+self.increment)

emp = Employee(10000, 0.1)
print(emp.salaryafterincrement)
emp.salaryafterincrement = 11000