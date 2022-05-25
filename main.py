# import required modules
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os
 
root = Tk()
root['bg']='black'
root.title("FILTER LAB")
root.geometry("1080x620")
root.resizable(width = False, height = False)

#functions
def selected():
    global img_path, img
    img_path = filedialog.askopenfilename(initialdir=os.getcwd()) 
    img = Image.open(img_path)
    img.thumbnail((350, 350)) #size of the image
    #imgg = img.filter(ImageFilter.BoxBlur(0))
    img1 = ImageTk.PhotoImage(img) #loads canvas compatible image
    canvas2.create_image(225, 225, image=img1) #x,y, image to  be displayed
    canvas2.image=img1 
                                                                                                                                                                                                               
def blur(event):
    global img_path, img1, imgg
    for m in range(0, v1.get()+1):
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            imgg = img.filter(ImageFilter.BoxBlur(m))
            img1 = ImageTk.PhotoImage(imgg) 
            canvas2.create_image(225, 225, image=img1)
            canvas2.image=img1

def contour(event):
    global img_path, img12, img13
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img12 = img.filter(ImageFilter.CONTOUR)
    img13 = ImageTk.PhotoImage(img12) 
    canvas2.create_image(225, 225, image=img13)
    canvas2.image=img13

def brightness(event):
    global img_path, img2, img3
    for m in range(0, v2.get()+1):
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            imgg = ImageEnhance.Brightness(img)
            img2 = imgg.enhance(m)
            img3 = ImageTk.PhotoImage(img2)
            canvas2.create_image(225, 225, image=img3)
            canvas2.image=img3

def contrast(event):
    global img_path, img4, img5
    for m in range(1, v3.get()+1):
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            imgg = ImageEnhance.Contrast(img)
            img4 = imgg.enhance(m)
            img5 = ImageTk.PhotoImage(img4)
            canvas2.create_image(225, 225, image=img5)
            canvas2.image=img5

def sharpen(event):
    global img_path, img14, img15
    for m in range(1, v6.get()+1):
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            imgg = ImageEnhance.Sharpness(img)
            img14 = imgg.enhance(m)
            img15 = ImageTk.PhotoImage(img14)
            canvas2.create_image(225, 225, image=img15)
            canvas2.image=img15

def color(event):
    global img_path, img16, img17
    for m in range(1, v7.get()+1):
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            imgg = ImageEnhance.Color(img)
            img16 = imgg.enhance(m)
            img17 = ImageTk.PhotoImage(img16)
            canvas2.create_image(225, 225, image=img17)
            canvas2.image=img17
            
def rotate_image(event):
        global img_path, img6, img7
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        img6 = img.rotate(int(rotate_combo.get()))
        img7 = ImageTk.PhotoImage(img6)
        canvas2.create_image(225, 225, image=img7)
        canvas2.image=img7
        
def flip_image(event):
        global img_path, img8, img9
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        if flip_combo.get() == "FLIP LEFT TO RIGHT":
            img8 = img.transpose(Image.FLIP_LEFT_RIGHT)
        elif flip_combo.get() == "FLIP TOP TO BOTTOM":
            img8 = img.transpose(Image.FLIP_TOP_BOTTOM)
        img9 = ImageTk.PhotoImage(img8)
        canvas2.create_image(225, 225, image=img9)
        canvas2.image=img9   

def image_border(event):
    global img_path, img10, img11

    for m in range(0, v4.get()+1):
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            img10 = ImageOps.expand(img, border=m, fill='black')
            img11 = ImageTk.PhotoImage(img10)
            canvas2.create_image(225, 225, image=img11)
            canvas2.image=img11

img1 = None
img3 = None
img5 = None
img7 = None
img9 = None
img11 = None
img13= None
img15= None
img17= None

def save():
    global img_path, imgg, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11
    #file=None
    ext = img_path.split(".")[-1]
    file=asksaveasfilename(defaultextension =f".{ext}",filetypes=[("All Files","."),("PNG file",".png"),("jpg file",".jpg")])
    if file: 
            if canvas2.image==img1:
                imgg.save(file)
            elif canvas2.image==img3:
                img2.save(file)
            elif canvas2.image==img5:
                img4.save(file)
            elif canvas2.image==img7:
                img6.save(file)
            elif canvas2.image==img9:
                img8.save(file)
            elif canvas2.image==img11:
                img10.save(file)
            elif canvas2.image==img13:
                img12.save(file) 
            elif canvas2.image==img15:
                img14.save(file)
            elif canvas2.image==img17:
                img16.save(file) 


