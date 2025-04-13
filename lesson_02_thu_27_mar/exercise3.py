# menu using mtch-case

# all the avaible operations
print("""
    1. Add \n
    2. Subtract \n
    3. Multiply \n
    4. Divide
    """)

operation = int(input("Enter the operation you wanna do (1-4): "))
a = int(input("Enter the first number a: "))
b = int(input("Enter the first number b: "))

# menu using match-case
match operation:
    case 1:
        print(f"{a} + {b} =",a+b)
    case 2:
        print(f"{a} - {b} =",a-b)
    case 3:
        print(f"{a} * {b} =",a*b)
    case 4:
        if b == 0:
            print("Zero Error Division")
        else:
            print(f"{a} / {b} =",a/b)
    case _:
        print("End session...")        