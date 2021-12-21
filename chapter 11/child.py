class employee:   # example of an single inheritance
    a = 12

class programmer(employee):
    b = 13

pr = programmer()
print(pr.a)
print(pr.b)        

em = employee()
# print(em.b) this will show error as it is parent class
print(em.a)
