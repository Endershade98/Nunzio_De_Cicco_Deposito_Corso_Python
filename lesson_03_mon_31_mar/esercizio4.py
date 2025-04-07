number_elements = input("Enter the number of elements you want to list: ")
number_list = []

if number_elements <= 0:
    print("It isn't a correct number!")
else:
    condition = input("What kind of element do you want to enter? [True, False, string, number]" )
    if condition == "bool":
        number_list.append(True)
    for i in range(number_elements):
        list_element = input("Enter an element: ")
        number_list.append(list_element)
    
for i in number_list: # search the max number in a list
    if i == max(number_list):
        print(i)
        
counter = 0
while i < len(number_list): # 
    if type(i) == float or type(i) == int:
        counter += 1



    