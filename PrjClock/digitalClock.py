from tkinter import*
from tkinter.ttk import*
from time import strftime

root =Tk()
root.title("Digital Clock")
def clock():
        string = strftime('%H:%M:%S:%p')
        Label.config(text=string)
        Label.after(1000,clock)

Label = Label(root, font= ("Sans srif",100), background='white', foreground='black')
Label.pack(anchor='center')

clock()

root.mainloop()

