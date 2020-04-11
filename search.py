#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found



def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests
    if index >= len(array):
        return None
    elif item == array[index]:
        return index
    return linear_search_recursive(array, item, index + 1)





def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item, 0, len(array) - 1)
    #picked the middle of array, compared the target to the middle element if it was greater
    #or smaller, and then discarded on half. Either we find it as middle element
    #or we don't find it

def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    pass
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    #[5, 6, 7, 10, 12]
    left_index = 0
    right_index = len(array) - 1

    while left_index <= right_index: 

        mid_index = (right_index + left_index) // 2
        print("Middle index", mid_index)
        print("Left index", left_index)
        print("Right index", right_index)
        

        if array[mid_index] == item:
            print("Found it!")
            return mid_index

        elif item < array[mid_index]:
            print("Entered ignore right")
            right_index = mid_index - 1

        elif item > array[mid_index]:
            left_index = mid_index + 1

#if item < item at middle, we ignore the right part of the array
# if the item > item at the middle we ignore the left part of the array

def binary_search_recursive(array, item, left=None, right=None):
    #Is the middle item what we are looking for?
    if left <= right:
        mid = (right + left) // 2
        if array[mid] < item:
            return binary_search_recursive(array, item, mid + 1, right)
        elif array[mid] > item:
            return binary_search_recursive(array, item, left, mid - 1)
        else:
            return mid

    

