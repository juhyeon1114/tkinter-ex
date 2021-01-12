from tkinter import *

root = Tk()
root.title('Hello GUI')
root.geometry('640x480+0+0') # 가로x세로+x좌표+y좌표

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

# set이 없으면 scroll을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode='extended', height=10, yscrollcommand=scrollbar.set)

for i in range(1,32):
    listbox.insert(END, 'day'+str(i))
listbox.pack()

scrollbar.config(command=listbox.yview)

root.mainloop()