import tkinter as tk
import tkinter.ttk as ttk
from datetime import *


class Application(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.root.geometry('1050x750')
        self.initialize_user_interface()

    def initialize_user_interface(self):
        self.root.title("Signin page")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.config(background="#EA8915")

        # Time & Date
        clock = tk.Label(self.root, font="bold")
        clock.place(x=5, y=5)

        time = datetime.now()
        clock.config(text=time.strftime('Date: ' + "%d/%m/%y\n" + 'Time: ' + "%H:%M:%S %p"), font='times 15', fg='black', bg='yellow')

        self.heading = tk.Label(self.root, text='- VISITORS REGISTOR -',font=("times new roman", 35), bg="yellow", fg="black")
        self.heading.place(x=300, y=40)

        # Define the different GUI widgets
        self.name_label = tk.Label(self.root, text="Name:",  font='arial 20 bold italic', fg='black', bg='yellow')
        self.name_label.place(x=200, y=150)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.place(x=400, y=150)

        self.purpose_label = tk.Label(self.root, text="Purpose", font='arial 20 bold italic', fg='black', bg='yellow')
        self.purpose_label.place(x=200, y=200)

        self.box = ttk.Combobox(self.root, state="readonly", font=("arial", 12, "bold"), width=22)
        self.box['values'] = ('SELECT', 'STUDENT', 'STAFF MEMBER')
        self.box.current(0)
        self.box.place(x=400, y=200)


        self.gen_lab = tk.Label(self.root, text="Gender", font=('arial 20 bold italic'), bg='yellow', fg='black')
        self.gen_lab.place(x=200, y=250)

        com = ttk.Combobox(self.root, state="readonly")
        com['values'] = ('Male', "Female", "Other")
        com.place(x=400, y=250)

        self.insert_btn = tk.Button(self.root, text="Insert", width=15,bg="yellow",
                                    command=self.insert_data)
        self.insert_btn.place(x=200, y=300)

        self.reg_btn = tk.Button(self.root, text="BACK", width=15, bg="yellow",
                                 command=self.back2)
        self.reg_btn.place(x=400, y=300)

        self.erase_btn = tk.Button(self.root, text="Delete", width=15,bg="yellow",
                                   command=self.delete_data)
        self.erase_btn.place(x=600, y=300)

        self.exit_btn = tk.Button(self.root, text="Exit", width=15,bg="yellow",
                                  command=self.root.quit)
        self.exit_btn.place(x=800, y=300)

        # Set the treeview
        self.tree = ttk.Treeview(self.root, columns=('Name', 'Purpose', 'Status', 'Time','DAY'))

        # Set the heading (Attribute Names)
        self.tree.heading('#0', text='Status')
        self.tree.heading('#1', text='Name')
        self.tree.heading('#2', text='Purpose')
        self.tree.heading('#3', text='Time')
        self.tree.heading('#4', text='DAY')

        # Specify attributes of the columns (We want to stretch it!)
        self.tree.column('#0', stretch=tk.YES)
        self.tree.column('#1', stretch=tk.YES)
        self.tree.column('#2', stretch=tk.YES)
        self.tree.column('#3', stretch=tk.YES)
        self.tree.column('#4', stretch=tk.YES)

        self.tree.place(x=80, y=350)
        self.treeview = self.tree

        self.id = 0
        self.iid = 0

    def back2(self):
        self.root.destroy()
        import logged



    def insert_data(self):
        day = datetime.now()
        time = day.strftime('%H:%M')
        self.treeview.insert('', 'end', iid=self.iid, text="Signed_In" + str(self.id),
                             values=(self.name_entry.get(),
                                     self.box.get(),time, day))
        self.iid = self.iid + 1
        self.id = self.id + 1


    def delete_data(self):
        row_id = int(self.tree.focus())
        self.treeview.delete(row_id)


app = Application(tk.Tk())
app.root.mainloop()
