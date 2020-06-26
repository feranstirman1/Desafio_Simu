from tkinter import *
from PIL import Image,ImageTk
import time

#defining some color themes
primaryColor = "#16161a"

buttonBgColor = "#7f5af0"
buttonFgColor = "#fffffe"

#creating the root window
root = Tk()
root.title("Desafio MEF en 3D")
root.minsize(width=1000,height=600)
root.maxsize(width=1000,height=600)
root.resizable(False,False)

#functions to help reuse code
def destroyCurrentAndOpenNewWindow(newWindowName):
    global root
    root.destroy()
    root = Tk()
    root.title(str(newWindowName))
    root.minsize(width=1000,height=600)
    root.maxsize(width=1000,height=600)
    root.resizable(False,False)

#setting the bg image for the home page and the buttons
bgImg = PhotoImage(file="resources/homepage.png")
bgnBtn = PhotoImage(file="resources/beginButton.png")
qtBtn = PhotoImage(file="resources/quitButton.png")

#creating a canvas to draw our items in
mainCanvas = Canvas(root,width=10000,height=600)
mainCanvas.pack()

#creating the items that will go on the canvas
bgImage = mainCanvas.create_image(500,300,image=bgImg)

beginButton = mainCanvas.create_image(-30,370,image=bgnBtn)
quitButton = mainCanvas.create_image(1030,450,image=qtBtn)


#funciones para animar los items dentro del canvas
xspeed = 7
def SlideRight(item,finalCoordinate):
    global mainCanvas
    pos = mainCanvas.coords(item)
    while(pos[0] < finalCoordinate):
        pos = mainCanvas.coords(item)
        mainCanvas.move(item,xspeed,0)
        root.update()
        time.sleep(0.001)
def SlideLeft(item,finalCoordinate):
    global mainCanvas
    pos = mainCanvas.coords(item)
    while(pos[0] > finalCoordinate):
        pos = mainCanvas.coords(item)
        mainCanvas.move(item,-xspeed,0)
        root.update()
        time.sleep(0.001)

#usar las animaciones
SlideRight(beginButton,500)
SlideLeft(quitButton,500)


#adding bindings to the two buttons
def beginApplication(event):
    print("The application has begun")

def closeApplication(event):
    #print("The app has ended")
    root.destroy()

mainCanvas.tag_bind(beginButton,"<Button-1>",beginApplication)
mainCanvas.tag_bind(quitButton,"<Button-1>",closeApplication)


#infinte loop the keep showing our main window
root.mainloop()