from tkinter import *
import random
import winsound
import time
def start(event):
    print('opening...')
    b.create_rectangle(0, 0, s, d, fill='#000000', outline='#000000')
    a.update()
    time.sleep(1)
    text001=b.create_text(s // 2, d // 50 * 30, text='Выбор пизода', fill='#00ffff', font=10, justify=LEFT)
    text002=b.create_text(s // 2, d // 50 * 31, text='Загруска', fill='#ffffff', font=10, justify=LEFT)
    text003=b.create_text(s // 2, d // 50 * 32, text='Настройки', fill='#ffffff', font=10, justify=LEFT)
    text004=b.create_text(s // 2, d // 50 * 33, text='Выход', fill='#ffffff', font=10, justify=LEFT)
def xe(event):
    if a.attributes('-fullscreen') == True:
        a.attributes('-fullscreen', False)
        print('fullscreen=0')
    
    elif a.attributes('-fullscreen') == False:
        a.attributes('-fullscreen', True)
        print('fullscreen=1')
def dx(event):
    a.destroy()
    print('quit')
def sc(event):
    print(0)
def xc(event):
    print('start')
    cd=a.bind('<q>', sc)
    b.create_rectangle(0, 0, s, d, fill='#AAAAAA', outline='#000000')
    b.create_line(s // 3, 0, s // 3, d, fill='#000000', width=5)
    b.create_line(s // 3 * 2, 0, s // 3 * 2, d, fill='#000000', width=5)
    b.create_line(0, d // 4, s, d // 4, fill='#000000', width=5)
    b.create_line(0, d // 4 * 2, s, d // 4 * 2, fill='#000000', width=5)
    b.create_line(0, d // 4 * 3, s, d // 4 * 3, fill='#000000', width=5)
    b.create_text(s // 2, d // 2, text="создатель:\nВова Вахмин\nподдержали:\nАртем Тиманов,\nВаня\nнажмите e для продолжения ", justify=CENTER, fill='#00FFFF', font=10)
    fd=a.bind('<e>', start)
def dg(event):
    a.destroy()
a=Tk()
a.attributes('-fullscreen', True)
s=a.winfo_screenwidth()
d=a.winfo_screenheight()
center_text=d * s // 2
a.title('Космечиские_Аномалии')
a.geometry('%dx%d' % (s, d))
a.resizable(width=False, height=False)
cd=a.bind('<q>', dg)
fd=a.bind('<e>', xc)
cd=a.bind('<F11>', xe)
b=Canvas(a, width=s, height=d, bg='#000000')
b.pack()
b.create_text(s // 2, d // 2, text='|q:выход|\n|e:запуск|\n|пожалуйста используйте английскую раскладку|\n|разрешение:%dx%d|' % (s, d), justify=LEFT, fill='#FFFFFF', font='sg')
a.mainloop()
