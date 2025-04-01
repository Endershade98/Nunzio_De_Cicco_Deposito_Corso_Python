import random as rd


my_number = int(input("Enter your number: "))

#def is_right(func)

def is_my_number(n: int) -> bool:
    """returns True if my number is n otherwise False"""
    if my_number == n:
        return True
    else:
        return False
    
def is_lower_or_greater(n: int, m: int) -> bool:
    """verifies if n if greater or lower than m"""
    if n > m:
        return True
    elif n < m:
        return False
    else:
        return is_my_number(n)
    
    
def drop_random_number(n: int) -> int:
    """returns a random number between 1 and 100"""
    n = 100
    for _ in range(1, n+1):
        resut = rd.randint(1, n+1)
    return resut

while is_my_number(my_number) != drop_random_number():
    if is_lower_or_greater == True:
        print(my_number, "is greater than", drop_random_number())
    elif is_lower_or_greater == False:
        print(my_number, "is lower than", drop_random_number())
    else:
        