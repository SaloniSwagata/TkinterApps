# Illustration of adding images to tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# width x height
root.geometry("733x434")

# width,height
root.minsize(500, 300)
root.maxsize(800, 500)

image = Image.open("sample.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)

label.pack()


root.mainloop()