class Myclass:
  a = 9

obj = Myclass()
print(obj.a)
obj.a = 0 # i am setting an instance attribute by doing this!
print(obj.a)
print(Myclass.a)