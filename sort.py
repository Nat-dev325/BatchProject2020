# Library for sorting functions

# Bubble Sort
def BubbleSort(toys):
    # Number of iterations; Ex. 5 elements = 5 iterations
    for i in range(0, len(toys)):
        # Indices; len(toys)-1 because there is no index that is the length of a list
        for j in range(0, len(toys) - 1):
            if toys[j]["Name"] > toys[j + 1]["Name"]:
                toys[j], toys[j + 1] = toys[j + 1], toys[j]

    return toys


# Insertion Sort
def InsertionSort(toys):

    # Iterate over the whole list
    for i in range(1, len(toys)):
        # Assign the unsorted item to a variable
        key = toys[i]

        # Index of the values for the key to compare to
        j = i - 1

        # Loop while the key is unsorted in the sorted list
        while j >= 0 and (key["Species"] < toys[j]["Species"]):
            toys[i] = toys[j]
            j = j - 1
            i = i - 1

        # Place the key back to the list once it is sorted
        toys[j + 1] = key

    return toys


# Function for displaying sorted items
def display(toys):
    display = ""
    for i in range(0, len(toys)):
        for j in toys[i]:
            #'{0: <number}' is for format purposes
            if j == "Name":
                display += str(j) + ": " + "{0: <20}".format(str(toys[i][j]))
                continue
            if j == "Feet":
                display += str(j) + ": " + "{0: <6}".format(str(toys[i][j]))
                continue
            display += str(j) + ": " + "{0: <10}".format(str(toys[i][j]))
        display += "\n"
    return display


# Function for Quick Sort
def partition(list, low, high):
    i = low - 1
    temp = list[high]
    pivot = temp["NumFeet"]
    for j in range(low, high):
        temp = list[j]
        if temp["NumFeet"] < pivot:  # determines which number of feet is smaller
            i = i + 1
            list[i], list[j] = list[j], list[i]  # swap
    list[i + 1], list[high] = list[high], list[i + 1]
    return i + 1


# Quick Sort
def quickSort(list, low, high):
    if len(list) == 1:  # returns list if it has only 1 toy
        return list
    elif high > low:
        parted = partition(list, low, high)

        quickSort(list, parted + 1, high)  # sorts by numfeet before parting the list
        quickSort(list, low, parted - 1)  # sorts by numfeet after parting the list

    return list


# Merge sort
def mergeSort(toys):
    if len(toys) > 1:
        # find the mid point of the list then divide in 2 halves
        mid = len(toys) // 2
        left = toys[:mid]
        right = toys[mid:]

        # recursively mergeSort the left and the right
        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            # compare the Height value of the left and the right. which ever value is higher will be placed in toys[k]
            if left[i]["Height"] <= right[j]["Height"]:
                toys[k] = left[i]
                i += 1
            else:
                toys[k] = right[j]
                j += 1
            k += 1
        # copy the remaining elements of the left to toys if there are any
        while i < len(left):
            toys[k] = left[i]
            i += 1
            k += 1
        # copy the remaining elements of the left to toys if there are any
        while j < len(right):
            toys[k] = right[j]
            j += 1
            k += 1
    return toys


# Selection Sort
def SelectionSort(toys):
    # iteration of the list
    for i in range(0, len(toys) - 1):
        # setting the first element in the unsorted list as the default min value
        min_value = i

        for j in range(i + 1, len(toys)):
            if toys[j]["FirstAppearance"] < toys[min_value]["FirstAppearance"]:
                # new min value
                min_value = j

        # new min value is no longer equal to default min value
        if min_value != i:
            # switching the values
            toys[min_value], toys[i] = toys[i], toys[min_value]

    return toys