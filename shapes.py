import math
from vector import Vector
from spaces import Space3D

def drawCube(CubeSpace: Space3D, size:int):
    CubeSpace.view_vector+=Vector(0,0,0)

    x1 = int(size/2)-size//8
    x2 = int(size/2)+size//8
    y1 = int(size/2)-size//12
    y2 = int(size/2)+size//12
    z1 = int(size/2)-size//8
    z2 = int(size/2)+size//8

    for i in range(x1,x2):
        for j in range(y1,y2):
            for k in range(z1,z2):
                if sum([i==x1, i==x2-1, j==y1, j==y2-1, k==z1, k==z2-1])>=2:
                    CubeSpace.addVector(Vector(i,j,k))


    #CubeSpace.addVector(CubeSpace.center)

    corners = ()
    for i in corners:
        for j in corners:
            for k in corners:
                CubeSpace.addVector(Vector(i,j,k))

def drawDonut(DonutSpace: Space3D, size:int):
    radius = 8
    a = 2
    for i in range (0,int(2*math.pi*100)):
        u = i/100
        for j in range(0,int(2*math.pi*100)):
            v = j/100
            x = int((radius+a*math.cos(v))*math.cos(u))
            y = int((radius+a*math.cos(v))*math.sin(u))
            z = int(a*math.sin(v))
            donut_point = Vector(x,y,z)+DonutSpace.center
            DonutSpace.addVector(donut_point)
            