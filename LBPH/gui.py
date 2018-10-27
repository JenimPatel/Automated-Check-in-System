from tkinter import *

f_name=[]
l_name=[]
ad_no=[]

def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

def store_entries():
    global f_name,l_name,ad_no
    f_name.append(e1.get())
    l_name.append(e2.get())
    ad_no.append(e3.get())

def display():
    for i in range(len(f_name)):
        print(f_name[i],l_name[i],ad_no[i])

master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)
Label(master, text="Ad no.").grid(row=2)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=store_entries).grid(row=3, column=1, sticky=W, pady=4)
Button(master,text='Display', command=display).grid(row=3,column=2,sticky=W, pady=4)

mainloop()