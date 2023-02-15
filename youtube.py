from tkinter import*
from pytube import YouTube
def ok():
    e1.get()
    e2.get()
    stream=YouTube(e1.get()).streams.get_highest_resolution().download(e2.get())


win=Tk()
win.geometry('500x500')
win.title("JEMY")
win.maxsize(500,500)
win.minsize(500,500)
win.config(bg='#2E4053')
icon=PhotoImage(file='icon-png-images-17.jpg')
win.iconphoto(True,icon)
l1=Label(text='URL',bg='#2E4053',font=('Arial',15,'bold'))
l1.place(x=140,y=170)
l2=Label(text='Download',bg='#2E4053',font=("Arial",15,'bold'))
l2.place(x=85,y=205)
l3=Label(text='Welcome in \nJEMY Application',bg='#2E4053',fg='#7F8C8D',font=('Arial',18,'bold')).pack()
e1=Entry(bg='#566573',font=("Arial",11,'bold'))
e1.place(x=190,y=170)
e2=Entry(bg='#566573',font=('Ariaal',11,'bold'))
e2.place(x=190,y=210)
b1=Button(text='OK',bg='#212F3C',font=('Arial',12,'bold'),command=ok)
b1.place(x=250,y=260)
win.mainloop()