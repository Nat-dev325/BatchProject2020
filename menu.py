# This contains all of the functions for main.py
import sort
import string


def menu():
    print(
        """\n===================Main Menu====================
 (1) Search for Toys
 (2) Declutter
 (3) Add Toy
 (4) Edit Toy
 (5) Playtime
 (6) Select Toy
 (7) Print Toys
 (8) Save Current Lineup
 (9) Load Last Lineup
 (0) Bedtime
================================================\n"""
    )
    while True:
        try:
            command = int(input("Enter command number (0-9): "))
            while command > 9 or command < 0:
                command = int(input("Invalid input. \nEnter command number (0,9): "))
            break
        except:
            print("Enter an integer from 0 to 9.")
    return command


# Search for Toy
def searchToy(collection):
    def search(attribute, toSearch):
        search_count = 0
        # check each element in collection
        for i in range(len(collection)):
            # print the information if the toSearch is found in collection[i][attribute]
            if toSearch == collection[i][attribute]:
                print()
                print("Name:", collection[i]["Name"])
                print("Species:", collection[i]["Species"])
                print("Height:", collection[i]["Height"])
                print("Number of Feet:", collection[i]["No. Feet"])
                print(
                    "First Appearance in Toy Story:", collection[i]["FirstAppearance"]
                )
                search_count += 1
        # if nothing is printed, print toSearch does not exist
        if search_count == 0:
            print("%s does not exist." % toSearch)

    # a sub-menu showing the main criteria of the attributes from which a user can choose from

    print(
        """\n=========Searching Toy in Collection============
 Which attribute do you want to search from?
 (1) Name
 (2) Species
 (3) Height
 (4) Number of Feet
 (5) First Appearance
================================================\n"""
    )
    # asking for the user choice and force to enter a valid input
    while True:
        try:
            user_choice = int(input("Enter your choice (1-5): "))
            while user_choice > 5 or user_choice < 1:
                user_choice = int(input("Invalid input. \nEnter your choice (1-5): "))
            break
        except:
            print("Enter an integer from 0 t 9.")

    # Search using attribute name
    # string.capwords(<string>) was used to capitalize only the first letter of each word

    if user_choice == 1:
        attribute = "Name"
        toSearch = string.capwords(input("\nWhat is the toy's name? "))
        search(attribute, toSearch)

    # Search using attribute species
    elif user_choice == 2:
        attribute = "Species"
        toSearch = string.capwords(input("\nWhat is the toy's species? "))
        search(attribute, toSearch)

    # Search using attribute height
    elif user_choice == 3:
        attribute = "Height"
        # Force input a float
        while True:
            try:
                toSearch = float(input("\nWhat is the toy's height? "))
                break
            except:
                print("Invalid input. Enter a number.")
        search(attribute, toSearch)

    # Search using attribute feet
    elif user_choice == 4:
        attribute = "No. Feet"
        # Force input an integer
        while True:
            try:
                toSearch = int(input("\nWhat is the toy's number of feet? "))
                break
            except:
                print("Invalid input. Enter an integer.")
        search(attribute, toSearch)

    # Search using attribute FirstAppearance
    elif user_choice == 5:
        attribute = "FirstAppearance"
        # Force input an integer
        while True:
            try:
                toSearch = int(input("\nWhat is the toy's first movie appearance? "))
                break
            except:
                print("Invalid input. Enter an integer.")
        search(attribute, toSearch)


def declutter(toys):  # function that removes a toy from the list
    print("\n===========Decluttering the Collection==========\n")
    x = input("What toy do you want to remove? ")
    toy_name = string.capwords(x)
    # Finds the dictionary within the list that corresponds to the given input
    for i in range(len(toys)):
        # determines whether the name attribute in dict "i" matches the given input
        if toys[i]["Name"] == toy_name:
            print("\n" + toy_name, "has been removed from the shelf\n")
            for attribute in toys[i]:
                # prints the attributes of the deleted object
                print(attribute + ": " + str(toys[i][attribute]) + ",", end=" ")
            # deletes the dict of the given input
            del toys[i]
            print()
            return toys
    else:
        # Manifests when there is no corresponding object in the list
        print("\n" + toy_name, "is not on the shelf")
        return toys


