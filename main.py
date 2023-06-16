from tkinter import *
import qrcode

root=Tk()
root.title("QR generator")
root.geometry("1000x550")
root.config(bg="#AE2321")
root.resizable(False,False)

def generate():
    name=title.get()
    text=entry.get()
    qr=qrcode.make(text)
    qr.save("Employee_QR/"+str(name)+".png")  

    global Image
    Image=PhotoImage(file="Employee_QR/"+str(name)+".png")
    Image_viwe.config(image=Image)

Image_viwe=Label(root,bg="#AE2321")
Image_viwe.pack(padx=50,pady=10,side=RIGHT)


Label(root,text="Title",fg="white",bg="#AE2321",font=15).place(x=50,y=170)

title=Entry(root,width=13,font="arial 15")
title.place(x=50,y=200)

entry=Entry(root,width=28,font="arial 15")
entry.place(x=50,y=250)

Button (root,text="Generate",width=20,height=2,bg="black",fg="white",command=generate).place(x=50,y=300)


root.mainloop()