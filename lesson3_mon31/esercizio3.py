print("====================Exercise1====================")

number = int(input("Enter a number: "))

if number < 0: # verifies number is not negative
    print(number, "is a negative number!")
else:
    if number % 2 == 0: # verifies number is even
        print(number, "is even")
    elif number % 2 == 1: # verifies number is odd
        print(number, "is odd")
    else: #raise an exception
        print(number, "isn't even or odd")
        print("Please try to enter another number.")



print("====================Exercise2====================")

pos_num = int(input("Enter a positive number: "))
condition = True

if pos_num <= 0:# verifies number is not negative or zero
    print(number, "is a negative number or zero!")
else:
    while condition: # the inifite loop using a True condition
        for i in range(pos_num+1, 0, -1): # printing numbers
            print(i)



print("====================Exercise3====================")

number_list = [1, 2, 3, 4]

for number in number_list:
    print(number**2) # print the number power of 2

