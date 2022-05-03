from tkinter import messagebox, simpledialog
messagebox.showinfo("Welcome", "Welcome to the Python last digit checker made by Moeed Ali")
messagebox.showwarning("Warning", "Using large numbers may cause your computer to hang, crash or use excessive system resources.")
answer0 = int(simpledialog.askstring("Base number", "Enter the base number: "))
answer1 = int(simpledialog.askstring("Exponent", "Enter the exponent: "))
number0 = (answer0 ** answer1)
num_str = repr(number0)
last_digit_str = num_str[-1]
last_digit = int(last_digit_str)
message = "The last digit is: " + str(last_digit)
messagebox.showinfo("Last digit", message)
# MADE BY MOEED ALI