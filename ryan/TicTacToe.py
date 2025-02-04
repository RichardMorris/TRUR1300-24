import random
import turtle as tut
import time


# Global
SCREEN = tut.Screen()

# Screen Setup
SCREEN.title("Tic Tac Toe")
SCREEN.bgcolor("black")
SCREEN.setup(width=600, height=600)
# 0-200, 200-400, 400-600 are the box co ords
#SCREEN.tracer(0)

T=tut.Turtle()
T.color("white")
T.penup()


def draw_board_line(direction, length):
    T.pendown()
    T.setheading(direction)
    T.forward(length)
    T.penup()



# Draw the board
def draw_board():
    T.clear()
    T.speed(0)
    for i in range(-100,101,200):
        T.goto(i,-300)
        draw_board_line(90,600)
        T.goto(-300,i)
        draw_board_line(0,600)
        print(i)
    SCREEN.update()





draw_board()
tut.done()