# import colorgram
import random
import turtle
from turtle import Turtle, Screen

# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)

color_list = [(243, 235, 74), (211, 158, 93), (186, 12, 69), (112, 179, 208), (25, 116, 168), (173, 171, 31), (219, 129, 166), (161, 79, 35), (129, 185, 146), (9, 32, 76), (222, 62, 105), (235, 73, 42), (180, 45, 94), (30, 136, 81), (236, 164, 193), (78, 12, 63), (12, 54, 33), (234, 227, 7), (26, 165, 209), (16, 43, 132), (58, 166, 96), (134, 214, 229), (10, 101, 63), (133, 34, 20), (91, 27, 11), (159, 211, 188)]

turtle.colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()

