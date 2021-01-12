from tkinter import *

root = Tk()
root.title('Hello GUI')
root.geometry('640x480+0+0') # 가로x세로+x좌표+y좌표

Label(root, text='choose the menus').pack(side='top')

Button(root, text='order').pack(side='bottom')

# 햄버거 프레임
frame_burger = Frame(root, relief='solid', bd=1)
frame_burger.pack(side='left', fill='both', expand=True)

Button(frame_burger, text='hamburger').pack()
Button(frame_burger, text='cheese burger').pack()
Button(frame_burger, text='chicken burger').pack()

# 음료 프레임
frame_drink = LabelFrame(root, relief='solid', bd=1, text='음료')
frame_drink.pack(side='right', fill='both', expand=True)

Button(frame_drink, text='coke').pack()
Button(frame_drink, text='cider').pack()

root.mainloop()