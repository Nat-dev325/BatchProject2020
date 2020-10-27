#This contains all of the functions for main.py
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
	global toys #to access and modify the global variable toys

	#function within a function in order to access the names in the list of toys
	def get_names(): 
		toys_names=[] #places names in a list and returns a list
		for index in range(len(toys)):
			toys_names.append(toys[index]["Name"].lower())
		return toys_names

	#function in order to get the index of toy with the variable "name"
	def get_index(name): 
		global toys
		index = 0
		for toy_dict in toys:
			if name.lower() == toy_dict["Name"].lower():
				return index
			else: index += 1

	#checks if there are toys in the first place. if none, ends the function
	if len(toys) == 0:
		return print("There are no toys to edit :(")

	toy_name = "" 

	#while loop to check if the toy name exists
	while toy_name.lower() not in get_names(): 
		toy_name = input("\nEnter toy's name. \nInput '0' to cancel editing\n")

		#Cancels editing the toy and skips the rest of the function
		if toy_name == "0": 
			return print("Successfully cancelled toy editing!")

		#shows the list of toys if toy is not found
		elif toy_name.lower() not in get_names(): 
			print("\nOh no! Toy not found :(\nYour toys are:\n")
			for dicts in toys:
				for attribute in dicts:
					if attribute == "FirstAppearance":
						print("(First Seen in Toy Story", dicts[attribute], end=")")
					else: print(attribute+":", dicts[attribute], end="\t")
				print()


	print("Toy found!")
	
	#try except while true loop so that one can edit multiple attributes
	while True: 
		try:
			print("""
Toy Attributes:
	1. Name
	2. Species
	3. Height
	4. Number of Feet
	5. Movie of Character's First Appearance
	0. Exit
			""")
			
			command = int(input("Which attribute do you want to edit?\nEnter command number: "))
			
			#CODE BLOCK FOR CHAGNING TOY NAME
			if command == 1: 
				new_toys_name = input("\nWhat is your toy's new name? ") 

				#checks if there is already a toy in the list of toys with that name
				if new_toys_name in get_names(): 
					print("That toy already exists!")
			
				else: 	#updates the dictionary of index from function get_index() and the key of "Name"
					toys[get_index(toy_name)]["Name"] = new_toys_name 
					print("Toy's name successfully edited!")
					toy_name = new_toys_name #needed part in order to update the variable toy_name
			
			#CODE BLOCK FOR CHAGNING TOY SPECIES
			elif command == 2:
				#updates the dictionary of index from function get_index() and the key of "Species"
				toys[get_index(toy_name)]["Species"] = input("\nWhat is your toy's new species? ") 
				print("Species attribute successfully edited!")
			
			#CODE BLOCK FOR CHAGNING TOY HEIGHT
			elif command == 3:
				 #updates the dictionary of index from function get_index() and the key of "Height"
				toys[get_index(toy_name)]["Height"] = float(input("\nWhat is your toy's new height? "))
				print("Height attribute successfully edited!")
			
			#CODE BLOCK FOR CHAGNING TOY FEET
			elif command == 4:
				toys[get_index(toy_name)]["Feet"] = int(input("\nWhat is your toy's new number of feet? "))
				print("Number of feet attribute successfully edited!")
			
			#CODE BLOCK FOR CHAGNING MOVIE APPEARANCE
			elif command == 5:
				#updates the dictionary of index from function get_index() and the key of "FirstAppearance"
				toys[get_index(toy_name)]["FirstAppearance"] = int(input("\nWhat Toy Story movie did the toy first appear? ")) 
				print("First Movie Appearance attribute successfully edited!")
			
			#CODE BLOCK TO EXIT EDITING
			elif command == 0:
				print("\n\nChanges have been saved!\nCurrent toy details are as follows:\n")
				
				#For loop to go through all attributes of said toy for printing
				for attribute in toys[get_index(toy_name)]:
					if attribute == "FirstAppearance":
						print("First Seen in Toy Story", toys[get_index(toy_name)][attribute], end="")
					else: 
						print(attribute+":", toys[get_index(toy_name)][attribute], end="\n")
				break
		
		except:
			print("There seems to be an error in the input") #if there is an error, print this. Example: if a string was given for height

def playtime():
    print(
        "\n==SUBMENU=======================================\n"
        + " (1)Bubble Sort\n"
        + " (2)Merge Sort\n"
        + " (3)Insertion Sort\n"
        + " (4)Selection Sort\n"
        + " (5)Quick Sort\n"
        + "================================================\n"
        )
    command_check = False
        while command_check == False: #This loop checks if the input is valid
            command = int(input("Enter command number(1-5): "))
            if command in range(1,6):
                    command_check = True
            return command
    if command == 1:
            print(BubbleSort(toys))
        elif command == 2:
            print(MergeSort(toys))
        elif command == 3:
            print(InsertionSort(toys))
        elif command == 4:
            print(SelectionSort(toys))
        elif command == 5:
            print(QuickSort(toys))
def select_toy():
def print_toys():
def save():
	fileHandler = open ("toys.txt", "w")				#make/access the file 'toys.txt' with writable mode
	for i in range (len(toys)):							#for every element in the list 'toys'
		name = toys[i]['Name']							#save the value of the current element 'Name' to name
		species = toys[i]['Species']					#same
		height = str(toys[i]['Height'])					#same
		feet = str(toys[i]['Feet'])						#same
		firstappearance = str(toys[i]['FirstAppearance']) #same
		fileHandler.write(name + ',' + species + ',' + height + ',' + feet +  ',' + firstappearance + '\n')
														#write the data in the file
	fileHandler.close() 								#close naten syepms

def load():
	fileHandler = open ("toys.txt", "r")				#access the file 'toys.txt' with read mode
	toys.clear()										#clear the existing elements to have the file data only
	for line in fileHandler:							#accessing every line in the file						
		toy_data = line[:-1].split(",")					#make list's elements by splitting using ","
		dict_toy = {}									#create a dict that will contain the current line data
		dict_toy["Name"] = toy_data[0]					#saving the specific data into its keys
		dict_toy["Species"] = toy_data[1]
		dict_toy["Height"] = toy_data[2]
		dict_toy["Feet"] = toy_data[3]
		dict_toy["FirstAppearance"] = toy_data[4]
		toys.append(dict_toy)							#appending the current line's dict to the main list 'toys'
	
	fileHandler.close()									#close naten ulit syemps

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