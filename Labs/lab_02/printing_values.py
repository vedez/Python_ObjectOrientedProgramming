# Description: Printing the values of each given variable and guessing what will be displayed when printed

print("Question 7")
int_a = 27
int_b = 5
int_a = 6

print(int_a)  # This will print '6' instead of '27' as a new value has been assigned to int_a in line 6
print(int_b + 5)  # This will print '10' (6 + 5)
print(int_b)  # This will print '5' and not 11 as the operation of adding 5 occurred within the print statement

print("Question 8")
a_float = 2.5
a_int = 7
b_int = 6

print(a_int / b_int)  # This will print a float number
print(a_int // a_float)
# This will print a float despite using '//',
# if we're using both int and a float - the system will continue to print the result as a float
print(a_int % b_int)  # This will print an int - '1'
print(int(a_float))  # This converts the float variable to an int - '2'
print(float(a_int))  # This converts the int number to a float - '7.0'

print("Question 9")
a_int = 10
b_int = 3
c_int = 2

print(a_int + b_int * c_int)  # Prints '16'
print((a_int + b_int) * c_int)  # Prints '26'
print(b_int ** c_int)  # Prints '9'

