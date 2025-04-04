import random as rd


def square(n: float) -> float:
    """returns the square of n"""
    if type(n) == int or type(n) == float:
        result = n**2
        return result


def generate_list(number_elements: int) -> list:
    """returns a list of random numbers between a and b"""
    a = float(input("Enter a first number a: "))
    b = float(input("Enter a second number b: "))
    # generate the list of random numbers 
    numbers = [rd.uniform(a, b) for _ in range(number_elements)]
    return numbers

    
def sum_list(my_list: list) -> float:
    """returns the sum of the element stored in my_list"""
    result = 0
    # type checking
    if type(my_list) == list:
        for i in my_list:
            if type(i) == float or type(i) == int:
                result += i
    return result
            
def multiply_list(list1: list, list2: list) -> float:
    """_summary_

    Args:
        list1 (list): first list
        list2 (list): second list

    Returns:
        float: product of the elemments of both the lists
    """
    if len(list1) == len(list2):
        pass #@todo

print(square(5))
List1 = generate_list(6)
print(sum_list(List1))