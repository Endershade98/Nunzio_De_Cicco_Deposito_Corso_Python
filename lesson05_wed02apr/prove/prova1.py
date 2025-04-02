start = input("Do you wanna start this game? (y/N): ")


def show_menu() -> str:
    """returns the main menu"""
    print("1. Start")
    print("2. Open")
    print("3. Save")
    print("4. Exit")


def select(option: int) -> bool:
    """returns all the actions you can do and True if an option is avaible"""
    actions = [
        "1. you selected: Start",
        "2. You selected: Open",
        "3. You selected: Save",
        "4. Exit..."]
    if option in range(1, 4):
        if option == 1:
            print(actions[0])
        elif option == 2:
            print(actions[1])
        elif option == 3:
            print(actions[2])
        elif option == 4:
            print(actions[3])
        else:
            print("This action is not avaible!")
    return True


def square(n: int) -> int:
    """returns the square of n"""
    return n**2


def list_numbers(n: int) -> list:
    """returns the list of element between 1 and n"""
    numbers = []
    for i in range(n):
        numbers.append(i)
    return numbers

def is_prime(n: int) -> bool:
    """returns True if n is a prime number, False otherwise"""
    sqrt_n = n**0.5
    for i in range(1, int(sqrt_n)+1):
        if n % i == 1:
            return True
        else:
            return False

def check_type(variable) -> bool:
    """returns True if the variable has the correct type, False otherwise"""
    if type(variable) == int:
        print(variable, "is an int")
        print(variable, "is a base type")
        return True
    elif type(variable) == float:
        print(variable, "is a float")
        print(variable, "is a base type")
        return True
    elif type(variable) == str:
        print(variable, "is a string")
        print(variable, "is a base type... maybe")
        return True
    else:
        print(variable, "is not a base type")
        return False
    

# this loop shows the main menu
while start == "y":
    show_menu()
    choice = input("Select an option between (1-4): ")
    if select(choice) == "4":
        break
        
