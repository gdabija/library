from tkinter import *
from PIL import Image, ImageTk
from tables_manipulation import *

root = Tk()
root.title( "Library App" )
root.minsize( width=400, height=400 )
root.geometry( "400x500" )

backround_image = Image.open( "2862101.png" )
[imageSizeWidth,imageSizeHeight] = backround_image.size
newImageWidth = int(imageSizeWidth*0.5)
newImageHeight = int(imageSizeHeight*0.5)
backround_image = backround_image.resize((newImageWidth,newImageHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(backround_image)
canvas = Canvas(root)
canvas.create_image(300,300, image=img)
canvas.config(bg="white", width=imageSizeWidth, height=imageSizeHeight)

headingFrame = Frame(root, bg="sky blue",bd=3, cursor="arrow") #bg="#FFBB00"
headingFrame.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.10)
headingLabel = Label(headingFrame, text="Options For \n Our Library", bg='saddlebrown', fg='white', font=('New Roman',13))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Book Details",bg='black', fg='black', command=add_book())
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

btn2 = Button(root,text="Delete Book",bg='black', fg='black', command=delete_book())
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

btn3 = Button(root,text="View Book List",bg='black', fg='black', command=print_available_books())
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

btn4 = Button(root,text="Issue Book to Student",bg='black', fg='black', command = issue_book())
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

btn5 = Button(root,text="Return Book",bg='black', fg='black', command = return_book())
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)
canvas.pack(expand = True, fill=BOTH)
mainloop()

