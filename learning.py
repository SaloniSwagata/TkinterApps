# Illustration of adding images to tkinter
from tkinter import *
root = Tk()

# width x height
root.geometry("733x434")

# width,height
root.minsize(500, 300)
root.maxsize(800, 500)

photo = PhotoImage(file="sample1.png")
label = Label(image=photo)

label.pack()


root.mainloop()