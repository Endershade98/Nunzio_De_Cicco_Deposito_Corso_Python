# use the crud method to modify a list of elements

number = input("Enter a number: ") # select a menu choise

my_list = ["1", "2", "3", "4"] # menu command list

elements = ["zero", "one", "two", "three"] # list of avaible elements

if my_list[0] == "1":# first command
    print("create a element")
    elements.append("one")
    
elif my_list[1] == "2":# second command
    print("delete a element")
    elements.remove("two")
    
elif my_list[2] == "3":# third command
    print("retrive a element")
    elements.insert(2, "three")

else:# forth command
    print("no choise avaible")
    