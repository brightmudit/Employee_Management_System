from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
import mysql.connector

class EmployeeManagement:

    def __init__(self, root):
        root.title("Employee Management System")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Style object
        s = ttk.Style()
        s.configure('mainframe.TFrame', background='red')
        s.configure('dashboard.TFrame', background='blue')
        s.configure('admin.TButton', font=('Times New Roman', 15))
        s.configure('employee.TButton', font=('Times New Roman', 15))


        # Creating main frame
        self.mainframe = ttk.Frame(root, style='mainframe.TFrame')
        # Dasboard frame
        self.dashboard = ttk.Frame(root, style='dashboard.TFrame')

        # Render main frames
        for frame in (self.mainframe, self.dashboard):
            frame.grid(column=0, row=0, sticky=(N,S,E,W))
            frame.columnconfigure(0, weight=1)
            frame.rowconfigure(0, weight=1)

        # Content frame (part of mainframe window from line 31 to 57)
        content_frame = ttk.Frame(self.mainframe, padding=60, borderwidth=2, relief='sunken')
        content_frame.grid(column=0, row=0)
        content_frame.columnconfigure(0, weight=1)
        content_frame.rowconfigure(0, weight=1)
        # Name label
        ttk.Label(content_frame, text="Name", font=('Times New Roman', 30)).grid(column=1, row=1, sticky=E)
        # Name Entry widget
        self.name = StringVar()
        self.name_entry = ttk.Entry(content_frame, width=30, textvariable=self.name, font=('Times New Roman', 15))
        self.name_entry.grid(column=2, row=1, sticky=(E, W))

        # Password label
        ttk.Label(content_frame, text="Password", font=('Times New Roman', 30)).grid(column=1, row=2, sticky=E)
        # Password Entry widget
        self.password = StringVar()
        self.password_entry = ttk.Entry(content_frame, width=16, textvariable=self.password,  font=('Times New Roman', 15))
        self.password_entry.grid(column=2, row=2, sticky=(E, W))
        self.password_entry.configure(show="*")

        # Log in button
        ttk.Button(content_frame, text="Log in", command=self.logIn).grid(column=2, row=3, sticky=(E, W))

        # Final touches
        for child in content_frame.winfo_children():
            child.grid_configure(padx=15, pady=15)
        self.name_entry.focus()

        # Dashboard frame contents
        db_content_frame = ttk.Frame(self.dashboard, padding=50, borderwidth=2, relief='sunken')
        db_content_frame.grid(column=0, row=0)
        db_content_frame.columnconfigure(0, weight=1)
        db_content_frame.rowconfigure(0, weight=1)

        admin_btn = ttk.Button(db_content_frame, text='Admin', style='admin.TButton')
        admin_btn.grid(column=0, row=0, ipadx=25, ipady=50)

        employee_frame = ttk.Button(db_content_frame, text='Employee', style='employee.TButton')
        employee_frame.grid(column=1, row=0, ipadx=25, ipady=50)

        back_btn = ttk.Button(db_content_frame, text='Go back', command=self.goBack)
        back_btn.grid(column=0, row=2, columnspan=2, sticky=(E,W))
        
        # Final touches
        for child in db_content_frame.winfo_children():
            child.grid_configure(padx=15, pady=15)

        self.showFrame(self.mainframe)

    def logIn(self):
        try:
            name_value = str(self.name.get())
            password_value = str(self.password.get())

            conn = mysql.connector.connect(host='localhost', user=name_value, passwd=password_value, database='employee_database')

            if conn.is_connected():
                print('Connected to MySQL database')
                self.name_entry.delete(0, END)
                self.password_entry.delete(0, END)
                self.showFrame(self.dashboard)

        except Exception as e:
            messagebox.showerror('Log in fail', 'Incorrect Name or Password. Please check again')
            self.name_entry.delete(0, END)
            self.password_entry.delete(0, END)

    def showFrame(self, frame):
        frame.tkraise()

    
    def goBack(self):
        self.showFrame(self.mainframe)



root = Tk()
app = EmployeeManagement(root)

# Starting mainloop
root.mainloop()