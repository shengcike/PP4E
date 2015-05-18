from tkinter import *
from Preview.tkinter102 import MyGui

# 应用主窗口
mainwin = Tk()
Label(mainwin, text='__main__').pack()

# 弹出窗口
popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
mainwin.mainloop()