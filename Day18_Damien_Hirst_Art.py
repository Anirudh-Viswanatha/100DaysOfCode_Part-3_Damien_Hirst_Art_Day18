# import colorgram
# colors = colorgram.extract("damien-hirst-severed-spots.jpeg", 20)
#
# rgb = []
#
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     color_tuple = (r,g,b)
#     rgb.append(color_tuple)
#
# print(rgb)

from turtle import Turtle,Screen
import turtle # importing turtle module for changing colormode
import random
turtle.colormode(255)

tim = Turtle()
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(350)
tim.setheading(0)
tim.speed("fastest")

# color_list came from above computation using colorgram. Few colors which are close to white shades are manually removed from color_list manually
color_list = [(235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62)]
number_of_dots = 10
number_of_rows = 10

def draw():
    for i in range(number_of_dots):
        random_color = random.choice(color_list)
        tim.dot(20, random_color)
        tim.forward(50)

def reset_draw():
    tim.backward(500)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(0)


for i in range(number_of_rows):
    draw()
    reset_draw()


screenclick = Screen()
screenclick.exitonclick()

# ------------------------------------------------------------------------------------------------

# Alternative method

# from turtle import Turtle,Screen
# import random
#
# turtle.colormode(255)
# tim = Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)
#
# screen = turtle_module.Screen()
# screen.exitonclick()
