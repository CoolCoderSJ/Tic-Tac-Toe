import basic_graphics
import time
from tkinter import *


def init(data):
    data.grid = [[False, False, False],[False, False, False],[False, False, False]]
    data.cols = 3
    data.rows = 3
    data.cellwidth = data.width/data.cols
    data.cellheight = data.height/data.rows
    data.XOlocations = {(0, 0): [data.cellwidth/2, data.cellheight/2],
                        (0, 1): [data.cellwidth/2 + data.cellwidth, data.cellheight/2],
                        (0, 2): [data.cellwidth/2 + data.cellwidth*2, data.cellheight/2],
                        (1, 0): [data.cellwidth/2, data.cellheight/2 + data.cellheight],
                        (1, 1): [data.cellwidth/2 + data.cellwidth, data.cellheight/2 + data.cellheight],
                        (1, 2): [data.cellwidth/2 + data.cellwidth*2, data.cellheight/2 + data.cellheight],
                        (2, 0): [data.cellwidth/2, data.cellheight/2 + data.cellheight*2],
                        (2, 1): [data.cellwidth/2 + data.cellwidth, data.cellheight/2 + data.cellheight*2],
                        (2, 2): [data.cellwidth/2 + data.cellwidth*2, data.cellheight/2 + data.cellheight*2]}
    data.pcount = 0
    data.squares = [[False, False, True],[True, True, False],[False, True, True]]


    
def mousePressed(canvas, event, data):
    (i, j) = getSquare(event.x, event.y, data)
    data.pcount += 1
    modnum = data.pcount % 2
    placeXOdet(canvas, i, j, data, modnum)
    isaWin(canvas, data)
    

def getSquare(ex, ey, data):
    j = ex //data.cellwidth
    i = ey //data.cellheight
    return int(i), int(j)

def placeXOdet(canvas, i, j, data, modnum):
    if modnum == 1:
        canvas.create_text(data.XOlocations[(i, j)][0], data.XOlocations[(i, j)][1], text = "X", fill="black", font="Monaco 25 bold")
        data.squares[i][j] = "X"
    else:
        canvas.create_text(data.XOlocations[(i, j)][0], data.XOlocations[(i, j)][1], text = "O", fill="black", font="Monaco 25 bold")
        data.squares[i][j] = "O"

def isaWin(canvas, data):
    if data.squares[0][0] == data.squares[0][1] == data.squares[0][2]:
        canvas.create_line(int(data.XOlocations[(0, 0)][0]), int(data.XOlocations[(0, 0)][1]), int(data.XOlocations[(0, 2)][0]), int(data.XOlocations[(0, 2)][1]), width = 5)
        canvas.update()
        time.sleep(3)
        winvar = data.squares[0][0]
        canvas.delete(ALL)
        canvas.create_text(data.width/2, data.height/2, text = "Congratulations! " + str(winvar) + " Won!")

    elif data.squares[1][0] == data.squares[1][1] == data.squares[1][2]:
        canvas.create_line(int(data.XOlocations[(1, 0)][0]), int(data.XOlocations[(1, 0)][1]), int(data.XOlocations[(1, 2)][0]), int(data.XOlocations[(1, 2)][1]), width = 5)
        canvas.update()
        time.sleep(3)
        winvar = data.squares[1][0]
        canvas.delete(ALL)
        canvas.create_text(data.width/2, data.height/2, text = "Congratulations! " + str(winvar) + " Won!")

    elif data.squares[0][0] == data.squares[1][0] == data.squares[2][0]:
        canvas.create_line(int(data.XOlocations[(0, 0)][0]), int(data.XOlocations[(0, 0)][1]), int(data.XOlocations[(2, 0)][0]), int(data.XOlocations[(2, 0)][1]), width = 5)
        canvas.update()
        time.sleep(3)
        winvar = data.squares[0][0]
        canvas.delete(ALL)
        canvas.create_text(data.width/2, data.height/2, text = "Congratulations! " + str(winvar) + " Won!")

    elif data.squares[0][1] == data.squares[1][1] == data.squares[2][1]:
        canvas.create_line(int(data.XOlocations[(0, 1)][0]), int(data.XOlocations[(0, 1)][1]), int(data.XOlocations[(2, 1)][0]), int(data.XOlocations[(2, 1)][1]), width = 5)
        canvas.update()
        time.sleep(3)
        winvar = data.squares[0][1]
        canvas.delete(ALL)
        canvas.create_text(data.width/2, data.height/2, text = "Congratulations! " + str(winvar) + " Won!")

    elif data.squares[0][2] == data.squares[1][2] == data.squares[2][2]:
        canvas.create_line(int(data.XOlocations[(0, 2)][0]), int(data.XOlocations[(0, 2)][1]), int(data.XOlocations[(2, 2)][0]), int(data.XOlocations[(2, 2)][1]), width = 5)
        canvas.update()
        time.sleep(3)
        winvar = data.squares[0][2]
        canvas.delete(ALL)
        canvas.create_text(data.width/2, data.height/2, text = "Congratulations! " + str(winvar) + " Won!")

    elif data.squares[0][0] == data.squares[1][1] == data.squares[2][2]:
        canvas.create_line(int(data.XOlocations[(0, 0)][0]), int(data.XOlocations[(0, 0)][1]), int(data.XOlocations[(2, 2)][0]), int(data.XOlocations[(2, 2)][1]), width = 5)
        canvas.update()
        time.sleep(3)
        winvar = data.squares[0][0]
        canvas.delete(ALL)
        canvas.create_text(data.width/2, data.height/2, text = "Congratulations! " + str(winvar) + " Won!")

    elif data.squares[0][2] == data.squares[1][1] == data.squares[2][0]:
        canvas.create_line(int(data.XOlocations[(0, 2)][0]), int(data.XOlocations[(0, 2)][1]), int(data.XOlocations[(2, 0)][0]), int(data.XOlocations[(2, 0)][1]), width = 5)
        canvas.update()
        time.sleep(3)
        winvar = data.squares[0][2]
        canvas.delete(ALL)
        canvas.create_text(data.width/2, data.height/2, text = "Congratulations! " + str(winvar) + " Won!")




def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    drawGrid(canvas, data)
    

def drawGrid(canvas, data):
    for i in range(0, len(data.grid)):
        for j in range(len(data.grid[i])):
            canvas.create_rectangle(data.cellwidth*j, data.cellheight*i, (j+1)*data.cellwidth, (i+1)*data.cellheight)
    






def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(canvas, event, data)
        #redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 99999999999999 # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(400, 400)
