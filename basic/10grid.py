from tkinter import *

root = Tk()
root.title('Hello GUI')
root.geometry('640x480+0+0') # 가로x세로+x좌표+y좌표

PAD_X = 10
PAD_Y = 10
GRID_PAD_X = 3
GRID_PAD_Y = 3
WIDTH = 5
HEIGHT = 2

# 맨 윗줄
btn_clear = Button(root, text='clear', width=WIDTH, height=HEIGHT)
btn_equal = Button(root, text='=', width=WIDTH, height=HEIGHT)
btn_slash = Button(root, text='/', width=WIDTH, height=HEIGHT)
btn_star = Button(root, text='*', width=WIDTH, height=HEIGHT)
btn_clear.grid(row=0, column=0, sticky=N+E+W+S, padx=GRID_PAD_X, pady=GRID_PAD_Y) #stick : 지정한 방향으로 늘려라
btn_equal.grid(row=0, column=1, sticky=N+E+W+S, padx=GRID_PAD_X, pady=GRID_PAD_Y)
btn_slash.grid(row=0, column=2, sticky=N+E+W+S, padx=GRID_PAD_X, pady=GRID_PAD_Y)
btn_star.grid(row=0, column=3, sticky=N+E+W+S, padx=GRID_PAD_X, pady=GRID_PAD_Y)

# 두번째 줄
btn_seven = Button(root, text='7', width=WIDTH, height=HEIGHT)
btn_eight = Button(root, text='8', width=WIDTH, height=HEIGHT)
btn_nine = Button(root, text='9', width=WIDTH, height=HEIGHT)
btn_minus = Button(root, text='-', width=WIDTH, height=HEIGHT)
btn_seven.grid(row=1, column=0, sticky=N+E+W+S, padx=GRID_PAD_X, pady=GRID_PAD_Y)
btn_eight.grid(row=1, column=1, sticky=N+E+W+S, padx=GRID_PAD_X, pady=GRID_PAD_Y)
btn_nine.grid(row=1, column=2, sticky=N+E+W+S, padx=GRID_PAD_X, pady=GRID_PAD_Y)
btn_minus.grid(row=1, column=3, sticky=N+E+W+S, padx=GRID_PAD_X, pady=GRID_PAD_Y)

# 세번째 줄
btn_four = Button(root, text='4', width=WIDTH, height=HEIGHT)
btn_five = Button(root, text='5', width=WIDTH, height=HEIGHT)
btn_six = Button(root, text='6', width=WIDTH, height=HEIGHT)
btn_plus = Button(root, text='+', width=WIDTH, height=HEIGHT)
btn_four.grid(row=2, column=0, sticky=N+E+W+S, padx=GRID_PAD_X, pady=GRID_PAD_Y)
btn_five.grid(row=2, column=1, sticky=N+E+W+S, padx=GRID_PAD_X, pady=GRID_PAD_Y)
btn_six.grid(row=2, column=2, sticky=N+E+W+S, padx=GRID_PAD_X, pady=GRID_PAD_Y)
btn_plus.grid(row=2, column=3, sticky=N+E+W+S, padx=GRID_PAD_X, pady=GRID_PAD_Y)

# 네번째 줄
btn_one = Button(root, text='1', width=WIDTH, height=HEIGHT)
btn_two = Button(root, text='2', width=WIDTH, height=HEIGHT)
btn_three = Button(root, text='3', width=WIDTH, height=HEIGHT)
btn_plus = Button(root, text='enter', width=WIDTH, height=HEIGHT)
btn_one.grid(row=3, column=0, sticky=N+E+W+S, padx=GRID_PAD_X, pady=GRID_PAD_Y)
btn_two.grid(row=3, column=1, sticky=N+E+W+S, padx=GRID_PAD_X, pady=GRID_PAD_Y)
btn_three.grid(row=3, column=2, sticky=N+E+W+S, padx=GRID_PAD_X, pady=GRID_PAD_Y)
btn_plus.grid(row=3, column=3, rowspan=2, sticky=N+E+W+S, padx=GRID_PAD_X, pady=GRID_PAD_Y)

# 다섯째 줄
btn_zero = Button(root, text='0', padx=GRID_PAD_X, pady=GRID_PAD_Y)
btn_dot = Button(root, text='.', padx=GRID_PAD_X, pady=GRID_PAD_Y)
btn_zero.grid(row=4, column=0, columnspan=2, sticky=N+E+W+S, padx=GRID_PAD_X, pady=GRID_PAD_Y)
btn_dot.grid(row=4, column=2, sticky=N+E+W+S, padx=GRID_PAD_X, pady=GRID_PAD_Y)

root.mainloop()