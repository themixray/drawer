from console import console
import os, sys

font_size = [8.2,15.5]

class canvas:
    def __init__(self,width,height):
        self.sp = (width*font_size[0],height*font_size[1])
        self.width, self.height = width, height
        self.changed = True
        self.pixels = [[" " for i in range(self.width)] for i in range(self.height)]
        console.set_size(self.sp[0]+30,self.sp[1]+10)
    def clear(self):
        # os.system("cls")
        print("\033[H\033[J",end="")
    def fill(self,symbol=" ",update=True):
        self.pixels = [[symbol for i in range(self.width)] for i in range(self.height)]
        self.changed = True
        if update: self.update()
    def update(self):
        self.changed = False
        out = ""
        for y in self.pixels:
            for x in y:
                out += x
            out += "\n"
        self.clear()
        print(out,end="")
    def set(self,x,y,symbol,update=True):
        if x < self.width and y < self.height:
            self.pixels[y][x] = symbol
            self.changed = True
            if update: self.update()
    def write(self,x,y,text,update=True):
        self.changed = True
        for n,s in enumerate(text):
            self.set(x+n,y,s,False)
        if update: self.update()
    def get(self,x,y):
        return self.pixels[y][x]
    def all(self):
        return self.pixels
    def get_mouse_position(self):
        return (console.get_mouse_position()[0]/self.sp[0]*self.width,
                (console.get_mouse_position()[1]/(self.sp[1]-font_size[1]*4)*self.height))
