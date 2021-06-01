# Illustration of fixed size window
from tkinter import *
root = Tk()

# width x height
root.geometry("733x434")

# width,height
root.minsize(500, 300)
root.maxsize(800, 500)

string = "Welcome to Tkinter"


msg = Label(text=string)
msg.pack()

root.mainloop()