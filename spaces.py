import time
import math
import os
import random

from vector import Vector

light_key = ".,o*ODQ0@"

class Space3D:
    def __init__(self, size, scale=0.21, viewport_adjust=4) -> None:
        self.scale = scale
        self.viewport_adjust = viewport_adjust
        self.center = Vector(size//2,size//2,size//2)
        self.view_vector = self.center
        self.light_source = Vector(0,0,0)
        self.size = size
        self.array = set()
    def __len__(self):
        return len(self.array)
    def setLightSource(self, v: Vector):
        self.light_source = v
    def setViewVector(self, v: Vector):
        self.view_vector = v
    def addVector(self, vector: Vector) -> None:
        self.array.add(vector)
    def shade(self):
        for vector in self.array: 
            vector.brightness = int((((self.size*3**0.5-(self.light_source-vector).mag())/(self.size*3**0.5))-.4)/.3*10)
            vector.brightness = int((vector[0]+vector[1]+vector[2])**2/(8*self.size**2)*10)
            if vector.brightness>9:
                vector.brightness=9
            #print(vector.brightness )
    def render(self, with_border = True) -> str:
        output = list((" "*self.size+"\n")*self.size)
        written = {}
        def write(vector:Vector, brightness:int):
            if(vector[0]>=self.size or vector[1]>=self.size or vector[0]<0 or vector[1]<0):
                return
            idx = int(vector[0]) + int(vector[1])*(self.size) + int(vector[1])*1
            distance = (vector-self.view_vector).mag()
            if(str(idx) in written):
                if distance > written[str(idx)]:
                    return
            written[str(idx)] = distance
            output[idx] = light_key[brightness]

        viewport_vector = self.view_vector-self.center
        viewport_point = viewport_vector.unit()*self.viewport_adjust+self.view_vector

        """system of equations in form 
            pv = projection vector
            v = point being projected
            vp = viewport point
            vv = viewport normal vector
            pv0 t + v0 = x, pv1 t + v1 = y, pv2 t + v2 = z
            vv0(x-vp0) + vv1(y-vp1) + vv2(z-vp2) = 0
            expanded:
            vv0(pv0 t + v0-vp0) + vv1(pv1 t + v1-vp1) + vv2(pv2 t + v2-vp2) 
            (vv0 pv0 + vv1 pv1 + vv2 pv2) t = vv0(v0-vp0) + vv1(v1-vp1) + vv2(v2-vp2)
            t = (vv0 pv0 + vv1 pv1 + vv2 pv2)
        """
        for vector in self.array:
            projection_vector = self.view_vector - vector

            (pv0,pv1,pv2) = projection_vector.unit().pos
            (v0,v1,v2) = vector.pos
            (vp0,vp1,vp2) = viewport_point.pos
            (vv0,vv1,vv2) = viewport_vector.unit().pos

            t = -(vv0*(v0-vp0) + vv1*(v1-vp1) + vv2*(v2-vp2))/(vv0 * pv0 + vv1 * pv1 + vv2 * pv2)

            projection_point = Vector(pv0 * t + v0, pv1 * t + v1, pv2 * t + v2)
            
            viewport_conversion = projection_point-viewport_point
            
            base1 = Vector(0,1,0)
            base2 = base1.cross(viewport_vector.unit()).unit()
            
            x =  viewport_conversion[0] / base2[0]  if base2[0]!=0 else viewport_conversion[2]/base2[2]
            y = (viewport_conversion - base2* x)[1]

            projection = Vector(x,y,0)+self.center
            """
            print("base2:",base2)
            print("projection point:",projection_point)
            print("projection: ",projection)
            print("viewpoint",self.view_vector)
            """
            write(projection,vector.brightness)
        return "".join(output)
    def rotate(self,step=0.05,timeStep=0.01, dimensions=3, erase=False):
        t = 0
        while True:
            time.sleep(timeStep)
            if(erase):
                os.system("clear")
            temp = self.view_vector.copy()
            newView = self.view_vector+Vector(1,0,0)*self.size*math.cos(t)*self.scale+Vector(0,0,1)*self.size*math.sin(t)*self.scale
            if(dimensions>=3):
                newView+=Vector(0,1,0)*self.size*math.sin(t)*self.scale
            self.setViewVector(newView)
            print(self.render())
            self.setViewVector(temp)
            t+=step
            