# Exploring Attributes of label and pack
from tkinter import *
# from PIL import Image, ImageTk

root = Tk()

# Adding title
root.title("Learning Tkinter")

# width x height
root.geometry("733x434")

# width,height
root.minsize(500, 300)
root.maxsize(800, 500)

# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text='Hello Everyone, \n Welcome to my page', bg="lightblue", fg="white", padx=13, pady=94, font="comicsansms 20 bold", borderwidth=3, relief=SUNKEN)

# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady

# title_label.pack(side=BOTTOM, anchor ="sw", fill=X)
title_label.pack(side=TOP, fill=Y, padx=34, pady=34)

# image = Image.open("sample.jpg")
# photo = ImageTk.PhotoImage(image)
# label = Label(image=photo)

# label.pack()


root.mainloop()