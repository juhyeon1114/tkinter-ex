####################################
# Merge the Images Program
####################################
from enum import EnumMeta
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
from PIL import Image
import os

'''
init
'''
root = Tk()
root.title('hello')
root.resizable(False, False)

'''
functions
'''
def mergeImages():
    images = [Image.open(x) for x in list_file.get(0, END)] # 한 줄 for문
    widths = [x.size[0] for x in images] # size[0] == image width
    heights = [x.size[1] for x in images] # size[1] == image height
    
    max_width = max(widths)
    total_height = sum(heights)

    result_img = Image.new('RGB', (max_width, total_height), (255, 255, 255)) # (색구성), (가로 세로크기), (배경색)
    y_offset = 0
    for idx, img in enumerate(images): # img붙여주기
        result_img.paste(img, (0, y_offset))
        y_offset += img.size[1]

        # progress bar
        progress = (idx + 1) / len(images) * 100
        p_var.set(progress)
        progressbar.update()


    dest_path = os.path.join(txt_dest_path.get(), 'py_gui.jpg')
    result_img.save(dest_path)
    msgbox.showinfo('info', 'success')

def startMerging():
    if list_file.size() == 0:
        msgbox.showwarning('Warning', 'Add image files')
        return

    if len(txt_dest_path.get()) == 0 :
        msgbox.showwarning('Warning', 'Add destination directory')
        return
    
    mergeImages()

def add_file():
    files = filedialog.askopenfilenames(
        title='select image files',
        filetypes=(('png', '*.png'), ('jpg', '*.jpg'), ('bmp', '*.bmp'), ('every', '*.*')),
        initialdir=r'C:\Users\juhyeon\Desktop\jh\wallpaper' # r을 붙이면 raw string으로 쓰여짐
    )
    for file in files:
        list_file.insert(END, file)

def delete_files():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

'''
file frame
'''
file_frame = Frame(root)
file_frame.pack(fill='x', padx=5, pady=5)
# add file btn
btn_add_file = Button(file_frame, text='add files', padx=5, pady=5, width=12, command=add_file)
btn_add_file.pack(side='left')
# delete files btn
btn_del_file = Button(file_frame, text='delete', padx=5, pady=5, width=12, command=delete_files)
btn_del_file.pack(side='right')

'''
list frame
'''
list_frame = Frame(root)
list_frame.pack(fill='both', padx=5, pady=5)
# scrollbar
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side='right', fill='y')
# file list
list_file = Listbox(list_frame, selectmode='extended', height=15, yscrollcommand=scrollbar.set)
list_file.pack(side='left', fill='both', expand=True)
scrollbar.config(command=list_file.yview)

'''
save route frame
'''
path_frame = LabelFrame(root, text='save route')
path_frame.pack(fill='x', padx=5, pady=5, ipady=5)
# destination path
txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side='left', fill='x', expand=True, padx=5, pady=5, ipady=4) # ipad == inner padding
# finde path btn
btn_dest_path = Button(path_frame, text='find', width=10, command=browse_dest_path)
btn_dest_path.pack(side='right', padx=5, pady=5)

'''
option frame
'''
frame_option = LabelFrame(root, text='option')
frame_option.pack(padx=5, pady=5, ipady=5)
# horizontal width option
label_width = Label(frame_option, text='width', width=8)
label_width.pack(side='left', padx=5, pady=5)
opt_width = ['maintain', '1024', '800', '640']
combo_width = ttk.Combobox(frame_option, state='readonly', values=opt_width, width=10)
combo_width.current(0)
combo_width.pack(side='left', padx=5, pady=5)
# interval space option
label_space = Label(frame_option, text='space', width=8)
label_space.pack(side='left', padx=5, pady=5)
opt_space = ['none', 'narrow', 'normal', 'wide']
combo_space = ttk.Combobox(frame_option, state='readonly', values=opt_space, width=10)
combo_space.current(0)
combo_space.pack(side='left', padx=5, pady=5)
# file format option
label_format = Label(frame_option, text='space', width=8)
label_format.pack(side='left', padx=5, pady=5)
opt_format = ['png', 'jpg', 'bmp']
combo_format = ttk.Combobox(frame_option, state='readonly', values=opt_format, width=10)
combo_format.current(0)
combo_format.pack(side='left', padx=5, pady=5)

'''
progressbar frame
'''
frame_progress = LabelFrame(root, text='progress')
frame_progress.pack(fill='x', padx=5, pady=5, ipady=5)
# progress bar
p_var = DoubleVar()
progressbar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progressbar.pack(fill='x', padx=5, pady=5)

'''
running frame
'''
frame_run = Frame(root)
frame_run.pack(fill='x', padx=5, pady=5)
# close btn
btn_close = Button(frame_run, padx=5, pady=5, text='close', width=12, command=root.quit)
btn_close.pack(side='right', padx=5, pady=5)
# start btn
btn_start = Button(frame_run, padx=5, pady=5, text='start', width=12, command=startMerging)
btn_start.pack(side='right', padx=5, pady=5)

'''
main loop
'''
root.mainloop()