import win32console
import threading
import win32gui
import win32api
import atexit
import os

class console:
    def __init__(self):
        self._is_enabled = False
        self.hwnd = win32console.GetConsoleWindow()
        atexit.register(lambda:self.set_input(True))
    def _mouse_thread(self):
        while True:
            if self.get_mouse_position()[1] > 30:
                if self.is_input():
                    self._set_input(False)
            else:
                if not self.is_input():
                    self._set_input(True)
    def run_moveable_thread(self):
        threading.Thread(target=self._mouse_thread,daemon=1).start()
    def get_position(self):
        return win32gui.GetWindowRect(self.hwnd)[:2]
    def get_mouse_position(self):
        pos = win32gui.GetCursorPos()
        return (pos[0]-self.get_position()[0]-7,
                pos[1]-self.get_position()[1]-30)
    def _set_input(self,value):
        win32gui.EnableWindow(self.hwnd,value)
    def set_input(self,value):
        self._is_enabled = value
        win32gui.EnableWindow(self.hwnd,value)
    def is_input(self):
        return win32gui.IsWindowEnabled(self.hwnd)
    def is_focus(self):
        return win32gui.GetForegroundWindow() == self.hwnd and \
               self.get_mouse_position()[1] >= 30 and \
               self.get_mouse_position()[0] > 0 and \
               self.get_mouse_position()[0] <= self.get_size()[0] and \
               self.get_mouse_position()[1] <= self.get_size()[1]
    def get_size(self):
        return (win32gui.GetWindowRect(self.hwnd)[2]-7,
                win32gui.GetWindowRect(self.hwnd)[3]-30)
    def set_size(self,w,h):
        win32gui.MoveWindow(self.hwnd,*self.get_position(),int(w),int(h),True)
    def set_position(self,x,y):
        win32gui.MoveWindow(self.hwnd,int(x),int(y),*self.get_size(),True)
    def set_rect(self,x,y,w,h):
        win32gui.MoveWindow(self.hwnd,int(x),int(y),int(w),int(h),True)
    def set_center(self):
        self.set_position(get_screen_size()[0]/2-self.get_size()[0]/2,
                          get_screen_size()[1]/2-self.get_size()[1]/2)
    def set_title(self,title):
        win32gui.SetWindowText(self.hwnd,title)
console = console()

def get_screen_size():
    return (win32api.GetSystemMetrics(0),
            win32api.GetSystemMetrics(1))
