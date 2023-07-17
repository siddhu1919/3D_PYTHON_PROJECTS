from turtle import position
from ursina import *
import random as r

app = Ursina()

#Friend List for Randomly Showing Names
friend = ["Sid","Abhinandan-Bhaiya","Vivek","Vinit","Saubhagya","Abhas"]

cube = Entity(model="cube",
              color = color.green,
              scale=2,
              position=(0,0,0)
              )
txt = Text(text="3D Rotating Cube",
           color=color.white,
           scale = 2,
           position = (-0.2,0.4)
           )
def update():
    #Code for moving the cube in the Cursor Direction

    # cube.x =  mouse.x   # Convert mouse x-coordinate to range -1 to 1
    # cube.y =  mouse.y   # Convert mouse y-coordinate to range -1 to 1
    # cube.z =  mouse.z   # Convert mouse y-coordinate to range -1 to 1

    # Code For Above Task and Changing
    cube.position = mouse.position
    cube.rotation_x += 2
    cube.rotation_y += 2
    cube.rotation_z += 2

        
    

app.run()