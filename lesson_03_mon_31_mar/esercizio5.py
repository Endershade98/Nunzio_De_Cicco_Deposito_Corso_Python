print("====================Exercise1====================")

string = input("Do you want to enter a string? (y/N): ")
number = input("Do you want to enter a number? (y/N): ")
condition = input("Do you want to repeat the process? (y/N): ")

if condition == "y":
    if number == "y":
        n = input("Enter a number: ")
        if n % 2 == 0:
            print(n, "is an even number")
        elif n & 2 == 1:
            print(n, "is an odd number")
        else:
            print(n, "isn't an odd or even number")
    elif number == "N":
        condition = input("Do you want to repeat the poces? (y/N): ")
    else:
        print("Your element isn't a string or a number! Please try to enter it againg")

if string == "y":
    s = input("Enter a string: ")
    print(s, "is a string")
elif string == "N":
    input("Do you want to repeat the process? (y/N): ")
else:
    print("Your element isn't a string or a number! Please try to enter it againg")



print("====================Exercise2====================")

a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
prime_numbers = []
other_numbers = []

for i in range(a, b):
    sqrt_i = i**0.5
    for j in range(2, int(sqrt_i)+1):
        if i % j == 0:
            print(i, "is a prime number!")
            prime_numbers.append(i)
        else:
            print(i, "is not a prime number!")
            other_numbers.append(i)

# you should use all the element we have studied during this session: break continue pass, while for match-case