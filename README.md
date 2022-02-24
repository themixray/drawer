# drawer
Draw symbols on console like pygame

## What can I do with this library?
For example
1. Buttons in the console (`console.run_moveable_thread()` and track mouse clicks)
2. Simple game
3. and more:)

## Example
```py
from console import console
from drawer import canvas

console.set_title("title")
console.run_moveable_thread()
win = canvas(64,32)

# ground
for x in range(win.width-2):
    win.set(x+1,win.height-1,"‾",False)
    win.set(x+1,0,"_",False)
for y in range(win.height-2):
    win.set(0,y+1,"|",False)
    win.set(win.width-1,y+1,"|",False)

run = True
while run:
    if win.changed:
        win.update()
```
