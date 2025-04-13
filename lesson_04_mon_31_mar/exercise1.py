number = int(input("Enter an integer number: "))

if number < 0: # exceptation handling
    print("This is a negative number!")
else:# this is the main code flow
    for index in range(number, 0, -1): # the for loop is used to print 
        print(index)
    question = input("Do you wanna changer your number? (y/N): ")
    if question == "y": # continue
        number = int(input("Please enter a new integer number: "))
    elif question == "N": # do not continue
        print("You are not selected a new number.")
    else:
        print("This option is not avaible!")
        print("Please select an avaible option...")