import colorgram
import turtle as t
from turtle import Screen as s
import random
# colores_rgb = []
#
# colores = colorgram.extract("color.jpg", 20)
#
# for color in colores:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_nuevo = (r, g, b)
#     colores_rgb.append(color_nuevo)
#
# print(colores_rgb)

lista_de_colores = [(203, 34, 66), (71, 116, 151), (228, 161, 193), (150, 184, 70),  (151, 160, 164), (242, 235, 46), (37, 161, 80),
 (35, 31, 32), (137, 205, 187), (240, 99, 54), (75, 65, 40),  (33, 162, 165), (221, 49, 65),  (142, 210, 191),
 (145, 69, 64), (38, 155, 73)]

tim = t.Turtle()
tim.pensize(10)
t.colormode(255)
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
numero_de_puntos = 100

for cuenta_de_puntos in range(1, numero_de_puntos + 1):
    tim.dot(20, random.choice(lista_de_colores))
    tim.forward(50)

    if  cuenta_de_puntos % 10 == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.left(180)

for _ in range(10):
    linea()
    enter()

pantalla = s()
pantalla.exitonclick()