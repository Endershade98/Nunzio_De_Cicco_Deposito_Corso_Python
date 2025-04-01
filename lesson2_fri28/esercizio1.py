# esercizio1

number = int(input("Enter a number: "))

if number%2 == 0:# verifies a number is odd 
    print(number, "is odd")
    
    number = int(input("Enter a number: "))
    
    if number == 1:# verifies a number is one
        print("Wow it is one!")
        
        number = int(input("Enter a number: "))
        
        if number == 0:# verifies a number is zero
            print("It is zero. Obviously!")
        else:
            print("not avaible number") # raise an exception
    else:
        print("not avaible number") # raise an exception
else:
    print("not avaible number") # raise an exception