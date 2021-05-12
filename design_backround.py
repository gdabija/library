from tkinter import *
from PIL import Image, ImageTk

from addBook import *
from delete_book import *
from print_book import *
from return_book import *
from issue_book import *

connect_database()
root = Tk()
root.title( "Library App" )
root.minsize( width=400, height=400 )
root.geometry( "400x500" )

backround_image = Image.open( "2862101.png" )
[imageSizeWidth, imageSizeHeight] = backround_image.size
newImageWidth = int( imageSizeWidth * 0.5 )
newImageHeight = int( imageSizeHeight * 0.5 )
backround_image = backround_image.resize( (newImageWidth, newImageHeight), Image.ANTIALIAS )
img = ImageTk.PhotoImage( backround_image )

canvas1 = Canvas( root )
canvas1.create_image( 300, 300, image=img )
canvas1.config( bg="white", width=imageSizeWidth, height=imageSizeHeight )
canvas1.pack( expand=True, fill=BOTH )

headingFrame = Frame( root, bg="sky blue", bd=3, cursor="arrow" )  # bg="#FFBB00"
headingFrame.place( relx=0.2, rely=0.1, relwidth=0.6, relheight=0.10 )
headingLabel = Label( headingFrame, text="Options For \n Our Library", bg='saddlebrown', fg='white',
                      font=('New Roman', 13) )
headingLabel.place( relx=0, rely=0, relwidth=1, relheight=1 )

btn1 = Button( root, text="Add Book", bg='black', fg='black', command=addBook )
btn1.place( relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1 )

btn2 = Button( root, text="Delete Book", bg='black', fg='black', command=deleteBook )
btn2.place( relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1 )

btn3 = Button( root, text="View Book List", bg='black', fg='black', command=printBooks )
btn3.place( relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1 )

btn4 = Button( root, text="Issue Book to Student", bg='black', fg='black', command=issueBook )
btn4.place( relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1 )

btn5 = Button( root, text="Return Book", bg='black', fg='black', command=returnBook )
btn5.place( relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1 )

btn6 = Button( root, text="Quit", bg='black', fg='black', command=root.destroy )
btn6.place( relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1 )

root.mainloop()
