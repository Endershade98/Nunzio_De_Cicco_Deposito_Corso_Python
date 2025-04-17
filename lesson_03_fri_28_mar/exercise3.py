# using if-elif-else create a pseudo account using a list or nested lists

condition = input("Do you want to create a new account (True/False): ")


if condition == "True":# star the main control flow to create your account
    account = []
    print("Create your new account...")
    name = input("Enter your name: ")# name required
    _password = input("Enter your password: ")# password required
    _id = input("Enter your id: ")# id required
    print("We are verify your account already exists or not. Please stand by...")
    if name in account or _id in account: # verifies your account already exists
        print("An account with", "Name: "+name, "ID:"+_id)# raises an exception
        print("Already exist!")
        print(account)
    else:# finally creatre a new account
        account.append(name)# add your name
        account.append(_password)# add your password
        account.append(_id)# add your ID
        print("Account successfully created!")
        print(account)
elif condition == "False":
    print("You can not create a new account!")
else: 
    print("Option not avaible!")
    

