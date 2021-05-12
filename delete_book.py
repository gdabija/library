from tkinter import *

from PIL import ImageTk, Image
from tables_manipulation import *


def deleteBook():
    global id, root, img, top

    #

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

    headingLabel = Label( headingFrame, text="Delete Book", bg='saddlebrown', fg='white', font=('New Roman', 13) )
    headingLabel.place( relx=0, rely=0, relwidth=1, relheight=1 )

    # Book ID
    lb1 = Label( top, text="Book ID : ", bg='brown', fg='white' )
    lb1.place( relx=0.075, rely=0.3, relheight=0.05 )

    id = Entry( top )
    id.place( relx=0.3, rely=0.3, relwidth=0.6, relheight=0.05 )

    button = Button( top, text="SUBMIT", bg="black", fg="black", command=removeBook )
    button.place( relx=0.1, rely=0.75, relwidth=0.3, relheight=0.05 )

    button2 = Button( top, text="QUIT", bg="black", fg="black", command=top.destroy )
    button2.place( relx=0.6, rely=0.75, relwidth=0.3, relheight=0.05 )

    return


def removeBook():
    bookId = id.get()
    topForMessage = Toplevel()
    canvasForMessage = Canvas( topForMessage )
    canvasForMessage.config( bg="white", width=200, height=200 )
    canvasForMessage.pack( expand=True, fill=BOTH )

    if (delete_book(bookId)):
        headingLabel = Label( topForMessage, text="Book Deleted", bg='white', fg='black', font=('New Roman', 13) )
        headingLabel.place( relx=0, rely=0, relwidth=1, relheight=1 )

    else:
        headingLabel = Label( topForMessage, text="Could not delete Book", bg='white', fg='black', font=('New Roman', 13) )
        headingLabel.place( relx=0, rely=0, relwidth=1, relheight=1 )

    top.destroy()

    return
