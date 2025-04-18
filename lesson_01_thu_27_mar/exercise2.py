# menu using if-elif-else

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

operation = input("Enter the operation you wanna do, select one of the following symbols ['+'', '-'', '*'', '/']: ")
operations = ["+", "-", "*", "/"]

if operation in operations: # first verification
    
    if operation == "+": # sum a and b
        print(a+b)
    elif operation == "-": # subtract a and b
        print(a-b)
    elif operation == "*": # multiply a and b
        print(a*b)
    elif operation == "/": # divide a by b
        if b == 0:
            print("Zero divisor error!")
        else:
            print(a/b)
    else:
        print("The operation is not avaible!") # exceptation