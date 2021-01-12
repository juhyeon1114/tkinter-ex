import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title('Hello GUI')
root.geometry('640x480+0+0') # 가로x세로+x좌표+y좌표

def info():
    msgbox.showinfo('알림', '정상적으로 예매가 완료되었습니다')

def warn():
    msgbox.showwarning('경고', '좌석이 매진되었습니다')

def error():
    msgbox.showerror('에러', '결제 오류')

def okcancel():
    msgbox.askokcancel('확인 / 취소', '해당 좌석을 예매하시겠습니까?')

def retrycancel():
    msgbox.askretrycancel('재시도 / 취소', '해당 좌석을 예매하시겠습니까?')

def yesno():
    msgbox.askyesno('예 / 아니오', '해당 좌석은 역방향입니다. 예매하시겠습니까?')

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message='예매 내역이 저장되지 않았습니다.\n저장 후에 종료하시겠습니까?')
    print(response)
    
Button(root, command=info, text='알림').pack()
Button(root, command=warn, text='경고').pack()
Button(root, command=error, text='에러').pack()

Button(root, command=okcancel, text='확인취소').pack()
Button(root, command=retrycancel, text='재시도 취소').pack()
Button(root, command=yesno, text='예 아니오').pack()
Button(root, command=yesnocancel, text='예 아니오 취소').pack()

root.mainloop()