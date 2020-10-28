#This contains all of the functions for main.py
import sort

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

def search_toys(toys):
    return None
def declutter(toys):
    return None
def add_toy(toys):
    return None
def edit_toy(toys_list): #toys_list should be the list containing the dictionaries
	toys = toys_list
	#function within a function in order to access the names in the list of toys
	def get_names(): 
		toys_names=[] #places names in a list and returns a list
		for index in range(len(toys)):
			toys_names.append(toys[index]["Name"].lower())
		return toys_names

	#function in order to get the index of toy with the variable "name"
	def get_index(name): 
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
		toy_name = input("\nEnter toy's name: ")

		#shows the list of toys if toy is not found
		if toy_name.lower() not in get_names(): 
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
			
			#CODE BLOCK FOR CHANGING TOY NAME
			if command == 1: 
				new_toys_name = input("\nWhat is your toy's new name? ") 

				#checks if there is already a toy in the list of toys with that name
				if new_toys_name.lower() in get_names(): 
					print("That toy already exists!")
			
				else: 	#updates the dictionary of index from function get_index() and the key of "Name"
					toys[get_index(toy_name)]["Name"] = new_toys_name 
					print("Toy's name successfully edited!")
					toy_name = new_toys_name #needed part in order to update the variable toy_name
			
			#CODE BLOCK FOR CHANGING TOY SPECIES
			elif command == 2:
				#updates the dictionary of index from function get_index() and the key of "Species"
				toys[get_index(toy_name)]["Species"] = input("\nWhat is your toy's new species? ") 
				print("Species attribute successfully edited!")
			
			#CODE BLOCK FOR CHANGING TOY HEIGHT
			elif command == 3:
				 #updates the dictionary of index from function get_index() and the key of "Height"
				toys[get_index(toy_name)]["Height"] = float(input("\nWhat is your toy's new height? "))
				print("Height attribute successfully edited!")
			
			#CODE BLOCK FOR CHANGING TOY FEET
			elif command == 4:
				toys[get_index(toy_name)]["NumFeet"] = int(input("\nWhat is your toy's new number of feet? "))
				print("Number of feet attribute successfully edited!")
			
			#CODE BLOCK FOR CHANGING MOVIE APPEARANCE
			elif command == 5:
				#updates the dictionary of index from function get_index() and the key of "FirstAppearance"
				movie_number = int(input("\nWhat Toy Story movie did the toy first appear? "))
				if movie_number < 5 and movie_number > 0:
					toys[get_index(toy_name)]["FirstAppearance"] = movie_number
					print("First Movie Appearance attribute successfully edited!")
				else:
					print("Changes failed. Valid inputs are only 1, 2, 3, or 4")
			
			#CODE BLOCK TO EXIT EDITING
			elif command == 0:
				print("\n\nChanges have been saved!\nCurrent toy details are as follows:\n")
				
				#For loop to go through all attributes of said toy for printing
				for attribute in toys[get_index(toy_name)]:
					if attribute == "FirstAppearance":
						print("First Seen in Toy Story", toys[get_index(toy_name)][attribute], end="")
					else: 
						print(attribute+":", toys[get_index(toy_name)][attribute], end="\n")
				print("\n\n")
				return toys[get_index(toy_name)]
		
		except:
			print("There seems to be an error in the input") #if there is an error, print this. Example: if a string was given for height

def playtime(toys):
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
    if command == 1:
        toys = sort.BubbleSort(toys)
    elif command == 2:
        toys = sort.MergeSort(toys)
    elif command == 3:
        toys = sort.InsertionSort(toys)
    elif command == 4:
        toys = sort.SelectionSort(toys)
    elif command == 5:
        toys = sort.QuickSort(toys)
    print(sort.display(toys))
    return toys

def select_toy():
    return None
def print_toys():
    return None

def save(toys):

    fileHandler = open ("toys.txt", "w")				#make/access the file 'toys.txt' with writable mode
    for i in range (len(toys)):							#for every element in the list 'toys'
        name = toys[i]['Name']							#save the value of the current element 'Name' to name
        species = toys[i]['Species']					#same
        height = str(toys[i]['Height'])					#same
        feet = str(toys[i]['NumFeet'])					#same
        firstappearance = str(toys[i]['FirstAppearance']) #same
        fileHandler.write(name + ',' + species + ',' + height + ',' + feet +  ',' + firstappearance + '\n')
    													#write the data in the file
    fileHandler.close()
    return toys

def load(toys):
    fileHandler = open ("toys.txt", "r")				#access the file 'toys.txt' with read mode
    toys.clear()										#clear the existing elements to have the file data only
    for line in fileHandler:							#accessing every line in the file						
        toy_data = line[:-1].split(",")					#make list's elements by splitting using ","
        dict_toy = {}									#create a dict that will contain the current line data
        dict_toy["Name"] = toy_data[0]					#saving the specific data into its keys
        dict_toy["Species"] = toy_data[1]
        dict_toy["Height"] = toy_data[2]
        dict_toy["NumFeet"] = toy_data[3]
        dict_toy["FirstAppearance"] = toy_data[4]
        toys.append(dict_toy)							#appending the current line's dict to the main list 'toys'
    fileHandler.close()
    return toys