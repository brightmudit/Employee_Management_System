from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
import mysql.connector

def logIn():
    try:
        name_value = str(name.get())
        password_value = str(password.get())

        conn = mysql.connector.connect(host='localhost', user=name_value, passwd=password_value, database='employee_database')

        if conn.is_connected():
            print('Connected to MySQL database')
            name_entry.delete(0, END)
            password_entry.delete(0, END)

    except Exception as e:
        messagebox.showerror('Log in fail', 'Incorrect Name or Password. Please check again')
        name_entry.delete(0, END)
        password_entry.delete(0, END)

# Window configure
root = Tk()
root.title("Employee Management System")

# Creating main frame
mainframe = ttk.Frame(root, padding=60, borderwidth=2, relief='sunken')
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Name label
ttk.Label(mainframe, text="Name", font=('Times New Roman', 30)).grid(column=1, row=1, sticky=E)
# Name Entry widget
name = StringVar()
name_entry = ttk.Entry(mainframe, width=30, textvariable=name, font=('Times New Roman', 15))
name_entry.grid(column=2, row=1, sticky=(E, W))

# Password label
ttk.Label(mainframe, text="Password", font=('Times New Roman', 30)).grid(column=1, row=2, sticky=E)
# Password Entry widget
password = StringVar()
password_entry = ttk.Entry(mainframe, width=16, textvariable=password,  font=('Times New Roman', 15))
password_entry.grid(column=2, row=2, sticky=(E, W))
password_entry.configure(show="*")

# Log in button
ttk.Button(mainframe, text="Log in", command=logIn).grid(column=2, row=3, sticky=(E, W))

# Final touches
for child in mainframe.winfo_children():
    child.grid_configure(padx=15, pady=15)
name_entry.focus()

# Starting mainloop
root.mainloop()