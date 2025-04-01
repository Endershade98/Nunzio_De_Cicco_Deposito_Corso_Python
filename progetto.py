# def create_account():
# def log_in():
# def log_out():

def sign_in() ->list:
    """return an account """
    name = input("Enter your name: ")
    _password = input("Enter your password: ")
    _symbols = ["@", "#", "+"]
    registred_account = []
    # verifies your name and password
    if name and _password in registred_account:
        print("This name already exist! Select another one.")
    # starting process 
    else:
        if _symbols[0] or _symbols[1] or _symbols[2] in _password:
            print("Your password is strong")
        # verifies your name
        elif name in registred_account:
            print("you should select one of this symbols")
            print(_symbols[0], _symbols[1], _symbols[2])
            print("to make more secure your password")
        # finally creatre a new registred_account
        else:
            registred_account.append(name)# add your name
            registred_account.append(_password)# add your password
            registred_account.append(True)
            print(registred_account)


def has_a_secret(_password: str) -> bool:
    """returns True if you have a secret password, False otherwise"""
    if _password == "GHIBLI":
        return True
    else:
        return False

def is_logged(account:list) -> bool:
    """returns True if an account is logged, False otherwise"""
    if True in account:
        return True
    else:
        return False
    
