from tkinter import colorchooser,Tk
from drawer import color_symbol
from colored import fg,bg,attr
from console import console
from drawer import canvas
import colorama
import mouse
import time

# -------   create canvas   -------

console.set_title("painting")  # set console title
console.run_moveable_thread()  # run thread that prohibits clicking on the console
win = canvas(64,34)            # creating canvas


# -------   create main view   -------

def reload():
    win.fill(" ",False)
    for x in range(62):
        win.set(x+1,31,"—",False)
        win.set(x+1,0,"_",False)
    for y in range(30):
        win.set(0,y+1,"|",False)
        win.set(63,y+1,"|",False)
    for y in range(29):
        for x in range(62):
            win.set(x+1,y+1," ",False)
    for i in btns:
        win.set(i[1],i[2],i[0][0],False)
        win.write(i[1]+1,i[2],i[0][1:][:-1],False)
        win.set(i[1]+len(i[0])-1,i[2],i[0][-1],False)
    win.update()


# -------   create buttons   -------

btns = []
def btn(text,x,y,cb):
    btns.append(["["+text.upper()+"]",x,y+32,cb,False])

btn("CLEAR",1,1,reload)

color = "white"

def choose_color():
    global color
    Tk().withdraw()
    color = colorchooser.askcolor(title="Choose color")[1]

btn("CHOOSE COLOR",10,1,choose_color)


# -------   main loop   -------

reload()

run = True
while run:
    if win.changed:
        win.update()
    if console.is_focus():
        pos = win.get_mouse_position()
        pos = (round(pos[0]),round(pos[1]))
        if mouse.is_pressed("left"):
            if pos[0] > 1 and pos[1] > 0 and pos[0] < 63 and pos[1] < 31:
                win.set(pos[0],pos[1],color_symbol(color))
            for i in btns:
                if pos[0] >= i[1] and pos[0] <= i[1]+len(i[0]) \
                            and pos[1] == i[2]+1 and not i[4]:
                    win.set(i[1],i[2],fg("black")+bg("white")+i[0][0],False)
                    win.write(i[1]+1,i[2],i[0][1:][:-1],False)
                    win.set(i[1]+len(i[0])-1,i[2],i[0][-1]+attr("reset"),False)
                    i[4] = True
        elif mouse.is_pressed("right"):
            win.set(pos[0],pos[1]," ")
        else:
            for i in btns:
                if i[4]:
                    win.set(i[1],i[2],i[0][0],False)
                    win.write(i[1]+1,i[2],i[0][1:][:-1],False)
                    win.set(i[1]+len(i[0])-1,i[2],i[0][-1],False)
                    i[4] = False
                    i[3]()
