def counting_sort(array, key=lambda x:x):
    """
    Returns a sorted list of elements from an array given an array and a key function which turns an element into a key
    to be used for index sorting
    :param array: an array to be sorted
    :param key: a key to turn an element into a key position
    :return: a sorted array
    """
    freq_array = frequency_array(array, key)
    indicies = running_total(freq_array)
    return sort_list(array, indicies, key)

def frequency_array(array, key):
    freq_array = [0] * (max(array, key=key) + 1)
    for item in array:
        freq_array[key(item)] += 1
    return freq_array

def running_total(array):
    running_total_array = [0] * len(array)
    total = 0
    for i, item in enumerate(array):
        running_total_array[i] = total
        total += item
    return running_total_array

def sort_list(array, indicies, key):
    sorted_list = [None] * len(array)
    for item in array:
        index = indicies[key(item)]
        indicies[key(item)] += 1
        sorted_list[index] = item
    return sorted_list


def radix_sort(array):
    """
    Takes an unsorted list of integers and sorts the list using counting sort algorithm and radix sort
    :param array: an unsorted list of integers
    :return: a sorted list of integers
    """
    n = len(str(max(array)))
    for i in range(0, n):
        key = lambda x: int(str(x)[::-1][i]) if i < len(str(x)) else 0
        array = counting_sort(array, key)
    return array