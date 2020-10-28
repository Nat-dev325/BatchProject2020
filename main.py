'''
-Documentation here-
'''
import menu
import os
toys = [
    {"Name":"Woody","Species":"Human","Height":15.8,"NumFeet":2,"FirstAppearance":1},
    {"Name":"Jessie","Species":"Human","Height":13.4,"NumFeet":2,"FirstAppearance":2},
    {"Name":"Buzz Lightyear","Species":"Human","Height":11.43,"NumFeet":2,"FirstAppearance":1}
]
os.system("cls")
#This is the start of the main function
while True: #This loop is to ensure that the program does not just terminate after a single command
    command = menu.menu()
    
    if command == 1:
        menu.search_toys(toys)
    elif command == 2:
        menu.declutter(toys)
    elif command == 3:
        menu.addToys(toys)
    elif command == 4:
        menu.edit_toy(toys)
    elif command == 5:
        menu.playtime(toys)
    elif command == 6:
        menu.select_toy(toys)
    elif command == 7:
        menu.print_toys(toys)
    elif command == 8:
        menu.save(toys)
    elif command == 9:
        menu.load(toys)
    elif command == 10:
        print(
            "\n================================================\n"
            + "It's bedtime! Sleep dreams!\n"
            + "================================================\n"
            )
        break