rotate = Label(root, text="Rotate:", font=("consolas 17 "),fg='white', bg='black', width=7, anchor='e')
rotate.place(x=700, y=50)
values = [0, 90, 180, 270]
rotate_combo = ttk.Combobox(root, values=values, font=('consolas 10 '))
rotate_combo.place(x=800, y=57)
rotate_combo.bind("<<ComboboxSelected>>", rotate_image)

flip = Label(root, text="Flip:", font=("consolas 17 "),fg='white', bg='black',width=7, anchor='e')
flip.place(x=700, y=102)
values1 = ["FLIP LEFT TO RIGHT", "FLIP TOP TO BOTTOM"]
flip_combo = ttk.Combobox(root, values=values1, font=('consolas 10 bold'))
flip_combo.place(x=800, y=109)
flip_combo.bind("<<ComboboxSelected>>", flip_image)

border = Label(root, text="Border:", font=("consolas 17 "), fg='white', bg='black',width=7, anchor='e')
border.place(x=700, y=154)
v4 = IntVar()   
scale4 = ttk.Scale(root, from_=0, to=15, variable=v4, orient=HORIZONTAL, command=image_border)
scale4.place(x=800, y=160)


# create labels, scales and comboboxes
blurr = Label(root, text="Blur:", font=("consolas 17 "),fg='white', bg='black', width=7, anchor='e')
blurr.place(x=700, y=205)
v1 = IntVar()
scale1 = ttk.Scale(root, from_=0, to=10, variable=v1, orient=HORIZONTAL, command=blur)
scale1.place(x=800, y=211)

bright = Label(root, text="Brightness:", font=("consolas 17 "),fg='white', bg='black',width=11, anchor='e')
bright.place(x=648, y=256)
v2 = IntVar()   
scale2 = ttk.Scale(root, from_=1, to=10, variable=v2, orient=HORIZONTAL, command=brightness) 
scale2.place(x=800, y=262)

contrast1 = Label(root, text="Contrast:", font=("consolas 17 "),fg='white',width=10, bg='black', anchor='e')
contrast1.place(x=660, y=307)
v3 = IntVar()   
scale3 = ttk.Scale(root, from_=0, to=10, variable=v3, orient=HORIZONTAL, command=contrast) 
scale3.place(x=800, y=313)

sharp = Label(root, text="Sharpness:", font=("consolas 17 "),fg='white',width=11, bg='black', anchor='e')
sharp.place(x=648, y=358)
v6 = IntVar()   
scale6 = ttk.Scale(root, from_=0, to=10, variable=v6, orient=HORIZONTAL, command=sharpen) 
scale6.place(x=800, y=364)

color1 = Label(root, text="Enhance:", font=("consolas 17 "),fg='white',width=11, bg='black', anchor='e')
color1.place(x=648, y=409)
v7 = IntVar()   
scale7 = ttk.Scale(root, from_=0, to=10, variable=v7, orient=HORIZONTAL, command=color) 
scale7.place(x=800, y=415)

contour1 = Label(root, text="Contour:", font=("consolas 17 "),fg='white', bg='black', width=8, anchor='e')
contour1.place(x=686, y=460)
v5 = IntVar()
scale5 = ttk.Scale(root, from_=0, to=10, variable=v5, orient=HORIZONTAL, command=contour)
scale5.place(x=800, y=466)


# create canvas to display image
canvas2 = Canvas(root, width="420", height="420", relief=RIDGE, bd=7, highlightbackground="#696969", highlightthickness=7)
canvas2.place(x=120, y=50)



# create buttons
def on_enter(e):
   btn1.config(background='white', foreground= "black")

def on_leave(e):
   btn1.config(background= '#106dc9', foreground= 'white')
btn1 = Button(root, text="Select Image", bg='#106dc9', fg='white',width=12, font=('consolas 12 bold'), relief=SUNKEN, command=selected)
btn1.place(x=120, y=540)

btn1.bind('<Enter>', on_enter)
btn1.bind('<Leave>', on_leave)


def on_enter(e):
   btn2.config(background='white', foreground= "black")

def on_leave(e):
   btn2.config(background= '#106dc9', foreground= 'white')
btn2 = Button(root, text="Save", bg='#106dc9', fg='white',width=12, font=('consolas 12 bold'), relief=SUNKEN,  command=save)
btn2.place(x=283, y=540)
btn2.bind('<Enter>', on_enter)
btn2.bind('<Leave>', on_leave)

def on_enter(e):
   btn3.config(background='white', foreground= "black")

def on_leave(e):
   btn3.config(background= '#106dc9', foreground= 'white')
btn3 = Button(root, text="Exit", bg='#106dc9', fg='white',width=12, font=('consolas 12 bold'), relief=SUNKEN, command=root.destroy)
btn3.place(x=445, y=540)
btn3.bind('<Enter>', on_enter)
btn3.bind('<Leave>', on_leave)

root.mainloop()
