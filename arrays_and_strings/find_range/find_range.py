# array = [3, 3, 4, 4, 4, 11, 11, 11, 11, 17, 20, 20, 20]
# value = 11
# findRange(array, value) --> [5, 8]
# O(log(n)+ log(n)) = O(log(n))
import unittest

def find_range(array, value):
    size = len(array)
    last_index = search_for_last(array, value, 0, size-1)
    if(last_index is None):
        return None
    else:
        first_index = search_for_first(array, value, 0, size-1)
        return [first_index, last_index]

def binary_search(array, value, start, end):
    if(start > end):
        return None
    pivot = (start + end)/2
    if(array[pivot] == value):
        return pivot
    elif(array[pivot] > value):
        return binary_search(array, value, start, pivot-1)
    else:
        return binary_search(array, value, pivot+1, end)

def search_for_first(array, value, start, end, last_found=None):
    if(start > end):
        return last_found
    pivot = (start + end)/2
    if(array[pivot] == value):
        return search_for_first(array, value, start, pivot-1, pivot)
    elif(array[pivot] > value):
        return search_for_first(array, value, start, pivot-1, last_found)
    else:
        return search_for_first(array, value, pivot+1, end, last_found)

def search_for_last(array, value, start, end, last_found=None):
    if(start > end):
        return last_found
    pivot = (start + end)/2
    if(array[pivot] == value):
        return search_for_last(array, value, pivot+1, end, pivot)
    elif(array[pivot] > value):
        return search_for_last(array, value, start, pivot-1, last_found)
    else:
        return search_for_last(array, value, pivot+1, end, last_found)
