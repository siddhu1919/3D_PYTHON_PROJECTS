# Importing Esssential Libraries
from time import sleep
from ursina import *
import random as r
class RotatingCube(Entity):
    def __init__(self):
        super().__init__(
            model='cube',
            color=color.cyan,
            scale=(2, 2, 2),
            position=(0, 0, 0)
        )

    def update(self):
        # Get the mouse position in the viewport
        mouse_x = mouse.x * 2 - 1  # Convert mouse x-coordinate to range -1 to 1
        mouse_y = mouse.y * 2 - 1  # Convert mouse y-coordinate to range -1 to 1

        # Calculate the rotation angles based on mouse position
        rotation_x = mouse_y * 90  # Rotate around x-axis based on mouse y-coordinate
        rotation_y = mouse_x * 90  # Rotate around y-axis based on mouse x-coordinate

        # #Changing cube color 
        # cube.color = color.rgb(r.randint(1,255),r.randint(1,255),r.randint(1,255))

        # Apply the rotation angles to the cube
        self.rotation = (rotation_x, rotation_y, 0)

app = Ursina()

cube = RotatingCube()

app.run()
