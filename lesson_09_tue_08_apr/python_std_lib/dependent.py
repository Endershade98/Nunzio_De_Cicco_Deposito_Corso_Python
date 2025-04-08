import random as rd


max_number = int(input("Enter the maximum number of numbers (51): "))
numbers_list = rd.sample(range(1, max_number), 5)

def range_number():
    
    while True:
        min = int(input("Enter a minimum number: "))
        max = int(input("Enter a maximum number: "))
        if max > min:
            numbers = [rd.sample(range(min, max)), ]


def number_string(list):
    string = ''.join(str(n) for n in numbers_list)
    return string

def enanched_open(mode, string):
    with open("testfile.txt", mode) as file:
        if mode == "w":
            file.write(string)
        elif mode == "r":
            file.read(string)
        
        
def guess_number(numb1, numb2):
    if numb1 and numb2 in numbers_list:
        print("You win")
    elif numb1 or numb2 in numbers_list:
        print("You lose")
    else:
        print("You gave up")
    
    

