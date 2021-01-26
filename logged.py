from tkinter import *
from tkinter import messagebox
import mysql.connector


root = Tk()
root.title("IN & OUT")
root.geometry("700x680")
root.config(background='#EA8F15')

mydb = mysql.connector.connect(user='root', passwd='@Lifechoices314', host='127.0.0.1',
                               database='Lifechoicesonline', auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

head = Label(root, text='LIFECHOICES ACADEMY',font=("times new roman", 35), bg="yellow", fg="black")
head.pack()

reg_frame = Frame(root, bg='#ABC895')
reg_frame.pack(pady=30)
heading = Label(reg_frame, text='- SIGN IN AND OUT -',
                font='times 22 bold underline',
                bg="yellow", fg="black")
heading.pack(pady=10)


def log():
    time = name_entry.get()
    sql = "UPDATE register set login = curtime() where name = %s"
    mycursor.execute(sql, (time,))

    mydb.commit()

    user = name_entry.get()
    sql = 'SELECT * FROM register WHERE name = %s'
    mycursor.execute(sql, (user,))
    results = mycursor.fetchall()
    if results:
        messagebox.showinfo("successfully", 'Logged In')
    else:
        messagebox.showinfo('error', 'try again')


def out():
    timeout = name_entry.get()
    sql = "UPDATE register set logout=curtime() where name = %s"
    mycursor.execute(sql, (timeout,))
    messagebox.showinfo("successfully", 'Logged Out')
    mydb.commit()

    user = name_entry.get()
    sql = 'SELECT * FROM register WHERE name = %s'
    mycursor.execute(sql, (user,))
    results = mycursor.fetchall()
    if results:
        root.destroy()

    else:
        messagebox.showinfo('UNKOWN STUDENT', 'Student not on Database')

def regi():
    root.destroy()
    import register

def visitor():
    messagebox.showinfo("Visitor", 'Go to Sing In Visitors?')
    root.destroy()
    import table


def back():
    root.destroy()
    import admin


name_label = Label(root, text="Name:", font='arial 15 bold',
                   fg='black',
                   bg='#ABC895')
name_label.pack(pady=10)
name_entry = Entry(root)
name_entry.pack(pady=10)

Inbtn = Button(root, text="Sign In", width=15, bg="yellow", fg='black',
               command=log)
Inbtn.pack(pady=10)

outbtn = Button(root, text="Sign Out", width=15, bg="yellow", fg='black',
                command=out)
outbtn.pack(pady=10)

stud_reg = Button(root, text="Register Students",width=15,bg="yellow", fg='black',
                      command=regi)
stud_reg.pack(pady=10)

visitbtn = Button(root, text="Sign Visitors", width=15, bg="yellow", fg='black',
                  command=visitor)
visitbtn.pack(pady=10)

bck_button = Button(root, text="Back to Admin",width=15,bg="yellow", fg='black',
                      command=back)
bck_button.pack(pady=10)
root.mainloop()
