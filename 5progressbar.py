import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('Hello GUI')
root.geometry('640x480+0+0') # 가로x세로+x좌표+y좌표

progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
progressbar.start(10) # 10ms마다 움직임
progressbar.pack()

progressbar2 = ttk.Progressbar(root, maximum=100, mode="determinate")
progressbar2.start(10) # 10ms마다 움직임
progressbar2.pack()

def btncmd():
    progressbar.stop() # 작동 중지
    pass

btn = Button(root, text='stop', command=btncmd)
btn.pack()

p_var = DoubleVar()
progressbar3 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var)
progressbar3.start(10) # 10ms마다 움직임
progressbar3.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01)
        p_var.set(i)
        progressbar3.update()

btn2 = Button(root, text='start', command=btncmd2)
btn2.pack()

root.mainloop()