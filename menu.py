'''
-Documentation here-
'''

#This is the start of the main function
def menu():
    print(
		"\n==MENU==========================================\n"
		+ " (1)Search for Toys\n"
		+ " (2)Declutter\n"
		+ " (3)Add Toy\n"
		+ " (4)Edit Toy\n"
		+ " (5)Playtime\n"
    + " (6)Select Toy\n"
    + " (7)Print Toys\n"
		+ " (8)Save Current Lineup\n"
		+ " (9)Load Last Lineup\n"
		+ " (10)Bedtime\n"
		+ "================================================\n"
		)
    command_check = False
    while command_check == False: #This loop checks if the input is valid
        command = int(input("Enter command number(1-10): "))
        if command in range(1,11):
            command_check = True
    return command

def search_toys():
def declutter():
def add_toy():
def edit_toy():
def playtime():
def select_toy():
def print_toys():
def save():
def load():

toys = [
    {"Name":"Woody","Species":"Human","Height":15.8,"Feet":2,"FirstAppearance":1},
    {"Name":"Jessie","Species":"Human","Height":13.4,"Feet":2,"FirstAppearance":2},
    {"Name":"Buzz Lightyear","Species":"Human","Height":11.43,"Feet":2,"FirstAppearance":1}
]
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
