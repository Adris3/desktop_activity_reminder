import time
from tkinter import *

# Create Tk Window
root = Tk()

# Set window size
root.geometry("300x250")

# Set title
root.title("Desktop Activity Reminder")

# Time variables
hour = StringVar()
minute = StringVar()
second = StringVar()

# Set default values as zero
hour.set("00")
minute.set("00")
second.set("00")

# Getting input from user with Entry class
hourEntry = Entry(root, width=3, font=("Arial", 18, ""),textvariable=hour)
minuteEntry = Entry(root, width=3, font=("Arial", 18, ""),textvariable=minute)
secondEntry = Entry(root, width=3, font=("Arial", 18, ""),textvariable=second)

hourEntry.place(x=80, y=20)
minuteEntry.place(x=130, y=20)
secondEntry.place(x=180, y=20)



root.mainloop()
