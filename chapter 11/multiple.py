class parent1:
    a = 5
class parent2:
    b = 9
class child (parent1,parent2):
    c= 10
ch = child()
print(ch.a, ch.b,ch.c)      
