import tkinter
from tkinter import messagebox
import time

#创建番茄钟窗口
root = tkinter.Tk()
root.title('番茄钟小程序')
root.geometry('300x300')
root.configure(bg='Tomato')

#创建计数的
count = 0

#创建完成计时后的弹窗
def mymsg():
    tkinter.messagebox.showinfo("提示", "恭喜完成一个番茄钟！！记得休息一下")
def mymsg2():
    tkinter.messagebox.showinfo("提示", "休息完毕！")


#创建番茄计时函数
# strptime()函数将字符串转换为datetime
def tomato_clock():
    remain_time = 1500
    bb = time.strftime('/  %M:%S', time.gmtime(remain_time))
    lb2.configure(text=bb)
    lb3.configure(text='剩余时间/总时间')
    for i in range(1500):
        remain_time -= 1
        aa = time.strftime('%M:%S', time.gmtime(remain_time))
        lb.configure(text=aa)
        root.update()
        time.sleep(1)
        if remain_time == 0:
            tomato_count()
            mymsg()

#创建计数的函数
def tomato_count():
    global count
    count += 1
    lb4.configure(text=count)

#创建休息时间函数
def relax():
    remain_time = 300
    bbb = time.strftime('/  %M:%S', time.gmtime(remain_time))
    lb2.configure(text=bbb)
    lb3.configure(text='剩余时间/总时间')
    for i in range(300):
        remain_time -= 1
        aaa = time.strftime('%M:%S', time.gmtime(remain_time))
        lb.configure(text=aaa)
        root.update()
        time.sleep(1)
        if remain_time == 0:
            mymsg2()

#创建各种标签

#番茄动态计时
lb = tkinter.Label(root, text=' ', bg='Tomato', fg='white', font='Verdana 16 bold', width=7, height=1)
lb.place(x=50, y=100)

#番茄固定时间
lb2 = tkinter.Label(root, text=' ', bg='Tomato', fg='white', font='Verdana 16 bold', width=8, height=1)
lb2.place(x=138, y=100)

#剩余时间/总时间
lb3 = tkinter.Label(root, text=' ', bg='Tomato', fg='white', font='Verdana 16 bold', width=14, height=2)
lb3.place(x=50, y=44)

#番茄个数显示
lb4 = tkinter.Label(root, text='0', bg='Tomato', fg='white', font='Verdana 16 bold', width=7, height=1)
lb4.place(x=25, y=20)

#左上角的 番茄：
lb5 = tkinter.Label(root, text='番茄：', bg='Tomato', fg='white', font='Verdana 16 bold', width=4, height=1)
lb5.place(x=5, y=20)


#按钮
#开启一个番茄
Button1 = tkinter.Button(root, text='开启一个番茄', bg='orange', fg='black', font='Verdana 14 bold', width=15, height=1, command=tomato_clock)
Button1.place(x=70, y=150)

#休息一下
Button2 = tkinter.Button(root, text='休息一下', bg='cornflowerblue', fg='black', font='Verdana 13 bold', width=15, height=1, command=relax)
Button2.place(x=70, y=200)

#循环
root.mainloop()