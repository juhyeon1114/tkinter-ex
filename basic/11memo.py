from tkinter import *
import os

root = Tk()
root.title('제목 없음 - Python 메모장')
root.geometry('640x480')

# 열기, 저장 파일 이름
filename = 'mynote.txt'

# menu
def open_file():
    if (os.path.isfile(filename)) :
        with open(filename, 'r', encoding='utf8') as file:
            txt.delete('1.0', END)
            txt.insert(END, file.read())

def save_file():
    with open(filename, 'w', encoding='utf8') as file:
        file.write(txt.get('1.0', END))

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label='open', command=open_file)
menu_file.add_command(label='save', command=save_file)
menu_file.add_separator()
menu_file.add_command(label='exit', command=root.quit)
menu.add_cascade(label='file', menu=menu_file)

root.config(menu=menu)

# scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side='right', fill='y')

# 본문
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(fill='both', expand=True, side='left')
scrollbar.config(command=txt.yview)

root.mainloop()