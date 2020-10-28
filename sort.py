# Library for sorting functions

# Bubble Sort
def BubbleSort(toys):
    #Number of iterations; Ex. 5 elements = 5 iterations
    for i in range(0,len(toys)):
        #Indices; len(toys)-1 because there is no index that is the length of a list
        for j in range(0,len(toys)-1):
            if toys[j]["Name"] > toys[j+1]["Name"]:
                toys[j], toys[j+1] = toys[j+1], toys[j]

    return toys

# Insertion Sort
def InsertionSort(toys):

	# Iterate over the whole list
	for i in range(1, len(toys)):
		# Assign the unsorted item to a variable
		key = toys[i]

		# Index of the values for the key to compare to
		j = i-1

		# Loop while the key is unsorted in the sorted list
		while j >= 0 and (key['Species'] < toys[j]['Species']):
			toys[i] = toys[j]
			j = j - 1
			i = i - 1
			
			
		# Place the key back to the list once it is sorted
		toys[j + 1] = key

	return toys

# Function for displaying sorted items
def display(toys):
    display = ""
    for i in range(0,len(toys)):
        for j in toys[i]:
            #'{0: <number}' is for format purposes
            if j == "Name":
                display += str(j) + ": " + '{0: <15}'.format(str(toys[i][j]))
                continue
            if j == "Feet":
                display += str(j) + ": " + '{0: <6}'.format(str(toys[i][j]))
                continue
            display += str(j) + ": " + '{0: <10}'.format(str(toys[i][j]))
        display += "\n"
    return display

