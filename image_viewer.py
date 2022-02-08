from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Jimmy Image Viewer")

my_image1 = ImageTk.PhotoImage(Image.open("mario.png"))
my_image2 = ImageTk.PhotoImage(Image.open("naruto.jpg"))
my_image3 = ImageTk.PhotoImage(Image.open("neji.jpg"))
my_image4 = ImageTk.PhotoImage(Image.open("sasuke.jpg"))
my_image5 = ImageTk.PhotoImage(Image.open("itachi.jpg"))
my_image6 = ImageTk.PhotoImage(Image.open("gaara.jpg"))
my_image7 = ImageTk.PhotoImage(Image.open("kiba.jpg"))
my_image8 = ImageTk.PhotoImage(Image.open("kakashi.jpg"))
my_image9 = ImageTk.PhotoImage(Image.open("pain.jpg"))
my_image10 = ImageTk.PhotoImage(Image.open("jiraiya.jpg"))
my_image11 = ImageTk.PhotoImage(Image.open("hinata.jpg"))
my_image12 = ImageTk.PhotoImage(Image.open("konohamaru.jpg"))
my_image13 = ImageTk.PhotoImage(Image.open("rasengan.jpg"))
my_image14 = ImageTk.PhotoImage(Image.open("lee.jpg"))
my_image15 = ImageTk.PhotoImage(Image.open("shino.jpg"))
my_image16 = ImageTk.PhotoImage(Image.open("shikamaru.jpg"))


image_list = [my_image1, my_image2, my_image3, my_image4, my_image5, my_image6, my_image7, my_image8, my_image9, my_image10, my_image11, my_image12, my_image13, my_image14, my_image15, my_image16]

global my_label    
my_label = Label(image = my_image1)
my_label.grid(row = "0", column = "0", columnspan = "3")

#for x in image_list:
global y
y = image_list.index(my_image1)

#counting global label
global count
count = Label(root, text = str(y+1) + " out of " + str(len(image_list)))
count.grid(row = "2", column = "2")

    
def previous():
    global my_label
    global previous
    global y
    global image_list
    global count
    
    if y != 0:
        y -= 1
    my_label.grid_forget()
    my_label = Label(image = image_list[y])
    my_label.grid(row = "0", column = "0", columnspan = "3")
    
    #counting
    count.grid_forget()
    count = Label(root, text = str(y+1) + " out of " + str(len(image_list)))
    count.grid(row = "2", column = "2")
    return

def next():
    global my_label
    global next
    global y
    global image_list
    global count
    
    if y != len(image_list) - 1:
        y += 1    
    my_label.grid_forget()
    my_label = Label(image = image_list[y])
    my_label.grid(row = "0", column = "0", columnspan = "3")
    
    #counting
    count.grid_forget()
    count = Label(root, text = str(y+1) + " out of " + str(len(image_list)))
    count.grid(row = "2", column = "2")
    return


button_previous = Button(root, text = "<< Previous", command = previous)
button_previous.grid(row = "1", column = "0")
        
button_exit = Button(root, text = "Exit", command= root.quit)
button_exit.grid(row = "1", column = "1")


button_next = Button(root, text = "Next >>", command = next)
button_next.grid(row = "1", column = "2")


root.mainloop()