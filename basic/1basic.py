from tkinter import *

root = Tk()
root.title('Hello GUI')

'''
frame
'''
root.geometry('640x480+0+0') # 가로x세로+x좌표+y좌표
# root.resizable(False, False) # 창의 가로, 세로 크기 변경 불가

'''
photo
'''
checkImg = PhotoImage(file='./img/check.png')
crossImg = PhotoImage(file='./img/cross.png')

'''
button
'''
btn1 = Button(root, text='버튼')
btn1.pack()

btn2 = Button(root, text='버튼', padx=5, pady=10)
btn2.pack()

btn3 = Button(root, text='버튼', width=10, height=3)
btn3.pack()

btn4 = Button(root, text='버튼', fg='red', bg='yellow')
btn4.pack()


btn5 = Button(root, image=checkImg)
btn5.pack()

def btncmd() :
    print('clicked btn')

btn6 = Button(root, text='동작', command=btncmd)
btn6.pack()

'''
label
'''
label1 = Label(root, text='안녕하세요')
label1.pack()

label2 = Label(root, image=checkImg)
label2.pack()

def change() :
    label1.config(text='또 만나요')
    label2.config(image=crossImg)

changeBtn = Button(root, text='클릭', command=change)
changeBtn.pack()

'''
text & entry
'''
txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, '글자를 입력하세요')

e = Entry(root, width=30)
e.pack()
e.insert(0, '한 줄만 입력')

def textBtnCmd():
    # 내용 출력
    print(txt.get('1.0', END)) # 첫번째줄.0번째위치부터 가져와라
    print(e.get())
    # 내용 삭제
    txt.delete('1.0', END)
    e.delete(0, END)

textBtn = Button(root, text='클릭', command=textBtnCmd)
textBtn.pack()



root.mainloop()