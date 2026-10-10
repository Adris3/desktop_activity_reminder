import time
from tkinter import *
from tkinter import messagebox

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

# Submit function
def submit():
    try:
        # check values
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input valid numbers")

    while temp > -1:
        min, sec = divmod(temp, 60)

        hours = 0
        if min > 60:
            hours, min = divmod(min, 60)

        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(min))
        second.set("{0:2d}".format(sec))

        # update the GUI
        root.update()
        time.sleep(1)

        if (temp == 0):
            messagebox.showinfo("Time's up")

        temp -= 1

# Button for starting the countdown
btn = Button(root, text="Set Time", bd = '5', command= submit)
btn.place(x = 70, y = 120)


root.mainloop()
