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

    :param array:
    :param valueDuplicate:
    :return:
    """
    numberDuplicate = 0
    for index in range(len(array)):
        if valueDuplicate == array[index]:
            numberDuplicate += 1
    return numberDuplicate





