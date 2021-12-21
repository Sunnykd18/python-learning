class Vector2d:
    def __init__(self,i,j) -> None:
        self.i = i
        self.j = j
    def printvector(self):
         print(f"{self.i}i + {self.j}j")
class vector3d(Vector2d):
    def __init__(self,i,j,k) -> None:
        super().__init__(i,j)
        self.k = k
    def printvector(self):
         print(f"{self.i}i + {self.j}j + {self.k}k")
v2 = Vector2d(1,9)
v3 = vector3d(1,9,16)

v2.printvector()
v3.printvector()
