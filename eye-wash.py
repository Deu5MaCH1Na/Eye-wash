from win32gui import *
from win32con import *
from win32api import *
import time
def foo(hwnd, mouse):
    if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd) :
        if !('write here.' in GetClassName(hwnd)):     #在此处填入白名单类名(即不隐藏)
            alpha =40                                  #透明度
            h=hwnd
            GetWindowLong(h, GWL_EXSTYLE)
            SetWindowLong(h, GWL_EXSTYLE, WS_EX_LAYERED)
            try:
                SetLayeredWindowAttributes(h, 0, alpha, LWA_ALPHA) #设置半透明
            except:
                pass
           
c=FindWindow('Shell_TrayWnd',None)
ShowWindow(c,SW_SHOW)
while(1):
    EnumWindows(foo, 0)
    time.sleep(1)
