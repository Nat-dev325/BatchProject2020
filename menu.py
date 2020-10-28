#This contains all of the functions for main.py
import sort
import string

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

#function that removes a toy from the list
def declutter(toys):
    toy_name = input("\nWhat toy do you want to remove? ")
    #Finds the dictionary within the list that corresponds to the given input
    for each_toy in toys:
        if each_toy["Name"] == toy_name:
            print("\n"+toy_name, "has been removed from the shelf\n") #Indicates that the object has been removed
            for attribute in each_toy: #Displays the attributes of the object
                print(attribute + ":" +str(each_toy[attribute]) +",", end=" ")
            for i in range(len(toys)): #Delete/Removes the object from the list by finding a name that matches the given input  
                if toys[i]["Name"] == toy_name:
                    del toys[i]

                    return toys
            break   #prevents the iteration of the codes from "if each_toy" to "for i in range" and the else condition 
                    #from manifesting if the Name is not corresponding to the current value of the "for each_toy" conditional
    else: print(toy_name, "is not on the shelf") #Manifests when there is no corresponding object in the list

def addToys(collection):
    print("===========Adding Toy in Collection==========")
    # initialization of dictionary
    dictToy = {
        "Name": "",
        "Species": "",
        "Height": 0,
        "NumFeet": 0,
        "FirstAppearance": 0,
    }

    # input name
    name = input("Enter Toy Name: ")

    # force the user to input a valid value type (int) and valid number of feet (cannot be less than 1)
    while True:
        try:
            numFeet = int(input("Enter Toy Number of Feet: "))
            while numFeet < 1:
                numFeet = int(input("Invalid Input. \nEnter Toy Number of Feet: "))
            break
        except ValueError:
            print("Enter an integer.")

    # input species
    species = input("Enter Toy Species: ")

    # force the user to input a valid value type (float) and valid height (cannot be less than or equal to 0)
    while True:
        try:
            height = float(input("Enter Toy Height: "))
            while height <= 0:
                height = float(input("Invalid Input. \nEnter Toy Height: "))
            break
        except ValueError:
            print("Enter a number.")

    # force the user to input a valid value type (int) and valid first appearance (can only enter either 1, 2, 3, or 4)
    while True:
        try:
            firstAppearance = int(input("Enter Toy First Appearance: "))
            while firstAppearance < 1 or firstAppearance > 4:
                firstAppearance = int(
                    input("Invalid Input. \nEnter Toy First Appearance: ")
                )
            break
        except ValueError:
            print("Enter an integer.")

    # update the values in the dictionary
    # string.capwords(<string>) was used to capitalize only the first letter of each word
    dictToy["Name"] = string.capwords(name)
    dictToy["Species"] = string.capwords(species)
    dictToy["Height"] = height
    dictToy["NumFeet"] = numFeet
    dictToy["FirstAppearance"] = firstAppearance

    # add dictToy to the original list of dictionaries
    collection.append(dictToy)

    # notify the user that they have successfully added a toy
    print("\n" + name + " added in Collection!")

    # print the attributes of the toy
    print(dictToy)

    return collection

def edit_toy(toys_list): #toys_list should be the list containing the dictionaries
	print("==========EDITING TOYS IN SELECTION============")
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
			display = ""
			for i in range(0,len(toys)):
				for j in toys[i]:
					if j == "Name":
						display += str(j) + ": " + '{0: <15}'.format(str(toys[i][j]))
						continue
					if j == "Feet":
						display += str(j) + ": " + '{0: <6}'.format(str(toys[i][j]))
						continue
					display += str(j) + ": " + '{0: <16}'.format(str(toys[i][j]))
				display += "\n"
			print(display)
	print("Toy found!")

    #try except while true loop so that one can edit multiple attributes
	while True: 
		try:
			print("""
================================================
Toy Attributes:
1. Name
2. Species
3. Height
4. Number of Feet
5. Movie of Character's First Appearance
0. Exit
================================================
		""")
			command = int(input("Which attribute do you want to edit?\nEnter command number: "))
			#CODE BLOCK FOR CHANGING TOY NAME
			if command == 1: 
				new_toys_name = input("\nWhat is your toy's new name? ") 
				#checks if there is already a toy in the list of toys with that name
				if new_toys_name.lower() in get_names(): 
					print("That toy already exists!")
				else:
						#updates the dictionary of index from function get_index() and the key of "Name"
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

							#updates the dictionary of index from function get_index() and the key of "Name"
							toys[get_index(toy_name)]["Name"] = string.capwords(new_toys_name )
							print("Toy's name successfully edited!")
							toy_name = new_toys_name #needed part in order to update the variable toy_name
			
				#CODE BLOCK FOR CHANGING TOY SPECIES
				elif command == 2:
				#updates the dictionary of index from function get_index() and the key of "Species"
						toys[get_index(toy_name)]["Species"] = string.capwords(input("\nWhat is your toy's new species? "))
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
						while True:
							try:
								movie_number = int(input("\nWhat Toy Story movie did the toy first appear? "))
								if movie_number < 5 and movie_number > 0:
									toys[get_index(toy_name)]["FirstAppearance"] = movie_number
									print("First Movie Appearance attribute successfully edited!")
									break
								else: print("Please enter a Toy Story movie")
							except:
								print("Please enter a Toy Story movie")
			
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
        toys = sort.quickSort(toys,0,len(toys)-1)
    print(sort.display(toys))
    return toys

def select_toy(toys):
	#the x is the last element in the list
	x = toys[-1]
	#a loop traversing though the keys and values of the last item in the list
	for i,j in x.items():
		#we return the last element in the list of toys
		print(i, ": ", j)
	#then we pop it
	#toys.pop(len(toys)-1)
	return(toys[-1])


def print_toy (toys):
	#checks if the list is not empty
	if len(toys) == 0:
		print("There are no toys in the list.")
	else:
		#will continue to print the Toy's attributes if the list is not empty
		print("The toys: \n")
		for i in range(len(toys)):
			print("Name: ", toys[i]["Name"])
			print("NumFeet: ", toys[i]["NumFeet"])
			print("Species: ",toys[i]["Species"])
			print("Height: ",toys[i]["Height"])
			print("\n")

def save(toys):
    #make/access the file 'toys.txt' with writable mode
    fileHandler = open ("toys.txt", "w")				
    #writing every elements from the list 'toys' to the file 'toys.txt'
    for i in range (len(toys)):							
        name = toys[i]['Name']							
        species = toys[i]['Species']					
        height = str(toys[i]['Height'])					
        feet = str(toys[i]['NumFeet'])					
        firstappearance = str(toys[i]['FirstAppearance']) 
        fileHandler.write(name + ',' + species + ',' + height + ',' + feet +  ',' + firstappearance + '\n')
    													
    fileHandler.close()
    return toys

def load(toys):
    #access the file 'toys.txt' with read mode
    fileHandler = open ("toys.txt", "r")	
    #clear the existing elements to have the file data only			
    toys.clear()			
    #saving every data seperated by "," into its keys							
    for line in fileHandler:											
        toy_data = line[:-1].split(",")					
        dict_toy = {}									
        dict_toy["Name"] = toy_data[0]					
        dict_toy["Species"] = toy_data[1]
        dict_toy["Height"] = toy_data[2]
        dict_toy["NumFeet"] = toy_data[3]
        dict_toy["FirstAppearance"] = toy_data[4]
        #appending the current line's elements to the main list 'toys'
        toys.append(dict_toy)							
    fileHandler.close()
    return toys
