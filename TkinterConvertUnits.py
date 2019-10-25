'''

Write a program that converts distances in kilometers to miles.
The task for this lab is to develop an Object Oriented GUI application
as a class that encapsulates the implementation of converting distances
in kilometers to miles. Display the result in an info dialog box.
Format floating point values to 2 decimal places.

Output: results as per lab spec.
Development Environment:  MAC home


'''

from tkinter import *
from tkinter import messagebox

# UserInut class inherits from tkinter Frame
class UserInput(Frame):
    # class init
    def __init__(self, master=None):
        Frame.__init__(self, master=None)
        self.master = master
        self.master.title("Convert Kilomenters to Miles")
        self.kin = Label(self.master,text="Enter Kilometers").grid(row=0)
        self.kin = Entry(self.master)
        self.kin.grid(row=0, column=1)

        self.convert = Button(self.master, text="Convert",command=self.convertme).\
            grid(row=3, column=0, sticky=W, pady=4)

        self.quit = Button(self.master, text="Quit",command=self.master.destroy).\
            grid(row=3, column=1, sticky=W, pady=4)

    def convertme(self):
        kilometers = self.kin.get()
        # messagebox.showerror(message=kilometers)
        # if conversion is succesful then method provides the output
        try:
            miles = round(float(kilometers) * float(0.62), 2)
            self.mileso = Label(self.master, text="Result in Miles").grid(row=1)
            self.mileso = Label(self.master, text=miles).grid(row=1, column=1)

        except ValueError as e:
            messagebox.showerror(message=kilometers + " is invalid input")


root = Tk()

root.geometry("400x200")
app = UserInput(root)
root.mainloop()