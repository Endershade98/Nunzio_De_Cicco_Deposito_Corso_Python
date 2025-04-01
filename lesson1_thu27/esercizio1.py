age = int(input("How old are you? "))


if age <= 0: # verifies the age is avaible
    print("your age is not avaible")
elif 1 <= age < 18:
    print("I'm sorry. You can't watch this movie")
elif 18 <= age <= 120: # verifies you have the correct age
    print("You can watch this movie")
else:
    print("Your age is not avaoble")
    age_check = int(input("Plese show your ID Card"))



