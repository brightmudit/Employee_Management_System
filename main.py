from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from mysql import connector
import mysql.connector
from mysql.connector import connection_cext

class EmployeeManagement:

    def __init__(self, root):
        root.title("Employee Management System")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.mysql_name = 'root'
        self.mysql_password = 'noob'
        self.employees_data = []
        # Connection mysql
        self.connection = mysql.connector.connect(
                    host="localhost",
                    user=self.mysql_name,
                    passwd=self.mysql_password,
                    database="employee_database"
                    )
        self.cursor = self.connection.cursor()

        # Style object
        s = ttk.Style()
        s.configure('mainframe.TFrame', background='red')
        s.configure('dashboard.TFrame', background='blue')
        s.configure('label.TLabel', font=('Times New Roman', 30))
        s.configure('admin.TFrame', background='green')
        s.configure('employee_data.TFrame', background='yellow')
        s.configure('ademp.TButton', font=('Times New Roman', 30))
        s.configure('back.TButton', font=('Times New Roman', 15))
        s.configure('list.TButton', font=('Times New Roman', 15))

        # Creating main frame
        self.mainframe = ttk.Frame(root, style='mainframe.TFrame')
        # Dasboard frame
        self.dashboard = ttk.Frame(root, style='dashboard.TFrame')
        # Admin window frame
        self.admin = ttk.Frame(root, style='admin.TFrame')
        # View employee data frame
        self.employees_data_fr = ttk.Frame(root, style='employee_data.TFrame')

        # Render main frames
        for frame in (self.mainframe, self.dashboard, self.admin, self.employees_data_fr):
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
        ttk.Button(content_frame, text="Log in", command=self.logIn, style='back.TButton').grid(column=2, row=3, sticky=(E, W))

        # Final touches
        for child in content_frame.winfo_children():
            child.grid_configure(padx=15, pady=15)
        self.name_entry.focus()

        # Dashboard frame contents (part for dashboard window from line 63 to 82)
        db_content_frame = ttk.Frame(self.dashboard, padding=50, borderwidth=2, relief='sunken')
        db_content_frame.grid(column=0, row=0)
        db_content_frame.columnconfigure(0, weight=1)
        db_content_frame.rowconfigure(0, weight=1)

        admin_btn = ttk.Button(db_content_frame, text='Admin', style='ademp.TButton', command=self.raiseAdminWin)
        admin_btn.grid(column=0, row=0, ipadx=25, ipady=50)

        employee_btn = ttk.Button(db_content_frame, text='Employee', style='ademp.TButton')
        employee_btn.grid(column=1, row=0, ipadx=25, ipady=50)

        back_btn = ttk.Button(db_content_frame, text='Go back', command=lambda: self.goBack(self.mainframe), style = 'back.TButton')
        back_btn.grid(column=0, row=2, columnspan=2, sticky=(E,W))
        
        # Final touches
        for child in db_content_frame.winfo_children():
            child.grid_configure(padx=15, pady=15)

        self.showFrame(self.mainframe)

        # Admin window contents (part of admin window from line 85 to 118)
        admin_content_frame = ttk.Frame(self.admin, padding=30, borderwidth=2, relief='sunken')
        admin_content_frame.grid(column=0, row=0)
        admin_content_frame.columnconfigure(0, weight=1)
        admin_content_frame.rowconfigure(0, weight=1)

        # Employee menu frame
        employee_menu_fr = ttk.Frame(admin_content_frame, borderwidth=2, relief='sunken')
        employee_menu_fr.grid(column=0, row=0)
        ttk.Label(employee_menu_fr, text='Employee Menu', style='label.TLabel').grid(column=0, row=0)
        ttk.Button(employee_menu_fr, text='1. View employees data', style='list.TButton', command=self.raiseViewEmployeeWin).grid(column=0, row=1)
        ttk.Button(employee_menu_fr, text='2. Add a new employee', style='list.TButton').grid(column=0, row=2)
        ttk.Button(employee_menu_fr, text='3. Delete an employee', style='list.TButton').grid(column=0, row=3)
        ttk.Button(employee_menu_fr, text='4. Update data of an employee', style='list.TButton').grid(column=0, row=4)
        # Attendence menu frame
        attendence_menu_fr = ttk.Frame(admin_content_frame, borderwidth=2, relief='sunken')
        attendence_menu_fr.grid(column=1, row=0, sticky=(N,S))
        ttk.Label(attendence_menu_fr, text='Attendence Menu', style='label.TLabel').grid(column=0, row=0)
        ttk.Button(attendence_menu_fr, text='1. View Attendence', style='list.TButton').grid(column=0, row=1)
        ttk.Button(attendence_menu_fr, text='2. Mark absent/present', style='list.TButton').grid(column=0, row=2)

        # Go back button
        back_btn = ttk.Button(admin_content_frame, text='Go back', command=lambda: self.goBack(self.dashboard), style='back.TButton')
        back_btn.grid(column=0, row=1, columnspan=2, sticky=(E,W))

        # Final touches
        for child in admin_content_frame.winfo_children():
            child.grid_configure(padx=20, pady=20)
        for child in employee_menu_fr.winfo_children():
            child.grid_configure(padx=6, pady=12)
        for child in attendence_menu_fr.winfo_children():
            child.grid_configure(padx=6, pady=12)

        # View employess data window contents
        data_content_fr = ttk.Frame(self.employees_data_fr, padding=30, borderwidth=2, relief='sunken')
        data_content_fr.grid(column=0, row=0)
        data_content_fr.columnconfigure(0, weight=1)
        data_content_fr.rowconfigure(0, weight=1)

        # Fething employess data
        self.cursor.execute('SELECT * FROM employee')
        self.employees_data = self.cursor.fetchall()
        # Adding column heading
        ttk.Label(data_content_fr, width=20, text='EId', borderwidth=1, relief=RIDGE, background='yellow').grid(row=0, column=0)
        ttk.Label(data_content_fr, width=20, text='Name', borderwidth=1, relief=RIDGE, background='yellow').grid(row=0, column=1)
        ttk.Label(data_content_fr, width=20, text='Gender', borderwidth=1, relief=RIDGE, background='yellow').grid(row=0, column=2)
        ttk.Label(data_content_fr, width=20, text='Age', borderwidth=1, relief=RIDGE, background='yellow').grid(row=0, column=3)
        ttk.Label(data_content_fr, width=20, text='Salary', borderwidth=1, relief=RIDGE, background='yellow').grid(row=0, column=4)
        ttk.Label(data_content_fr, width=20, text='Bonus', borderwidth=1, relief=RIDGE, background='yellow').grid(row=0, column=5)
        ttk.Label(data_content_fr, width=20, text='Department', borderwidth=1, relief=RIDGE, background='yellow').grid(row=0, column=6)
        i = 1
        for employee in self.employees_data:
            for j in range(len(employee)):
                e = ttk.Label(data_content_fr, width=20, text=employee[j])
                e.grid(row=i, column=j)
            i += 1
        
    def logIn(self):
        name= str(self.name.get())
        password = str(self.password.get())
        if name == self.mysql_name and password == self.mysql_password:
            print('Connected to MySQL database')
            self.name_entry.delete(0, END)
            self.password_entry.delete(0, END)
            self.showFrame(self.dashboard)
        else:
            messagebox.showerror('Log in fail', 'Incorrect Name or Password. Please check again')
            self.name_entry.delete(0, END)
            self.password_entry.delete(0, END)

    def showFrame(self, frame):
        frame.tkraise()

    
    def goBack(self, frame):
        self.showFrame(frame)

    def raiseAdminWin(self):
        self.showFrame(self.admin)

    def raiseViewEmployeeWin(self):
        self.showFrame(self.employees_data_fr)


root = Tk()
app = EmployeeManagement(root)

# Starting mainloop
root.mainloop()