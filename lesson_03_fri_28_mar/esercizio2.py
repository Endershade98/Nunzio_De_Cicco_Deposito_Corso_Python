number = int(input("Enter a number: ")) # select a menu choise

my_list = ["1", "2", "3", "4"] # menu command list

elements = [] # list of avaible elements

if number[0] == "1":# first command
    print("create a element")
    elements.append(1)
    
elif number[1] == "2":# second command
    print("delete a element")
    my_list.remove("due")
    
elif number[2] == "3":# third command
    print("retrive a element")
    my_list.insert(2, "tre")

else:# forth command
    print("no choise avaible")
    