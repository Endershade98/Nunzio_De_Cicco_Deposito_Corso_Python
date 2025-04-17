# nested if-elif-else example

number = int(input("Enter a number: "))

if number%2 == 0:# verifies a number is odd 
    print(number, "is odd")
    
    if number == 1:# verifies the new number is one
        print("Wow it is one!")
        
        if number == 0:# verifies the new number is zero
            print("It is zero. Obviously!")
        else:
            print("not avaible number") # raise an exception
    else:
        print("not avaible number") # raise an exception
else:
    print("not avaible number") # raise an exception