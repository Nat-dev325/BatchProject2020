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
                    print("\n", (toys))  #FOR TESTING ONLY
                                        #to check if object is successfuly removed from the list
                                        # remove this or add a // # // in front to prevent this code from manifesting
                    return toys
            break 	#prevents the iteration of the codes from "if each_toy" to "for i in range" and the else condition 
					#from manifesting if the Name is not corresponding to the current value of the "for each_toy" conditional
    else: print(toy_name, "is not on the shelf") #Manifests when there is no corresponding object in the list 