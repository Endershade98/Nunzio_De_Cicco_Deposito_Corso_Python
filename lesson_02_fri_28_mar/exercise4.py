# try to create an account without using OOP principles (functions and classes or dicts)
# you can only use if-elif-else and the lists

# what we need to create an account
name = input("Enter your name: ")
email = input("Enter your email: ")
_symbols = ["@", "#", "+"]
print("Build a strong password using the following symbols",_symbols[0], _symbols[1], _symbols[2])
_password = input("Enter your password: ")

# your pseudo account
account = []

# verifing your name and email
if name in account or email in account: 
    print("Your 'name' or 'email' are still used! Select another one please.")
# starting process 
else:
    if _symbols[0] in _password or _symbols[1] in _password or _symbols[2] in _password:
        print("Your password is strong")
        print("We are creating your account, please stand by...")
        # finally creatre a new account
        account.append(name) # add your name
        account.append(email) # add your email
        account.append(_password) # add your password
        print(account) # print your account 
        
    
