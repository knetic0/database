from tkinter import *
from tkinter import ttk
from tkinter.simpledialog import askstring
from tkinter.simpledialog import askinteger
from tkinter.messagebox import showinfo
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

def saveCustomer(_cControl):
    connCustomer = sqlite3.connect("connCustomer.db")
    cursorCustomer = connCustomer.cursor()

    customerList = [
                        (objectEntryName.get(), objectEntrySurname.get(),objectEntryIDNumber.get(),
                         objectEntryEmail.get(),objectEntryPhone.get(),date.get())
                   ]

    if _cControl == False:
        cursorCustomer.executemany("insert into customer values (?,?,?,?,?,?)", customerList)

        connCustomer.commit()

        seeAllCustomer = cursorCustomer.execute("select * from customer")
        for customerItems in seeAllCustomer:
            print(customerItems)

        connCustomer.close()
    else:
        cursorCustomer.execute("DELETE FROM customer")
        print('Succesfull')
        print(cursorCustomer.fetchall())
        connCustomer.commit()
        connCustomer.close()


def savePersonnel(_pControl):
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
    if _pControl == False:
        cursorPersonnel.executemany("insert into personnel values (?,?,?,?,?,?,?)",personnelList)

        connPersonnel.commit()

        seeAll = cursorPersonnel.execute("select * from personnel")
        for items in seeAll:
            print(items)

        connPersonnel.close()
    else:
        cursorPersonnel.execute("DELETE FROM personnel")
        print('Succesfull')
        print(cursorPersonnel.fetchall())
        connPersonnel.commit()
        connPersonnel.close()

def customerInfo():
    objectLabel.config(text='Musteri Kayiti')
    objectLabel.place(y=50,x=925)

    objectEntrySalary.config(state=DISABLED)

    submitButton = ttk.Button(gui,text='Save for Customer',command=lambda:saveCustomer(False))
    submitButton.place(x=975,y=500)

def personnelInfo():
    objectLabel.config(text='Personel Kayiti')
    objectLabel.place(y=50,x=905)

    objectEntrySalary.config(state=NORMAL)

    submitButtonPersonnel = ttk.Button(gui,text='Save for Personnel',command=lambda:savePersonnel(False))
    submitButtonPersonnel.place(x=975,y=500)

def adminLogin():
    loginName = askstring('Nickname','Enter Admin Name')
    loginPassword = askinteger('Password','Enter Admin Password')

    if loginName == 'admin' and loginPassword == 1234:
        showinfo('Welcome',"You're just sign in as Admin")

        root = Tk()
        root.geometry('360x360')
        root.title('Admin')

        reDatabaseCustomer = sqlite3.connect("connCustomer.db")
        reDatabasePersonnel = sqlite3.connect("connPersonnel.db")

        reCursorCustomer = reDatabaseCustomer.cursor()
        reCursorPersonnel = reDatabasePersonnel.cursor()

        reCursorCustomer.execute('select * from customer')
        reCursorPersonnel.execute('select * from personnel')

        reSeeAllCustomer = reCursorCustomer.fetchall()
        reSeeAllPersonel = reCursorPersonnel.fetchall()

        reDatabaseCustomer.commit()
        reDatabasePersonnel.commit()

        listbox = Listbox(root,width=60,font='Arial,24')
        listbox.place(x=50,y=60)

        listboxPersonnel = Listbox(root,width=60,font='Arial,24')
        listboxPersonnel.place(x=50,y=240)


        for i in range(len(reSeeAllCustomer)):
            listbox.insert(i,reSeeAllCustomer[i])

        for j in range(len(reSeeAllPersonel)):
            listboxPersonnel.insert(j,reSeeAllPersonel[j])

        def deleteIndex():
            reDeleteCustomer = sqlite3.connect("connCustomer.db")
            reDeleteCursorCustomer = reDeleteCustomer.cursor()
            deleteVar = askinteger('Enter Index Number','Enter Index Number from 1 to ...')

            reDeleteCursorCustomer.execute("DELETE FROM customer where id=?",(deleteVar,))
            reDeleteCursorCustomer.execute("select * from customer")
            listbox.delete(deleteVar)

            reDeleteCustomer.commit()
            reDeleteCustomer.close()

        def deleteIndexPersonnel():
            reDeletePersonel = sqlite3.connect("connPersonnel.db")
            reDeleteCursorPersonel = reDeletePersonel.cursor()
            deleteVarPersonel = askinteger('Enter Index Number','Enter Index Number from 0 to ...')

            reDeleteCursorPersonel.execute("DELETE FROM personnel where id=?",(deleteVarPersonel,))
            reDeleteCursorPersonel.execute("select * from personnel")
            listboxPersonnel.delete(deleteVarPersonel)

            reDeletePersonel.commit()
            reDeletePersonel.close()

        deleteVarButton = ttk.Button(root,text='Delete Customer',command=deleteIndex)
        deleteVarButton.place(x=700,y=200)

        deleteVarButtonPersonnel = ttk.Button(root,text='Delete Personnel',command=deleteIndexPersonnel)
        deleteVarButtonPersonnel.place(x=700,y=250)

        #for reRowsPersonel in reSeeAllPersonel:


        reDatabasePersonnel.close()
        reDatabaseCustomer.close()

        root.mainloop()

customerVariable = IntVar()

customer = ttk.Radiobutton(gui,text='Musteri',command=customerInfo,variable=customerVariable,value= 1)
customer.place(x=200,y=650)

personnel = ttk.Radiobutton(gui,text='Personel',command=personnelInfo,variable=customerVariable,value=2)
personnel.place(x=350,y=650)

deleteButton = ttk.Button(gui,text='Delete All Personnel',command=lambda:savePersonnel(True))
deleteButton.place(y=700,x=300)

deleteButtonCustomer = ttk.Button(gui,text='Delete All Customer',command=lambda:saveCustomer(True))
deleteButtonCustomer.place(y=700,x=175)

adminButton = ttk.Button(gui,text='Login by Admin',command=adminLogin)
adminButton.place(y=750,x=250)

gui.mainloop()