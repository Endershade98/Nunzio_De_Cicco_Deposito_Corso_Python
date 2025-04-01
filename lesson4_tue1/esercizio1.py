n = int(input("Enter a positive number: "))

# this loop is build to better select a positive number
while n <= 0:
    # verifies n is not a positive number
    if n < 0:
        print(n, "is a negative number! Please enter a positive number.")
        n = input("Enter a positive number: ")
    elif n == 0:
        print(n, "is zero! Please enter a positive number.")
        n = input("Enter a positive number: ")
    # if n is not negative or zero is executed this block
    else:
        print(n, "is a positive number.")
        
even_sum = 0
odd_numbers = [] 
# the for loop verifies n is an even or an odd number
for i in range(n+1):
    if i % 2 == 0: # is even 
        even_sum += i
    elif i & 2 == 1: # is odd
        odd_numbers.append(i)
    else:
        continue
        
print(even_sum) # print the sum of even numbers
print(odd_numbers) # print the list of all odd numbers


sqrt_n = n**0.5
# verifies n is a prime number
for i in range(2, int(sqrt_n)+1):
    if n % i == 1:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number!")

