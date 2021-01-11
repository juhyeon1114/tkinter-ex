from tkinter import *

root = Tk()
root.title('Hello GUI')
root.geometry('640x480+0+0') # 가로x세로+x좌표+y좌표

def create_new_file():
    print('새 파일 생성')

def create_new_window():
    print('새 창 생성')

menu = Menu(root)

# File menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label='New File', command=create_new_file)
menu_file.add_command(label='New Window', command=create_new_window)
menu_file.add_separator()
menu_file.add_command(label='Open File...')
menu_file.add_command(label='Save All', state='disable') # 비 활성화
menu_file.add_command(label='Exit', command=root.quit)
menu.add_cascade(label='File', menu=menu_file)

# Edit menu
menu.add_cascade(label='Edit')

# Language menu (radio 버튼을 통해서 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label='python')
menu_lang.add_radiobutton(label='node')
menu_lang.add_radiobutton(label='java')
menu.add_cascade(label='Language', menu=menu_lang)

# View menu
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label='Show Minimap')
menu.add_cascade(label='View', menu=menu_view)

root.config(menu=menu)

root.mainloop()