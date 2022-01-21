from tkinter import *
from PIL import Image, ImageTk,ImageFilter
# from tkinter import ttk
from tkinter import filedialog as fd

import os
import time

root = Tk()
root.geometry("600x440")
root.configure(bg="powder blue")

frame1 = Frame(root, bg="thistle1")
frame2 = Frame(root, bg="lavender")
frame3 = Frame(root, bg="powder blue")


def openimg():
    global cnt
    global imgf2
    global img
    global imgf2_label
    global str
    # if cnt <1:
    frame2.filename = fd.askopenfilename(filetypes=(
    ("png files", "*.png"), ("all files", "*.*"), ("jpg files", "*.jpg"),
    ("jpeg file", "*.jpeg")))  # *.png means any name with png extension and *.* means anyy name with any extension
    # str = frame2.filename
    # labelf2 = Label(frame2, text=frame2.filename).grid()
    imgf2 = ImageTk.PhotoImage(Image.open(frame2.filename))
    img = Image.open(frame2.filename)
    print(type(img))
    print(img.size)
    imgf2_label = Label(frame2, image=imgf2)
    imgf2_label.grid(row=1, column=0)
    return img
    # else:
    #     print("cannot open more than one image, first delete opened image")
    # cnt=cnt+1
    # return filedialog.askopenfilename(filetypes=(("png files", "*.png")))


def crop():
    global img
    global labeld
    print(type(img))

    w, h = img.size
    left = w / 4
    right = 3 * w / 4
    upper = h / 4
    lower = 3 * h / 4
    img2 = img.crop([left, upper, right, lower])
    image = ImageTk.PhotoImage(img2)
    # img2.show()
    labeld = Label(frame2, image=image)
    labeld.grid(row=1, column=1)

    frame2.mainloop()
    # imgf2_label = Label(frame2, image=image)
    # imgf2_label.grid(row=, column=1, columnspan=3)
    return


def delete():
    # global cnt
    global imgf2_label #open image
    global labeld #crop
    global label_r #rotate
    global label_fil #filter
    imgf2_label.grid_forget()
    labeld.grid_forget()
    label_r.grid_forget()
    label_fil.grid_forget()


    # frame2.pack_forget()
    # frame2.pack(expand=1,fill=BOTH)
    # cnt=cnt-1


def go_to_f1():
    frame2.pack_forget()
    frame3.pack_forget()
    frame1.pack(expand=1, fill=BOTH)


def img_extract():
    frame2.pack_forget()
    frame3.pack(expand=1, fill=BOTH)
    return


def Edit_to_next():
    frame1.pack_forget()
    frame2.pack(expand=1, fill=BOTH)
    return


def resize_image(frame1, copy_of_image, label1):
    new_height = 400
    new_width = 400
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label1.configure(image=photo)
    label1.image = photo
    frame1.configure(bg="gold")


def next():
    global n
    global items_list
    n = (n + 1) % len(items_list)
    img1 = items_list[n]
    print(img1)
    image = Image.open("./Photo_Ibm/" + img1)
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)

    label = Label(frame1, image=photo)
    label.bind('<configure>', resize_image(frame1, copy_of_image, label1))
    # label.grid(row=0,column=0,columnspan=3)


def previous():
    global n
    global items_list
    n = (n - 1) % len(items_list)
    img1 = items_list[n]
    print(img1)
    image = Image.open("./Photo_Ibm/" + img1)
    print(type(image))
    # print("image size is"+str(image.size))
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)

    label2 = Label(frame1, image=photo)
    label2.bind('<configure>', resize_image(frame1, copy_of_image, label1))
    # label2.grid(row=0, column=0, columnspan=3)


def rotate():
    global img
    global label_r
    # global imag
    # global label_r
    print(type(img))
    img2 = img.rotate(90)
    # img2.show()
    # time.sleep(2)
    imag = ImageTk.PhotoImage(img2)
    # time.sleep(2)
    label_r = Label(frame2, image=imag)
    label_r.grid(row=2,column=0)
    frame2.mainloop()


def filt():
    global img
    global label_fil
    imgf = img.filter(ImageFilter.BoxBlur(2))
    imagf=ImageTk.PhotoImage(imgf)
    label_fil=Label(frame2,image=imagf)
    label_fil.grid(row=2,column=1)
    frame2.mainloop()

n = 0
global imgf2

items_list = os.listdir("Photo_Ibm")
img1 = items_list[n]

image = Image.open("./Photo_Ibm/" + img1)
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label1 = Label(frame1, image=photo)
label1.bind('<configure>', resize_image(frame1, copy_of_image, label1))
label1.grid(row=0, column=0, columnspan=3)
b1 = Button(frame1, text=">>", width=5, height=2, bg="gray1", fg="snow", command=next)
b1.grid(row=1, column=3)

b2 = Button(frame1, text="<<", width=5, height=2, bg="gray1", fg="snow", command=previous)
b2.grid(row=1, column=0)

b3 = Button(frame1, text="EXIT", width=27, height=2, bg="gray1", fg="snow", command=root.quit)
b3.grid(row=1, column=2)

b4 = Button(frame1, text="EDIT", width=24, height=2, bg="gray1", fg="snow", command=Edit_to_next)
b4.grid(row=1, column=1)

# ------------------frame2 components-------------------------#
b21 = Button(frame2, text="IMAGE EXTRACTION",bg="gray35",fg="yellow", command=img_extract)
b21.grid(row=0, column=7)

b22 = Button(frame2, text="open image", bg="gray35",fg="yellow",command=openimg)
b22.grid(row=0, column=0)

b23 = Button(frame2, text="ZOOM",bg="gray35",fg="yellow",)
b23.grid(row=0, column=1)

b24 = Button(frame2, text="CROP",bg="gray35",fg="yellow", command=crop)
b24.grid(row=0, column=2)

b25 = Button(frame2, text="Rotate", bg="gray35",fg="yellow",command=rotate)
b25.grid(row=0, column=3)

b26 = Button(frame2, text="BLUR",bg="gray35",fg="yellow",command = filt)
b26.grid(row=0, column=4)

b27 = Button(frame2, text="delete",bg="gray35",fg="yellow", command=delete)
b27.grid(row=0, column=5)

b2N = Button(frame2, text="GO TO HOMEPAGE",bg="gray35",fg="yellow", command=go_to_f1)
b2N.grid(row=0, column=6)

# ------------------------frame3------------------------#
b31 = Button(frame3, text="GO TO HOMEPAGE", command=go_to_f1)
b31.grid()
# -------------------starting with frame1----------------#

frame1.pack(expand=1, fill=BOTH)
root.mainloop()


