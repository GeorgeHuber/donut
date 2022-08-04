import os

from spaces import Space3D
import shapes

os.system("clear")

size = 40


DonutSpace = Space3D(size,1.1,90)
shapes.drawDonut(DonutSpace, size)
DonutSpace.shade()
DonutSpace.rotate(dimensions=3, timeStep=0.02)


