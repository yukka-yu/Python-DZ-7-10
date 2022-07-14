from pytube import YouTube
from tkinter import *


# в этом файле скачивается видео с помощью интерфейса с парой окошек для адреса видео и папки, куда его скачать

def clicked():
    link = txt1.get()
    path = txt2.get()
    yt = YouTube(link)
    video_best = yt.streams.order_by('resolution').filter(progressive=True, file_extension='mp4').desc().first()
    video_best.download(path)


window = Tk()
window.geometry('420x200')
window.title('Video Download App')

lbl1 = Label(window, text="Add your video link here", font=("Arial Bold", 18))  
lbl1.grid(column=0, row=0) 

txt1 = Entry(window,width=50)  
txt1.grid(column=0, row=1)

lbl2 = Label(window, text="Add path to your Video Folder here", font=("Arial Bold", 16))  
lbl2.grid(column=0, row=2) 

txt2 = Entry(window,width=50)  
txt2.grid(column=0, row=3)


btn = Button(window, text="Download", font=("Arial Bold", 24), command=clicked)  
btn.grid(column=0, row=4) 

window.mainloop()