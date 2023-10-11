from tkinter import *
from tkinter import ttk
import sqlite3


'''c=sqlite3.connect("student.db")
curses=c.cursor()
curses.execute("CREATE TABLE IF NOT EXISTS Student(ID INTEGER,NAME VARCHAR(20),AGE INTEGER,DOB VARCHAR(20),GENDER VARCHAR(20),CITY VARCHAR(20))")
c.commit()
c.close()
print("table created")'''


class student:
    def __init__(self,main):
        self.main=main
        self.T_Frame = Frame(self.main,height=50,width=1200,background="green",bd=2,relief=GROOVE)
        self.T_Frame.pack()
        self.Title=Label(self.T_Frame,text="student management system",font="arial 20 bold",width=1200,bg="yellow")
        self.Title.pack()
        

        self.Frame1=Frame(self.main,height=580,width=480,bd=2,bg="green",relief=GROOVE)
        self.Frame1.pack(side=LEFT)
        self.Frame1.pack_propagate(0)
        

        Label(self.Frame1, text="Student Details",bg="yellow",font="arial 12 bold").place(x=20,y=20)

        self.id=Label(self.Frame1,text="ID",bg="green",font="arial 11 bold")
        self.id.place(x =40,y=60)
        self.Id_Entry=Entry(self.Frame1,width=40)
        self.Id_Entry.place(x=150,y=60)

        self.name=Label(self.Frame1,text="NAME",bg="green",font="arial 11 bold")
        self.name.place(x =40,y=100)
        self.name_Entry=Entry(self.Frame1,width=40)
        self.name_Entry.place(x=150,y=100)

        self.age=Label(self.Frame1,text="AGE",bg="green",font="arial 11 bold")
        self.age.place(x =40,y=140)
        self.age_Entry=Entry(self.Frame1,width=40)
        self.age_Entry.place(x=150,y=140)

        self.DOB=Label(self.Frame1,text="DOB",bg="green",font="arial 11 bold")
        self.DOB.place(x =40,y=180)
        self.DOB_Entry=Entry(self.Frame1,width=40)
        self.DOB_Entry.place(x=150,y=180)

        self.gender=Label(self.Frame1,text="GENDER",bg="green",font="arial 11 bold")
        self.gender.place(x =40,y=220)
        self.gender_Entry=Entry(self.Frame1,width=40)
        self.gender_Entry.place(x=150,y=220)

        self.city=Label(self.Frame1,text="CITY",bg="green",font="arial 11 bold")
        self.city.place(x =40,y=260)
        self.city_Entry=Entry(self.Frame1,width=40)
        self.city_Entry.place(x=150,y=260)

    #  ----------------------------BUTTON------------------------------

        self.Button_Frame=Frame(self.Frame1,height=250,width=250,relief=GROOVE,bd=2,bg="green")
        self.Button_Frame.place(x=80,y=300)

        self.Add=Button(self.Button_Frame,text="Add",width=25,font="arial 11 bold",command=self.Add)
        self.Add.pack()

        self.Delete=Button(self.Button_Frame,text="Delete",width=25,font="arial 11 bold",command=self.Delete)
        self.Delete.pack()

        self.Update=Button(self.Button_Frame,text="Update",width=25,font="arial 11 bold",command=self.Update)
        self.Update.pack()

        self.Clear=Button(self.Button_Frame,text="Clear",width=25,font="arial 11 bold",command=self.Clear)
        self.Clear.pack()

        self.Frame2=Frame(self.main,height=580,width=800,bd=2,bg="grey",relief=GROOVE)
        self.Frame2.pack(side=RIGHT)

        self.tree=ttk.Treeview(self.Frame2,columns=("c1","c2","c3","c4","c5","c6"),show="headings",height=25)
        self.tree.pack()

        self.tree.column("#1",anchor=CENTER,width=60)
        self.tree.heading("#1",text="ID")

        self.tree.column("#2",anchor=CENTER,width=100)
        self.tree.heading("#2",text="NAME")

        self.tree.column("#3",anchor=CENTER,width=115)
        self.tree.heading("#3",text="AGE")

        self.tree.column("#4",anchor=CENTER,width=110)
        self.tree.heading("#4",text="DOB")

        self.tree.column("#5",anchor=CENTER,width=110)
        self.tree.heading("#5",text="GENTER")

        self.tree.column("#6",anchor=CENTER)
        self.tree.heading("#6",text="CITY")

        self.tree.insert("",index=0,values=(1,"Aravind",26,"12-09-1996","Male","Thondi"))
        self.tree.pack()

    def Add(self):
        id=self.Id_Entry.get()
        name=self.name_Entry.get()
        age=self.age_Entry.get()
        dob=self.DOB_Entry.get()
        gender=self.gender_Entry.get()
        city=self.city_Entry.get()
        c=sqlite3.connect("student.db")
        curses=c.cursor()
        curses.execute("INSERT INTO Student(ID,NAME,AGE,DOB,GENDER,CITY)VALUES(?,?,?,?,?,?)",(id,name,age,dob,gender,city))
        c.commit()
        c.close()
        print("value inserted")
        self.tree.insert("",index=0,values=(id,name,age,dob,gender,city))

    def Delete(self):
        item=self.tree.selection()[0]
        self.tree.delete(item)

    def Update(self):
        id=self.Id_Entry.get()
        name=self.name_Entry.get()
        age=self.age_Entry.get()
        dob=self.DOB_Entry.get()
        gender=self.gender_Entry.get()
        city=self.city_Entry.get()
        item=self.tree.selection()[0]
        self.tree.item(item,values=(id,name,age,dob,gender,city))

    def Clear(self):
        self.Id_Entry.delete(0,END)
        self.name_Entry.delete(0,END)
        self.age_Entry.delete(0,END)
        self.DOB_Entry.delete(0,END)
        self.gender_Entry.delete(0,END)
        self.city_Entry.delete(0,END)



main =Tk()
main.title("student management system")
main.resizable(False,False)
main.geometry("1200x600")


student(main)
main.mainloop()
