class parent1:
    a = 5
    def __init__(self) -> None:
        print("parent")
class parent2(parent1):
    b = 9
    def __init__(self) -> None:
        print("parent2")
        super().__init__()
class child(parent2):
    c= 10
    def __init__(self) -> None:
        super().__init__()
        print("child")
ch = child()
print(ch.a, ch.b,ch.c)      