def addToys(collection):
    print("\n===========Adding Toy in Collection==========\n")
    # initialization of dictionary
    dictToy = {
        "Name": "",
        "Species": "",
        "Height": 0,
        "No. Feet": 0,
        "FirstAppearance": 0,
    }

    # input name
    name = string.capwords(input("Enter Toy's Name: "))
    # Check if the name in the collection is already entered.
    for i in range(len(collection)):
        if name == collection[i]["Name"]:
            print("Unable to add.", name, "is already in the collection.")
            return collection
    # force the user to input a valid value type (int) and valid number of feet (cannot be less than 1)
    while True:
        try:
            numFeet = int(input("Enter Toy's Number of Feet: "))
            while numFeet < 1:
                numFeet = int(input("Invalid Input. \nEnter Toy's Number of Feet: "))
            break
        except ValueError:
            print("Enter an integer.")

    # input species
    species = string.capwords(input("Enter Toy's Species: "))

    # force the user to input a valid value type (float) and valid height (cannot be less than or equal to 0)
    while True:
        try:
            height = float(input("Enter Toy's Height: "))
            while height <= 0:
                height = float(input("Invalid Input. \nEnter Toy's Height: "))
            break
        except ValueError:
            print("Enter a number.")

    # force the user to input a valid value type (int) and valid first appearance (can only enter either 1, 2, 3, or 4)
    while True:
        try:
            firstAppearance = int(input("Enter Toy's First Appearance: "))
            while firstAppearance < 1 or firstAppearance > 4:
                firstAppearance = int(
                    input("Invalid Input. \nEnter Toy's First Appearance: ")
                )
            break
        except ValueError:
            print("Enter an integer.")

    # update the values in the dictionary
    dictToy["Name"] = string.capwords(name)
    dictToy["Species"] = string.capwords(species)
    dictToy["Height"] = height
    dictToy["No. Feet"] = numFeet
    dictToy["FirstAppearance"] = firstAppearance

    # add dictToy to the original list of dictionaries
    collection.append(dictToy)

    # notify the user that they have successfully added a toy
    print("\n" + name + " added in Collection!")

    # print the attributes of the toy
    print(dictToy)

    return dictToy


def edit_toy(toys):  # toys_list should be the list containing the dictionaries
    print("\n==========Editing Toy in Collection============")

    # function within a function in order to access the names in the list of toys
    def get_names():
        toys_names = []  # places names in a list and returns a list
        for index in range(len(toys)):
            toys_names.append(toys[index]["Name"])
        return toys_names

    # function in order to get the index of toy with the variable "name"
    def get_index(name):
        index = 0
        for toy_dict in toys:
            if name == toy_dict["Name"]:
                return index
            else:
                index += 1

    # checks if there are toys in the first place. if none, ends the function
    if len(toys) == 0:
        return print("There are no toys to edit :(")

    toy_name = ""

    # loop to check if the toy name exists

    while toy_name not in get_names():
        toy_name = string.capwords(input("\nEnter toy's name: "))

        if toy_name not in get_names():
            print("Oh no! Toy not found :(\nHere are your toys:")
            for x in get_names():
                print("\t" + x)

    print("Toy found!")

    # try except while true loop so that one can edit multiple attributes
    while True:
        try:
            print(
                """\n================================================
Toy Attributes:
(1) Name
(2) Species
(3) Height
(4) Number of Feet
(5) Movie of Character's First Appearance
(0) Exit
================================================"""
            )
            command = int(
                input("\nWhich attribute do you want to edit?\nEnter command number: ")
            )

            # CODE BLOCK FOR CHANGING TOY NAME
            if command == 1:
                new_toys_name = string.capwords(
                    input("\nWhat is your toy's new name? ")
                )

                # checks if there is already a toy in the list of toys with that name
                if new_toys_name in get_names():
                    print("That toy already exists!")
                else:

                    # updates the dictionary of index from function get_index() and the key of "Name"
                    toys[get_index(toy_name)]["Name"] = new_toys_name
                    print("Toy's name successfully edited!")
                    toy_name = new_toys_name  # needed part in order to update the variable toy_name

            # CODE BLOCK FOR CHANGING TOY SPECIES
            elif command == 2:
                # updates the dictionary of index from function get_index() and the key of "Species"
                toys[get_index(toy_name)]["Species"] = string.capwords(
                    input("\nWhat is your toy's new species? ")
                )
                print("Species attribute successfully edited!")

            # CODE BLOCK FOR CHANGING TOY HEIGHT
            elif command == 3:
                # updates the dictionary of index from function get_index() and the key of "Height"
                toys[get_index(toy_name)]["Height"] = float(
                    input("\nWhat is your toy's new height? ")
                )
                print("Height attribute successfully edited!")

            # CODE BLOCK FOR CHANGING TOY FEET
            elif command == 4:
<<<<<<< HEAD
                toys[get_index(toy_name)]["NumFeet"] = int(
                    input("\nWhat is your toy's new number of feet? ")
                )
=======
                toys[get_index(toy_name)]["No. Feet"] = int(input("\nWhat is your toy's new number of feet? "))
>>>>>>> b9cee616148c261c57f7ba4acc7d229fabd6e703
                print("Number of feet attribute successfully edited!")

            # CODE BLOCK FOR CHANGING MOVIE APPEARANCE
            elif command == 5:
                # updates the dictionary of index from function get_index() and the key of "FirstAppearance"
                while True:
                    try:
                        movie_number = int(
                            input("\nWhat Toy Story movie did the toy first appear? ")
                        )
                        if movie_number < 5 and movie_number > 0:
                            toys[get_index(toy_name)]["FirstAppearance"] = movie_number
                            print(
                                "First Movie Appearance attribute successfully edited!"
                            )
                            break
                        else:
                            print("Please enter a Toy Story movie")
                    except:
                        print("Please enter a Toy Story movie")

            # CODE BLOCK TO EXIT EDITING
            elif command == 0:
                print(
                    "\nChanges have been saved!\nCurrent toy details are as follows:\n"
                )

                # For loop to go through all attributes of said toy for printing
                for attribute in toys[get_index(toy_name)]:
                    if attribute == "FirstAppearance":
