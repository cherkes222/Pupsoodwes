import os
import tkinter
import sqlite3
import subprocess
import player


player.root.withdraw()

self = tkinter.Tk()
self.geometry("400x300")
self.title("Login")
self.config(bg="light gray")


em_c = tkinter.StringVar()
pcode_c = tkinter.StringVar()
nm_c = tkinter.StringVar()

self.columnconfigure(0, weight=1)
self.columnconfigure(1, weight=1)
self.columnconfigure(0, weight=1)
self.columnconfigure(0, weight=1)
self.rowconfigure(0, weight=1)
self.rowconfigure(1, weight=1)
self.rowconfigure(0, weight=1)
self.rowconfigure(0, weight=1)


def create():

    another_f = tkinter.Frame(self, relief="raised", border=4, bg="pink")
    another_f.grid(row=1, column=0, columnspan=2, sticky="new")

    name = tkinter.Label(another_f, text="Name(in caps)", fg="white", bg="pink")
    name.config(font=("Franklin Gothic Medium", 12))
    name.grid(row=0, column=0, sticky="w", padx=4)

    name_blank = tkinter.Entry(another_f, textvariable=nm_c, relief="sunk", border=4)
    name_blank.grid(row=0, column=1, padx=4)

    email_c = tkinter.Label(another_f, text="Email/Phone no.", fg="white", bg="pink")
    email_c.config(font=("Franklin Gothic Medium", 12))
    email_c.grid(row=1, column=0, sticky="w", padx=4)

    email_c_b = tkinter.Entry(another_f, textvariable=em_c, relief="sunk", border=4)
    email_c_b.grid(row=1, column=1, padx=4)

    password_c = tkinter.Label(another_f, text="password", fg="white", bg="pink")
    password_c.config(font=("Franklin Gothic Medium", 12))
    password_c.grid(row=2, column=0, sticky="w", padx=4)

    password_c_b = tkinter.Entry(another_f, textvariable=pcode_c, relief="sunk", border=4)
    password_c_b.grid(row=2, column=1, padx=4)

    ok_c = tkinter.Button(another_f, text="Confirm", relief="raised", border=4, command=two)
    ok_c.grid(row=3, column=4, sticky="e")

    cancel_c = tkinter.Button(another_f, text="Cancel", relief="raised", border=4, command=self.quit)
    cancel_c.grid(row=3, column=5, sticky="w")

    another_f.tkraise()


def two():
    cp()
    login()


def login():

    lable = tkinter.Label(self, text="Welcome", fg="black", bg="light gray")
    lable.config(font=("Comic Sans MS", 20))
    lable.grid(row=0, column=0, columnspan=2, sticky="new")

    iden = tkinter.Frame(self, relief="raised", border=4, bg="pink")
    iden.grid(row=1, column=0, columnspan=2, sticky="new")

    email = tkinter.Label(iden, text="Email/phone no.", fg="white", bg="pink")
    email.config(font=("Franklin Gothic Medium", 12))
    email.grid(row=0, column=0)

    blank1 = tkinter.Entry(iden, textvariable=em_c, relief="sunk", border=4)
    blank1.grid(row=0, column=1, sticky="we")

    password = tkinter.Label(iden, text="Password", fg="white", bg="pink")
    password.config(font=("Franklin Gothic Medium", 12))
    password.grid(row=4, column=0, sticky="ws")

    blank2 = tkinter.Entry(iden, textvariable=pcode_c, relief="sunk", border=4)
    blank2.grid(row=4, column=1, sticky="we")

    okbutton = tkinter.Button(iden, text="Login", relief="raised", border=4, command=data)
    okbutton.grid(row=7, column=5, sticky="se")

    canclebutton = tkinter.Button(iden, text="Cancel", relief="raised", border=4, command=self.quit)
    canclebutton.grid(row=7, column=6, sticky="ws")

    sign = tkinter.Button(iden, text="Create account", relief="raised", border=4, command=create)
    sign.grid(row=8, column=0, sticky="we")






def final():


    fram_f = tkinter.Frame(self, bg="grey")
    fram_f.grid(row=0, column=0, rowspan=4, columnspan=4, sticky="news")
    lable_f = tkinter.Label(fram_f, text="Successfully Login in account", fg="green", bg="grey")
    lable_f.config(font=("Comic Sans MS", 16))
    lable_f.grid(row=0, column=0, rowspan=5, padx=20, pady=100, columnspan=5, sticky="we")
    playerwin_f = tkinter.Button(fram_f, text="Ok", border=4, height=1, width=10)
    playerwin_f.grid(row=3, column=3, sticky="ws")
    self.destroy()
    player.root.deiconify()



def found():

    fram_f = tkinter.Frame(self, bg="light blue")
    fram_f.grid(row=0, column=0, rowspan=4, columnspan=4, sticky="news")
    lable_f = tkinter.Label(fram_f, text="Account Not Found", fg="red", bg="light blue")
    lable_f.config(font=("Comic Sans MS", 16))
    lable_f.grid(row=0, column=0, rowspan=5, padx=20, pady=100, columnspan=5, sticky="we")
    sign = tkinter.Button(fram_f, text="<<Back", relief="raised", border=4, command=login)
    sign.grid(row=3, column=0, sticky="we")


"""Data base work start"""

db = sqlite3.connect("lalas2.sqlite")
db.execute("CREATE table if not exists lalas2(name TEXT NOT NULL, email TEXT NOT NULL, password TEXT)")


def data():

    cursor = db.cursor()
    yo = ""
    for i in em_c.get():
        yo += i
    cursor.execute("SELECT email, password from lalas2 WHERE email=? And password=?", (yo, pcode_c.get()))

    row = cursor.fetchone()
    if row:
        final()
    else:
       found()


def cp():
    cu = db.cursor()
    cu.execute("INSERT into lalas2 VALUES(?,?,?)", (nm_c.get(), em_c.get(), pcode_c.get(),))
    cu.connection.commit()


login()


def closing():
    self.destroy()
    player.root.destroy()


self.protocol("WM_DELETE_WINDOW", closing)
tkinter.mainloop()

#if __name__ == "__mainloop__":
  #  player.root.destroy()

