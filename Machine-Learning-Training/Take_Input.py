a=input('Enter a value: ') 
print(a)
#Take any input from the user and print it (note: input() function always returns a string)

try:
    b=int(input('Enter an integer: '))
    #Use the int() function to convert the input string to an integer
    print(b)
except ValueError:
    print("Invalid input. Please enter an integer.")
#Use a try-except block to handle the case where the user does not enter a valid integer

try:
    c=float(input('Enter a float: '))
    #Use the float() function to convert the input string to a float
    print(c)
except ValueError:
    print("Invalid input. Please enter a float.")

try:
    d=bool(input('Enter a boolean value (True or False): '))
    #Use the bool() function to convert the input string to a boolean
    print(d)
except ValueError:
    print("Invalid input. Please enter a boolean value.")