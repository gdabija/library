from tkinter import *

from PIL import ImageTk, Image
from tables_manipulation import *


def printBooks():
    global img, root, top, data

    top = Toplevel()
    top.title( "Library App" )
    top.minsize( width=400, height=400 )
    top.geometry( "400x500" )
    #
    backround_image = Image.open( "2862101.png" )
    [imageSizeWidth, imageSizeHeight] = backround_image.size
    newImageWidth = int( imageSizeWidth * 0.5 )
    newImageHeight = int( imageSizeHeight * 0.5 )
    backround_image = backround_image.resize( (newImageWidth, newImageHeight), Image.ANTIALIAS )
    img = ImageTk.PhotoImage( backround_image )

    canvas1 = Canvas( top )
    canvas1.create_image( 300, 300, image=img )
    canvas1.config( bg="white", width=imageSizeWidth, height=imageSizeHeight )
    canvas1.pack( expand=True, fill=BOTH )

    headingFrame = Frame( top, bg="sky blue", bd=3, cursor="arrow" )  # bg="#FFBB00"
    headingFrame.place( relx=0.2, rely=0.1, relwidth=0.6, relheight=0.10 )

    headingLabel = Label( headingFrame, text="Print Books", bg='saddlebrown', fg='white', font=('New Roman', 13) )
    headingLabel.place( relx=0, rely=0, relwidth=1, relheight=1 )
    #Get data for the books
    data = getListBooks()

    labelFrame1 = Frame(top,bg='white')
    labelFrame1.place(relx=0.02,rely=0.3,relwidth=0.96,relheight=0.5)
    y= 0.2
    for row in data:
        Label(labelFrame1,text="%-10s%-20s%-20s%-20s"%(row[0],row[1],row[2],row[3]) ,bg='white', fg='black').place(relx=0.02,rely=y)
        y+= 0.1

    button2 = Button( top, text="QUIT", bg="black", fg="black", command=top.destroy )
    button2.place( relx=0.6, rely=0.75, relwidth=0.3, relheight=0.05 )
    return

def getListBooks():

    data = print_books()
    return data
