# how does import work
import my_module as mm #alias


x_copy = mm.x
print(x_copy) 

new_var = mm.somma(2, 3)
print(new_var)

circle_example = mm.Circle(2.5)
print(circle_example.area())