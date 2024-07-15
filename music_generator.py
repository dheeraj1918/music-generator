import numpy as np
import soundfile as sf
from tkinter import *
def music(address):
    fs=8000
    ts=np.arange(0,0.5,1/fs)
    notes=np.random.randint(1,88,size=np.random.randint(30,45))
    length=notes.size
    output=np.array([])
    for i in range(1,length):
        f=440*(2**((notes[i]-49)/12))
        x=np.cos(2*np.pi*f*ts)
        output=np.concatenate([output,x])
    sf.write(address+"\\song.wav",output,fs)
    status.config(text="Saved Successfully")
    return True
address="C:\\Users\\Dheeraj\\Dropbox\\PC\\Downloads"
window=Tk()
txt_label=Label(window,text="Click SUBMIT to Generate Music")
txt_label.pack()
submit_btn=Button(window,text="SUBMIT",command=lambda:music(address))
submit_btn.pack()
status=Label(window,text="")
status.pack()
window.geometry("300x125")
window.mainloop()