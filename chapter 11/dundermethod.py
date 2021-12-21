class employe:
    def __init__(self,a,name) -> None:
           self.a = a
           self.name= name
    def __add__(self,obj):
        return self.a + obj.a

    def __str__(self) -> str:
        return self.name
a = employe(43,"sunny")       
b = employe(23,"sagar")         
print(a,b)