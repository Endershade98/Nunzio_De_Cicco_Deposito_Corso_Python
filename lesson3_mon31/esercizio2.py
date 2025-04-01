number = int(input("Enter an integer number: "))
prime_numbers = []
even_numbers = []

if number < 0:# exceptation handling
    print("This is a negative number!")
else:# this is the main code flow
    if number % 2 == 0:
        print(number, "is a even number")
        even_numbers.append(number)
    else:
        print(number, "is not an even number")
        question = input("Do you wanna know what kind of number it is? (y/N): ")
        if question == "y": # continue 
            sqrt_number = number**0.5
            for i in range(2, int(sqrt_number)+1):
                if number % i == 0:
                    print(number, "is a prime number!")
                    prime_numbers.append(number)
        elif question == "N": # do not continue
            print("You have not selected a new number.")
        else:
            print("This option is not avaible!")
            print("Please select an avaible option...")