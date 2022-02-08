from tkinter import *
import PIL.Image, PIL.ImageTk
root = Tk()
root.title("Jimmy Image Viewer")
#img = ("wm", "iconphoto", root._w, PhotoImage(file = "a.ico"))
#root.tk.call(img)
img = PIL.Image.open("background/mario.png")
image = PIL.ImageTk.PhotoImage(img)
Lb = Label(root, image = image)
Lb.pack()