def check_for_validity(item):
    while True:
        try:
            item = int(item)
            break
        except:
            print("You have entered an unrecognised character. Please restart the program. ")
            exit()
print("Welcome to the Python last digit checker made by Moeed Ali")
answer0 = input("Enter the base number: ")
answer1 = input("Enter the exponent: ")
check_for_validity(answer0)
check_for_validity(answer1)
answer0 = int(answer0)
answer1 = int(answer1)
number0 = (answer0 ** answer1)
num_str = repr(number0)
last_digit_str = num_str[-1]
last_digit = int(last_digit_str)
input("The last digit is ", last_digit)
# MADE BY MOEED ALI
