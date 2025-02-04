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
# Diagonal Length is ~282.84

SCREEN.tracer(0)

T=tut.Turtle()
T.color("white")
T.penup()
T.hideturtle()

Event = False
lastClick = [0,0]

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


def draw_cross():
    for i in [45,135]:
        T.setheading(i)
        T.forward(40)
        T.pendown()
        T.forward(200)
        T.penup()
        T.backward(240)
        T.setheading(0)
        T.forward(200)
    SCREEN.update()

def draw_naught():
    T.setheading(90)
    T.forward(100)
    T.setheading(0)
    T.forward(100)
    T.forward(70)
    T.setheading(270)
    T.pendown()
    for i in range(0,360,1):
        T.right(1)
        T.forward(1.24)
    T.penup()
    SCREEN.update()

def get_T_pos(pos):
    TPos = [((pos[0]*200)-300),((pos[1]*200)-300)]
    T.goto(TPos[0], TPos[1])

def on_click(x, y):
    global Event
    global lastClick

    SCREEN.onscreenclick(None)
    Event = True
    pos = [x,y]

    for i in range(2):
        x = pos[i]
        if x < -100:
            pos[i] = 0
        elif x < 100:
            pos[i] = 1
        else:
            pos[i] = 2
    
    get_T_pos(pos)
    lastClick = pos

def get_move(playState, board):
    global Event
    success = False
    while not success:
        if playState == "Player":
            Event = False
            SCREEN.onscreenclick(on_click)
            SCREEN.listen()
            while not Event:
                SCREEN.update()
            if board[lastClick[0]][lastClick[1]] == 0:
                board[lastClick[0]][lastClick[1]] = 1
                draw_cross()
                success = True
                playState = "Computer"
        else:
            move = [random.randint(0,2),random.randint(0,2)]
            if board[move[0]][move[1]] == 0:
                get_T_pos(move)
                board[move[0]][move[1]] = 2
                draw_naught()
                success = True
                playState = "Player"
        return board, playState
                








def game_loop():
    board = [[0 for _ in range(3)] for _ in range(3)]
    draw_board()
    turns = ["Player","Computer"]
    playState = turns[random.randint(0,1)]
    while playState in turns:
        print(f"{playState}'s Turn")
        board, playState = get_move(playState, board)









game_loop()



tut.done()