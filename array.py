def displayArray(array) -> None:
    """
    Print each element of an array
    :param array: array to display
    :return: None
    """
    for element in array:
        print(element)

def minimumWithIndexOfArray(array):
    """
    Returns the minimum value of an array and its index
    :param array: array of integer or float
    :return: two integer or float, minimum value index and minimum value
    """
    minimumValue = array[0]
    minimumValueIndex = 0
    for index in range(1, len(array)):
        if array[index] < minimumValue:
            minimumValue = array[index]
            minimumValueIndex = index
    return minimumValueIndex, minimumValue

def minimumOfArray(array):
    """
    Returns the minimum value of an array
    :param array: array of integer or float
    :return: integer or float : minimum value of an array
    """
    minimumValue = array[0]
    for index in range(1, len(array)):
        if array[index] < minimumValue:
            minimumValue = array[index]
    return minimumValue

def maximumWithIndexOfArray(array):
    """
    Returns the maximum value of an array and its index
    :param array: array of integer or float
    :return: two integer or float, maximum value index and maximum value
    """
    maximumValue = array[0]
    maximumValueIndex = 0
    for index in range(1, len(array)):
        if array[index] > maximumValue:
            maximumValue = array[index]
            maximumValueIndex = index
    return maximumValueIndex, maximumValue

def maximumOfArray(array):
    """
    Returns the maximum value of an array
    :param array: array of integer or float
    :return: integer or float : maximum value of an array
    """
    maximumValue = array[0]
    for index in range(1, len(array)):
        if array[index] > maximumValue:
            maximumValue = array[index]
    return maximumValue

def duplicateArray(array, valueDuplicate):
    """
    Count the number of occurrences
    :param array:
    :param valueDuplicate:
    :return:
    """
    numberDuplicate = 0
    for index in range(len(array)):
        if valueDuplicate == array[index]:
            numberDuplicate += 1
    return numberDuplicate

def createEntryArrayInt(numberElement):
    """
    Create an array of number Element integers
    :param numberElement: int : number of elements in the array
    :return: array
    """
    array = []
    while len(array) != numberElement:
        try:
            array.append(int(input("Enter an Integer :")))
        except ValueError:
            print("It's not an Integer!")
    return array

def FindValueArray(array, valueToFind):
    """
    Finds if the value is in the array and returns the first index
    :param array: the array where the search will be carried out
    :param valueToFind: value to find in the array
    :return: returns the index of where the value is located
    """
    i = 0
    while (i < len(array)) and (array[i] != valueToFind):
        i += 1
    if i < len(array):
        return i
    else:
        print("Value not find")

