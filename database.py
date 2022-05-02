from tkinter import *
from tkinter import ttk
from tkinter.simpledialog import askstring
from tkinter.simpledialog import askinteger
from tkinter.messagebox import showinfo
import sqlite3
from time import strftime

gui = Tk()
gui.geometry('1920x1080')
gui.title('Database')

logo = PhotoImage(file='download.png')
logoLabel = ttk.Label(gui,image=logo)
logoLabel.place(x=50,y=125)

timeLabel = ttk.Label(gui,font=('Ubuntu', 12))
timeLabel.place(x=1750,y=950)

def time():
    string = strftime('%H:%M:%S %p')
    timeLabel.config(text = string)
    timeLabel.after(1000, time)

time()

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
    '''
    cursorCustomer.execute("create table customer(name string, surname string, id integer, mail string, phone integer, date integer)")
    '''
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

    showinfo("Please Read This Information Before Access as Admin!", 'If you want to delete any Customer'
            ' or Personnel you must delete from Database before. So you must click Delete .. From Treeview.')

    if loginName == 'admin' and loginPassword == 1234:
        showinfo('Welcome',"You're just sign in as Admin")

        root = Tk()
        root.geometry('360x360')
        root.title('Admin')

        rootMy_menu = Menu(root)
        root.config(menu=rootMy_menu)

        def signout():
            showinfo('Successful!','Sign Out is successful!')
            root.destroy()

        accountSettingsMenu = Menu(rootMy_menu,tearoff=False)
        rootMy_menu.add_cascade(label='Account',menu=accountSettingsMenu)
        accountSettingsMenu.add_command(label='Sign Out',command=signout)

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

        treeCustomer = ttk.Treeview(root,column=('c1','c2','c3','c4','c5','c6'),show='headings',height=15)
        treeCustomer.place(x=200,y=200)

        treePersonnel = ttk.Treeview(root,column=('p1','p2','p3','p4','p5','p6','p7'),show='headings',height=15)
        treePersonnel.place(x=200,y=600)

        ''' CUSTOMER '''

        treeCustomer.column("# 1",anchor=CENTER)
        treeCustomer.heading("# 1",text='Name')
        treeCustomer.column("# 2",anchor=CENTER)
        treeCustomer.heading("# 2",text='Surname')
        treeCustomer.column("# 3",anchor=CENTER)
        treeCustomer.heading("# 3",text='ID')
        treeCustomer.column("# 4",anchor=CENTER)
        treeCustomer.heading("# 4",text='E-Mail')
        treeCustomer.column("# 5",anchor=CENTER)
        treeCustomer.heading("# 5",text='Phone Number')
        treeCustomer.column("# 6",anchor=CENTER)
        treeCustomer.heading("# 6",text='Birth')

        '''PERSONNEL'''

        treePersonnel.column("# 1", anchor=CENTER)
        treePersonnel.heading("# 1", text='Name')
        treePersonnel.column("# 2", anchor=CENTER)
        treePersonnel.heading("# 2", text='Surname')
        treePersonnel.column("# 3", anchor=CENTER)
        treePersonnel.heading("# 3", text='ID')
        treePersonnel.column("# 4", anchor=CENTER)
        treePersonnel.heading("# 4", text='Salary')
        treePersonnel.column("# 5",anchor=CENTER)
        treePersonnel.heading("# 5", text='E-Mail')
        treePersonnel.column("# 6", anchor=CENTER)
        treePersonnel.heading("# 6", text='Phone Number')
        treePersonnel.column("# 7", anchor=CENTER)
        treePersonnel.heading("# 7", text='Birth')

        for i in range(len(reSeeAllCustomer)):
            treeCustomer.insert('','end',text='{}'.format(i),values=(reSeeAllCustomer[i]))

        for j in range(len(reSeeAllPersonel)):
            treePersonnel.insert('','end',text='{}'.format(j),values=(reSeeAllPersonel[j]))

        def deleteTreeCustomer():
            deleteVarCustomer = treeCustomer.selection()[0]
            treeCustomer.delete(deleteVarCustomer)

        def deleteTreePersonnel():
            deleteVarPersonnel = treePersonnel.selection()[0]
            treePersonnel.delete(deleteVarPersonnel)

        def deleteIndex():
            reDeleteCustomer = sqlite3.connect("connCustomer.db")
            reDeleteCursorCustomer = reDeleteCustomer.cursor()
            deleteVar = askinteger('Enter Index Number','Enter Index Number from 1 to ...')
            reDeleteCursorCustomer.execute("DELETE FROM customer where id=?",(deleteVar,))
            reDeleteCursorCustomer.execute("select * from customer")

            reDeleteCustomer.commit()
            reDeleteCustomer.close()

        def deleteIndexPersonnel():
            reDeletePersonel = sqlite3.connect("connPersonnel.db")
            reDeleteCursorPersonel = reDeletePersonel.cursor()
            deleteVarPersonel = askinteger('Enter Index Number','Enter Index Number from 0 to ...')
            reDeleteCursorPersonel.execute("DELETE FROM personnel where id=?",(deleteVarPersonel,))
            reDeleteCursorPersonel.execute("select * from personnel")


            reDeletePersonel.commit()
            reDeletePersonel.close()

        deleteFromTreeCustomer = ttk.Button(root,text='Delete Customer From Treeview',command=deleteTreeCustomer)
        deleteFromTreeCustomer.place(x=1200,y=550)

        deleteFromTreePersonnel = ttk.Button(root,text='Delete Personnel From Treeview',command=deleteTreePersonnel)
        deleteFromTreePersonnel.place(x=1200,y=950)


        deleteVarButton = ttk.Button(root,text='Delete Customer',command=deleteIndex)
        deleteVarButton.place(x=1000,y=550)

        deleteVarButtonPersonnel = ttk.Button(root,text='Delete Personnel',command=deleteIndexPersonnel)
        deleteVarButtonPersonnel.place(x=1000,y=950)

        #for reRowsPersonel in reSeeAllPersonel:


        reDatabasePersonnel.close()
        reDatabaseCustomer.close()

        root.mainloop()

    else:
        showinfo('Incorrect Password or Username','Please re-entry your Username and Password.')

customerVariable = IntVar()

customer = ttk.Radiobutton(gui,text='Musteri',command=customerInfo,variable=customerVariable,value= 1)
customer.place(x=200,y=650)

personnel = ttk.Radiobutton(gui,text='Personel',command=personnelInfo,variable=customerVariable,value=2)
personnel.place(x=350,y=650)

deleteButton = ttk.Button(gui,text='Delete All Personnel',command=lambda:savePersonnel(True))
deleteButton.place(y=700,x=350)

deleteButtonCustomer = ttk.Button(gui,text='Delete All Customer',command=lambda:saveCustomer(True))
deleteButtonCustomer.place(y=700,x=175)

adminButton = ttk.Button(gui,text='Login by Admin',command=adminLogin)
adminButton.place(y=750,x=250)

gui.mainloop()
