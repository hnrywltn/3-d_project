# from ursina import *

# app = Ursina()
# cube = Entity(model="cube", color=color.red, texture="white_cube", scale=2)


# def update():
#     cube.rotation_x = cube.rotation_x + 0.25
#     cube.rotation_y = cube.rotation_y + 0.5


#--------------------------------------------------------------------------------
# from ursina import *

# app = Ursina()

# model = load_model('./LadyCat/LadyCat.obj')
# entity = Entity(model=model, texture="./LadyCat/LadyCat.bmp")

# def update():
#     entity.rotation_x = entity.rotation_x + 0.25
#     entity.rotation_y = entity.rotation_y + 0.5

#--------------------------------------------------------------------------------
# from ursina import *

# app = Ursina()
# model = load_model('./LadyCat/LadyCat.obj')
# player = Entity(model=model, texture="./LadyCat/LadyCat.bmp", scale=1)


# def update():
#     player.x += held_keys["d"] * 0.1
#     player.x -= held_keys["a"] * 0.1
#     player.y += held_keys["w"] * 0.1
#     player.y -= held_keys["s"] * 0.1
#     player.rotation_x += held_keys["r"] * 5
#     player.rotation_y += held_keys["e"] * 5




#--------------------------------------------------------------------------------
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

for z in range(10):
    for x in range(10):
        Entity(
            model="cube",
            color=color.pink,

        )


app.run()
