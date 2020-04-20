from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

mainwindow = Tk()

mainwindow.title("BookStore")
mainwindow.configure(background='yellow')
mainwindow['padx'] = 4

l1=Label(mainwindow,text="Title",background="yellow",fg='black')
l1.grid(row=0,column=0)

l2=Label(mainwindow,text="Author", background="yellow",fg='black')
l2.grid(row=0,column=2)

l3=Label(mainwindow,text="Year", background="yellow",fg='black')
l3.grid(row=1,column=0)

l4=Label(mainwindow,text="ISBN", background="yellow",fg='black')
l4.grid(row=1,column=2)

title_text=StringVar()
e1= Entry(mainwindow,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2= Entry(mainwindow,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3= Entry(mainwindow,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4= Entry(mainwindow,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1= Listbox(mainwindow, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1= Scrollbar(mainwindow)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

myLevel=Label(mainwindow, text="Made by Faysal", background='yellow')
myLevel.grid(row=7, column=0, columnspan=2)

b1= Button(mainwindow,text="View all", width=12,
background="blue", fg='white', command=view_command)
b1.grid(row=2,column=3)

b2= Button(mainwindow,text="Search entry", width=12,
background="blue", fg='white', command=search_command)
b2.grid(row=3,column=3)

b3= Button(mainwindow,text="Add entry", width=12,
background="blue", fg='white', command=add_command)
b3.grid(row=4,column=3)

b4= Button(mainwindow,text="Update selected", width=12,
background="blue", fg='white', command=update_command)
b4.grid(row=5,column=3)

b5= Button(mainwindow,text="Delete selected", width=12,
background="blue", fg='white', command=delete_command)
b5.grid(row=6,column=3)

b6= Button(mainwindow,text="Close", width=12,
background="blue", fg='white', command=mainwindow.destroy)
b6.grid(row=7,column=3)

mainwindow.mainloop()