from ursina import *
app = Ursina()
camera = EditorCamera()
cube = Entity(
    model="sphere",
    color = color.white,
    scale = 1.7,
    position = 0
    )
def update():
    # Adjust camera movement speed
    speed = 5

    # Check for key presses and move the camera accordingly
    if held_keys['w']:
        camera.position += camera.forward * speed * time.dt
    if held_keys['s']:
        camera.position -= camera.forward * speed * time.dt
    if held_keys['a']:
        camera.position -= camera.right * speed * time.dt
    if held_keys['d']:
        camera.position += camera.right * speed * time.dt
    
app.run()