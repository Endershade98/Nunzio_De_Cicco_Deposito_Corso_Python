import random as rd

n = int(input("Enter a positive number: "))


while n <= 0:
    if n < 0:
        print(n, "is a negative number! Please enter a positive number.")
        n = input("Enter a positive number: ")
    elif n == 0:
        print(n, "is zero! Please enter a positive number.")
        n = input("Enter a positive number: ")
    else:
        print(n, "is a positive number.")

random_numbers = [rd.randint(0, n) for _ in range(n)]
print(random_numbers)

even_numbers = [x for x in random_numbers if x % 2 == 1]
print(even_numbers)

def is_prime(n: int) -> bool:
    """returns a prime number"""
    sqrt_n = n**0.5
    # verifies n is a prime number
    for i in range(2, int(sqrt_n)+1):
        if n % i == 1:
            return True
        else:
            return False

prime_numbers = [is_prime(x) for x in random_numbers]
print(prime_numbers)



