'''
-Documentation here-
'''

#This is the start of the main function
while True: #This loop is to ensure that the program does not just terminate after a single command
    command = menu()
    
    if command == 1:
        search_toys(toys)
    elif command == 2:
        declutter(toys)
    elif command == 3:
        add_toy(toys)
    elif command == 4:
        edit_toy(toys)
    elif command == 5:
        playtime(toys)
    elif command == 6:
        select_toy(toys)
    elif command == 7:
        print_toys(toys)
    elif command == 8:
        save(toys)
    elif command == 9:
        load(toys)
    elif command == 10:
        print(
            "\n================================================\n"
            + "It's bedtime! Sleep dreams!\n"
            + "================================================\n"
            )
        break