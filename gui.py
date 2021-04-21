import tkinter as tk
from tkinter import messagebox as mb
top=tk.Tk()
def hellocallback():
    mb.showinfo("Hello How U?","Okay Hi")
B= tk.Button(top, text ="Hello", command=hellocallback)
B.pack()
top.mainloop()
