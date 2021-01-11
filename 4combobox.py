import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('Hello GUI')
root.geometry('640x480+0+0') # 가로x세로+x좌표+y좌표

values = [str(i) + '일' for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set('카드 결제일') # 최초 목록의 제목

readonly_combobox = ttk.Combobox(root, height=10, values=values)
readonly_combobox.pack()
readonly_combobox.current(0) # 최초 목록의 제목

def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()