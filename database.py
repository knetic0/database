from tkinter import *
from tkinter import ttk
import sqlite3

gui = Tk()
gui.geometry('1920x1080')
gui.title('Database')

logo = PhotoImage(file='download.png')
logoLabel = ttk.Label(gui,image=logo)
logoLabel.place(x=50,y=125)

objectLabel = ttk.Label(gui,text='Lutfen Kayit Turunu Seciniz.',font='Arial 28')
objectLabel.place(x=780,y=50)

objectLabelName = ttk.Label(gui,text='Name = ',font='Arial,20')
objectLabelName.place(y=175,x=625)
objectLabelSurname = ttk.Label(gui,text='Surname = ',font='Arial,20')
objectLabelSurname.place(y=175,x=1100)
objectLabelIDNumber = ttk.Label(gui,text='ID Number = ',font='Arial,20')
objectLabelIDNumber.place(y=250,x=580)
objectLabelSalary = ttk.Label(gui,text='Salary = ',font='Arial,20')
objectLabelSalary.place(y=250,x=1120)
objectLabelEmail = ttk.Label(gui,text='Email = ',font='Arial,20')
objectLabelEmail.place(y=325,x=625)
objectLabelPhone = ttk.Label(gui,text='Phone Number = ',font='Arial,20')
objectLabelPhone.place(y=325,x=1045)
objectLabelDate = ttk.Label(gui,text='Birthday = ',font='Arial,20')
objectLabelDate.place(y=400,x=780)

objectEntryName = ttk.Entry(gui,font='Arial,20')
objectEntryName.place(x=700,y=175)
objectEntrySurname = ttk.Entry(gui,font='Arial,20')
objectEntrySurname.place(x=1200,y=175)
objectEntryIDNumber = ttk.Entry(gui,font='Arial,20')
objectEntryIDNumber.place(x=700,y=250)
objectEntrySalary = ttk.Entry(gui,font='Arial,20')
objectEntrySalary.place(x=1200,y=250)
objectEntryEmail = ttk.Entry(gui,font='Arial,20')
objectEntryEmail.place(x=700,y=325)
objectEntryPhone = ttk.Entry(gui,font='Arial,20')
objectEntryPhone.place(x=1200,y=325)

variables = ['1980','1981','1982','1983','1984','1985',
             '1986','1987','1988','1989','1990','1991',
             '1992','1993','1994','1995','1996','1997',
             '1998','1999','2000','2001','2002','2003']

date = ttk.Combobox(gui,values=variables,font='Arial,20')
date.place(x=880,y=400)

def saveCustomer():
    connCustomer = sqlite3.connect("connCustomer.db")
    cursorCustomer = connCustomer.cursor()

    customerList = [
                        (objectEntryName.get(), objectEntrySurname.get(),objectEntryIDNumber.get(),
                         objectEntryEmail.get(),objectEntryPhone.get(),date.get())
                   ]

    cursorCustomer.executemany("insert into customer values (?,?,?,?,?,?)", customerList)

    connCustomer.commit()

    seeAllCustomer = cursorCustomer.execute("select * from customer")
    for customerItems in seeAllCustomer:
        print(customerItems)

    connCustomer.close()


def savePersonnel():
    connPersonnel = sqlite3.connect("connPersonnel.db")
    cursorPersonnel = connPersonnel.cursor()
    '''
    cursorPersonnel.execute("create table personnel(name string, surname string, id integer, salary integer, mail string,"
                            "phone integer, date integer)")
    '''
    personnelList = [
                        (objectEntryName.get(),objectEntrySurname.get(),objectEntryIDNumber.get(),
                         objectEntrySalary.get(),objectEntryEmail.get(),objectEntryPhone.get(),date.get())
                    ]

    cursorPersonnel.executemany("insert into personnel values (?,?,?,?,?,?,?)",personnelList)

    connPersonnel.commit()

    seeAll = cursorPersonnel.execute("select * from personnel")
    for items in seeAll:
        print(items)

    connPersonnel.close()

def customerInfo():
    objectLabel.config(text='Musteri Kayiti')
    objectLabel.place(y=50,x=925)

    objectEntrySalary.config(state=DISABLED)

    submitButton = ttk.Button(gui,text='Save for Customer',command=saveCustomer)
    submitButton.place(x=975,y=500)

def personnelInfo():
    objectLabel.config(text='Personel Kayiti')
    objectLabel.place(y=50,x=905)

    objectEntrySalary.config(state=NORMAL)

    submitButtonPersonnel = ttk.Button(gui,text='Save for Personnel',command=savePersonnel)
    submitButtonPersonnel.place(x=975,y=500)

customerVariable = IntVar()

customer = ttk.Radiobutton(gui,text='Musteri',command=customerInfo,variable=customerVariable,value= 1)
customer.place(x=200,y=650)

personnel = ttk.Radiobutton(gui,text='Personel',command=personnelInfo,variable=customerVariable,value=2)
personnel.place(x=350,y=650)

gui.mainloop()