# Library for sorting functions

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