# what is match case in python? How does it works
# you can use it whenever you wanna write a menu

command = input("Enter a command: ")

match command:
    case "start":
        print("avvio del programma")
    case "stop":
        print("termina il programma")
    case "pausa":
        print("metti in pausa il programma")
    case _:
        print("no command found")