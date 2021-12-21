class employee:
    a = 10
    b = 7
    c = 12
    @classmethod
    def setattri(cls, a, b, c):
        cls.a = a
        cls.b = b
        cls.c = c
emp = employee()
print(employee.a,employee.b,employee.c)
emp.setattri(1,2,3)
print(employee.a,employee.b,employee.c)        