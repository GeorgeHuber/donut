class Vector:
    def __init__(self, x, y, z) -> None:
        self.pos = (x,y,z)
        self.brightness = 0
        self.distance = None
    def __str__(self):
        return str(self.pos)
    def __repr__(self) -> str:
        return str(self)
    def __getitem__(self,key):
        return self.pos[key]
    def __sub__(self, other):
        return Vector(self.pos[0] - other.pos[0], self.pos[1] - other.pos[1], self.pos[2] - other.pos[2])
    def __add__(self, other):
        new = self.pos + other.pos
        return Vector(self.pos[0] + other.pos[0], self.pos[1] + other.pos[1], self.pos[2] + other.pos[2])
    def __mul__(self, const):
        return Vector(self.pos[0] *const, self.pos[1] *const, self.pos[2] *const)
    def __truediv__(self, const):
        return self*(1/const)
    def __eq__(self, other):
        return self[0]==other[0] and self[1]==other[1] and self[2]==other[2]
    def __hash__(self) -> int:
        return hash(f"{self[0]}{self[1]}{self[2]}")
    def mag(self):
        return (self[0]**2+self[1]**2+self[2]**2)**0.5
    def unit(self):
        return self/self.mag()
    def cross(self,other):
        return Vector(self[1]*other[2] - self[2]*other[1],
         self[2]*other[0] - self[0]*other[2],
         self[0]*other[1] - self[1]*other[0])
    def copy(self):
        return Vector(self[0],self[1],self[2])
    
