from tkinter import messagebox, simpledialog
def check_for_validity(item):
    while True:
        try:
            item = int(item)
            break
        except:
            messagebox.showerror("Critical Error",
                                 "You have entered an unrecognised character. Please restart the program. ")
            exit()
messagebox.showinfo("Welcome", "Welcome to the Python last digit finder made by Moeed Ali")
messagebox.showwarning("Warning", "Using large numbers may cause your computer to hang, crash or use excessive system resources.")
answer0 = (simpledialog.askstring("Base number", "Please enter the base number: "))
answer1 = (simpledialog.askstring("Exponent", "Enter the exponent: "))
check_for_validity(answer0)
check_for_validity(answer1)
answer0 = int(answer0)
answer1 = int(answer1)
number0 = (answer0 ** answer1)
num_str = repr(number0)
last_digit_str = num_str[-1]
last_digit = int(last_digit_str)
message = "The last digit is: " + str(last_digit)
messagebox.showinfo("Last digit", message)