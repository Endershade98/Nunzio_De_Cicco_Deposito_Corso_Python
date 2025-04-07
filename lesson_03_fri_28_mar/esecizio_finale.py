name = input("Enter your name: ")
_password = input("Enter your password: ")
_symbols = ["@", "#", "+"]

account = []

if name and _password in account:# verifies your name and password
    print("This name already exist! Select another one.")
else:# starting process 
    if _symbols[0] or _symbols[1] or _symbols[2] in _password:
        print("Your password is strong")
    elif name in account:# verifies your name
        print("you should select one of this symbols")
        print(_symbols[0], _symbols[1], _symbols[2])
        print("to make more secure your password")
    else:# finally creatre a new account
        account.append(name)# add your name
        account.append(_password)# add your password
        print(account)
        
    
