from ursina import *
import random as r 

app = Ursina() #ursina object

class rotating_cube(Entity):
    def __init__(self):
        super().__init__(
            model="Cube",
            color = color.red,
            scale = 1.5,
            position = (0,0,0),
            texture = color.white
            )
    def update(self):
        self.rotation_x += 2
        self.rotation_y += 2
        self.rotation_z += 2

cube = rotating_cube()

app.run()