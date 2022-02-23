from console import console
from drawer import canvas
import colorama
import mouse

console.set_title("painting")
console.run_moveable_thread()
win = canvas(64,34)

def clear():
    win.fill()
    for x in range(win.width-2):
        win.set(x+1,31,"‾",False)
        win.set(x+1,0,"_",False)
    for y in range(30):
        win.set(0,y+1,"|",False)
        win.set(win.width-1,y+1,"|",False)
    win.write(29,33,"[CLEAR]",False)
    win.update()
clear()

cop = False

run = True
while run:
    if win.changed:
        win.update()
    if console.is_focus():
        pos = win.get_mouse_position()
        pos = (int(pos[0]),int(pos[1]))
        if mouse.is_pressed("left"):
            if pos[0]>1and pos[1]>0and pos[0]<63and pos[1]<31:
                win.set(pos[0],pos[1],"#")
            elif pos[0]>27and pos[0]<35and pos[1]==34:
                win.write(29,33,colorama.Back.WHITE+\
                          colorama.Fore.BLACK+"[CLEAR]"+\
                          colorama.Style.RESET_ALL,True)
                cop = True
        elif mouse.is_pressed("right"):
            win.set(pos[0],pos[1]," ")
        elif cop:
            clear()
            cop = False
