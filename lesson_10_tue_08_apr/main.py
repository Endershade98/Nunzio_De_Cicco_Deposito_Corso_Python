my_list = [1, 3, 4, 6, 7, 8]
filter = []

def even(n: int) -> bool:
    return n%2 == 1

def odd(n: int) -> bool:
    return n%2 == 0

filtered_list = [even(m) for m in my_list] #metodo1
filt_list = filter(even(), my_list) #metodo2
fil_list = []
