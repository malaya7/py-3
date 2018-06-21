from tkinter import *
import backend

def getSelectedRow(event):
    global selectedTuple
    try:
        selectedTuple=list1.get(list1.curselection()[0])
        e1.delete(0,END)
        e1.insert(END,selectedTuple[1])
        e2.delete(0,END)
        e2.insert(END,selectedTuple[2])
        e3.delete(0,END)
        e3.insert(END,selectedTuple[3])
        e4.delete(0,END)
        e4.insert(END,selectedTuple[4])
    except IndexError:
        pass

def deleteFunction():
    backend.delete(selectedTuple[0])
    view()

def view():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def searchFunction():
    list1.delete(0,END)
    for row in backend.search(titleText.get(),authorText.get(),yearText.get(),ISBNText.get()):
        list1.insert(END,row)

def addItem():
    backend.insert(titleText.get(),authorText.get(),yearText.get(),ISBNText.get())
    list1.delete(0,END)
    list1.insert(END,(titleText.get(),authorText.get(),yearText.get(),ISBNText.get()))

def updateFunction():
    backend.update(selectedTuple[0],titleText.get(),authorText.get(),yearText.get(),ISBNText.get())

window = Tk()
window.wm_title("Book Shelf")

titleLB = Label(window,text="Title")
titleLB.grid(row=0,column=0)

yearLB = Label(window,text="Year")
yearLB.grid(row=1,column=0)

authorLB = Label(window,text="Author")
authorLB.grid(row=0,column=2)

ISBNLB = Label(window,text="ISBN")
ISBNLB.grid(row=1,column=2)

titleText = StringVar()
e1 = Entry(window,textvariable=titleText)
e1.grid(row=0,column=1)

authorText = StringVar()
e2 = Entry(window,textvariable=authorText)
e2.grid(row=0,column=3)

yearText = StringVar()
e3 = Entry(window,textvariable=yearText)
e3.grid(row=1,column=1)

ISBNText = StringVar()
e4 = Entry(window,textvariable=ISBNText)
e4.grid(row=1,column=3)

list1 = Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=3,column=2,rowspan=4)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>",getSelectedRow)

viewAllBtn = Button(window,text="View all",width=12,command=view)
viewAllBtn.grid(row=2,column=3)

SearchBtn = Button(window,text="Search entry",width=12,command=searchFunction)
SearchBtn.grid(row=3,column=3)

AddBtn = Button(window,text="Add entry",width=12,command=addItem)
AddBtn.grid(row=4,column=3)

updateBtn = Button(window,text="Update",width=12,command=updateFunction)
updateBtn.grid(row=5,column=3)

deleteBtn = Button(window,text="Delete",width=12,command=deleteFunction)
deleteBtn.grid(row=6,column=3)

closeBtn = Button(window,text="Close",width=12,command=window.destroy)
closeBtn.grid(row=7,column=3)

window.mainloop()
