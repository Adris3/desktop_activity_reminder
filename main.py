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


root.mainloop()
