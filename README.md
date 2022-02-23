# drawer
Draw symbols on console like pygame

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
