"""
-Documentation here-
"""
import menu
import os

# Initialize an empty list
toys = []
os.system("cls")
# This is the start of the main function
while (
    True
):  # This loop is to ensure that the program does not just terminate after a single command
    command = menu.menu()

    if command == 1:
        menu.searchToy(toys)
    elif command == 2:
        toys = menu.declutter(toys)
    elif command == 3:
        added_toy = menu.addToys(toys)
        if added_toy != None:
            toys.append(added_toy)
    elif command == 4:
        menu.edit_toy(toys)
    elif command == 5:
        menu.playtime(toys)
    elif command == 6:
        selected_toy = menu.select_toy(toys)
    elif command == 7:
        menu.print_toy(toys)
    elif command == 8:
        menu.save(toys)
    elif command == 9:
        toys = menu.load(toys)
    elif command == 0:
        print(
            """\n================================================
 It's bedtime! Sweet dreams!
================================================"""
        )
        break