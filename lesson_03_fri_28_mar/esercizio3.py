
condition = bool(input("Do you want to create a new account (y/N): "))
account = []

if condition == True:# star the main control flow to create your account
    print("Create your new account...")
    name = input("Enter your name: ")# name required
    password = input("Enter your password: ")# password required
    _id = input("Enter your id: ")# id required
    if name and password and _id in account: # verifies your account already exists
        print("An account with", "Name: "+name, "Password: "+password, "ID:"+_id)# raises an exception
        print("Already exist!")
    else:# finally creatre a new account
        account.append(name)# add your name
        account.append(password)# add your password
        account.append(_id)# add your ID 
        print(account)
else:
    print("You can not create a new account!")
    