<<<<<<< HEAD
                        print(
                            "(First Seen in Toy Story)",
                            toys[get_index(toy_name)][attribute],
                            end="",
                        )
                    else:
                        print(
                            attribute + ":",
                            toys[get_index(toy_name)][attribute],
                            end="\n",
                        )
=======
                        print("(First Seen in Toy Story", toys[get_index(toy_name)][attribute], end=")")
                    else: 
                        print(attribute+":", toys[get_index(toy_name)][attribute], end="\n")
>>>>>>> b9cee616148c261c57f7ba4acc7d229fabd6e703
                print("\n\n")
                return toys[get_index(toy_name)]

        except:
            print(
                "There seems to be an error in the input"
            )  # if there is an error, print this. Example: if a string was given for height


def playtime(toys):
    print(
        """\n==================Playtime======================
 (1) Name                     (Bubble Sort)
 (2) Height                   (Merge Sort)
 (3) Species                  (Insertion Sort)
 (4) First Movie Appearance   (Selection Sort)
 (5) Number of Feet           (Quick Sort)
================================================\n"""
    )
    # This loop forces the user to enter a valid input
    while True:
        try:
            command = int(input("Enter command number(1-5): "))
            while command > 5 or command < 1:
                command = int(input("Invalid input. \nEnter command number(1-5): "))
            break
        except:
            print("Enter an integer from 1 to 5.")

    if command == 1:
        toys = sort.BubbleSort(toys)
    elif command == 2:
        toys = sort.mergeSort(toys)
    elif command == 3:
        toys = sort.InsertionSort(toys)
    elif command == 4:
        toys = sort.SelectionSort(toys)
    elif command == 5:
        toys = sort.quickSort(toys, 0, len(toys) - 1)
    print(sort.display(toys))
    return toys


def select_toy(toys):
    print("\n============Dequeuing Collection================\n")
    # the x is the last element in the list
    x = toys[0]
    # a loop traversing though the keys and values of the last item in the list
    for i, j in x.items():
        # we return the last element in the list of toys
        print(i, "\b: ", j)
    return toys[0]


def print_toy(toys):
    print("\n==============Printing Collection===============\n")
    # checks if the list is not empty
    if len(toys) == 0:
        print("There are no toys in the list.")
    # will continue to print the Toy's attributes if the list is not empty
    else:
        print("The toys: \n")
        for i in range(len(toys)):
            print("Name:", toys[i]["Name"])
<<<<<<< HEAD
            print("Number of Feet:", toys[i]["NumFeet"])
            print("Species:", toys[i]["Species"])
            print("Height:", toys[i]["Height"])
=======
            print("Number of Feet:", toys[i]["No. Feet"])
            print("Species:",toys[i]["Species"])
            print("Height:",toys[i]["Height"])
>>>>>>> b9cee616148c261c57f7ba4acc7d229fabd6e703
            print("First Appearance:", toys[i]["FirstAppearance"])
            print()


def save(toys):
<<<<<<< HEAD
    # make/access the file 'toys.txt' with writable mode
    fileHandler = open("toys.txt", "w")
    # writing every elements from the list 'toys' to the file 'toys.txt'
    for i in range(len(toys)):
        name = toys[i]["Name"]
        species = toys[i]["Species"]
        height = str(toys[i]["Height"])
        feet = str(toys[i]["NumFeet"])
        firstappearance = str(toys[i]["FirstAppearance"])
        fileHandler.write(
            name
            + ","
            + species
            + ","
            + height
            + ","
            + feet
            + ","
            + firstappearance
            + "\n"
        )

=======
    #make/access the file 'toys.txt' with writable mode
    fileHandler = open ("toys.txt", "w")				
    #writing every elements from the list 'toys' to the file 'toys.txt'
    for i in range (len(toys)):							
        name = toys[i]['Name']							
        species = toys[i]['Species']					
        height = str(toys[i]['Height'])					
        feet = str(toys[i]['No. Feet'])					
        firstappearance = str(toys[i]['FirstAppearance']) 
        fileHandler.write(name + ',' + species + ',' + height + ',' + feet +  ',' + firstappearance + '\n')
    													
>>>>>>> b9cee616148c261c57f7ba4acc7d229fabd6e703
    fileHandler.close()
    return toys


def load(toys):
    # access the file 'toys.txt' with read mode
    fileHandler = open("toys.txt", "r")
    # clear the existing elements to have the file data only
    toys.clear()
    # saving every data seperated by "," into its keys
    for line in fileHandler:
        toy_data = line[:-1].split(",")
        dict_toy = {}
        dict_toy["Name"] = toy_data[0]
        dict_toy["Species"] = toy_data[1]
        dict_toy["Height"] = float(toy_data[2])
        dict_toy["No. Feet"] = int(toy_data[3])
        dict_toy["FirstAppearance"] = int(toy_data[4])
        # appending the current line's elements to the main list 'toys'
        toys.append(dict_toy)
    fileHandler.close()

    return toys
