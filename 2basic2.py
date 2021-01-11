from tkinter import *

root = Tk()
root.title('Hello GUI')
root.geometry('640x480+0+0') # 가로x세로+x좌표+y좌표

'''
listbox
'''
listbox = Listbox(root, selectmode="extended", height=0) #selectmode = extended, single ...
listbox.insert(0, '사과')
listbox.insert(1, '딸기')
listbox.insert(2, '바나나')
listbox.insert(END, '수박')
listbox.insert(END, '포도')
listbox.pack()

def btnCmd():
    listbox.delete(END)
    print(listbox.get(0, END))
    print(listbox.size(), '개 남음')
    pass

def deleteSelectedLists():
    selected = listbox.curselection()
    print(selected)

btn = Button(root, text='클릭', command=btnCmd)
btn.pack()

btn2 = Button(root, text='선택항목', command=deleteSelectedLists)
btn2.pack()

'''
checkbox
'''
chkvar = IntVar() # chkvar 에 int 형으로 값을 저장한다.
chkbox = Checkbutton(root, text='오늘 하루 이 창을 열지 않기', variable=chkvar)
# chkbox.select() # 선택
# chkbox.deselect() # 선택 해제 (default)
chkbox.pack()

def cmd():
    print(chkvar.get())

chkBtn = Button(root, text='클릭', command=cmd)
chkBtn.pack()

root.mainloop()