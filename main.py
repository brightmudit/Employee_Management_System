from tkinter import *
from tkinter import ttk

# Window configure
root = Tk()
root.title("Employee Management System")

# Creating main frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Name label
ttk.Label(mainframe, text="Name").grid(column=1, row=1, sticky=E)
# Name Entry widget
name = StringVar()
name_entry = ttk.Entry(mainframe, width=30, textvariable=name)
name_entry.grid(column=2, row=1, sticky=(E, W))

# Password label
ttk.Label(mainframe, text="Password").grid(column=1, row=2, sticky=E)
# Password Entry widget
password = StringVar()
password_entry = ttk.Entry(mainframe, width=16, textvariable=password)
password_entry.grid(column=2, row=2, sticky=(E, W))
password_entry.configure(show="*")

# Log in button
ttk.Button(mainframe, text="Log in").grid(column=2, row=3, sticky=(E, W))

# Final touches
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
name_entry.focus()

# Starting mainloop
root.mainloop()