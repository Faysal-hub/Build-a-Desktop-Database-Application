import tkinter



mainwindow = tkinter.Tk()

mainwindow.title("Black Jack")
mainwindow.configure(background='yellow')
mainwindow['padx'] = 8

l1=tkinter.Label(mainwindow,text="Title",background="yellow", fg='black')
l1.grid(row=0,column=0)

l2=tkinter.Label(mainwindow,text="Author", background="yellow", fg='black')
l2.grid(row=0,column=2)

l3=tkinter.Label(mainwindow,text="Year", background="yellow", fg='black')
l3.grid(row=1,column=0)

l4=tkinter.Label(mainwindow,text="ISBN", background="yellow", fg='black')
l4.grid(row=1,column=2)

# title_text=StringVar()
e1=tkinter.Entry(mainwindow,)
e1.grid(row=0,column=1)

# author_text=StringVar()
e2=tkinter.Entry(mainwindow,)
e2.grid(row=0,column=3)

# year_text=StringVar()
e3=tkinter.Entry(mainwindow,)
e3.grid(row=1,column=1)

# isbn_text=StringVar()
e4=tkinter.Entry(mainwindow,)
e4.grid(row=1,column=3)

list1=tkinter.Listbox(mainwindow, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=tkinter.Scrollbar(mainwindow)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# list1.bind('<<tkinter.ListboxSelect>>',get_selected_row)

b1=tkinter.Button(mainwindow,text="View all", width=12,background="blue", fg='white')
b1.grid(row=2,column=3)

b2=tkinter.Button(mainwindow,text="Search entry", width=12,background="blue", fg='white')
b2.grid(row=3,column=3)

b3=tkinter.Button(mainwindow,text="Add entry", width=12,background="blue", fg='white')
b3.grid(row=4,column=3)

b4=tkinter.Button(mainwindow,text="Update selected", width=12,background="blue", fg='white')
b4.grid(row=5,column=3)

b5=tkinter.Button(mainwindow,text="Delete selected", width=12,background="blue", fg='white')
b5.grid(row=6,column=3)

b6=tkinter.Button(mainwindow,text="Close", width=12,background="blue", fg='white')
b6.grid(row=7,column=3)

mainwindow.mainloop()