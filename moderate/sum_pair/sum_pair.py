import math

def sum_pair(array, wanted_sum):
    sorted_array = sorted(array)
    size = len(array)
    pairs = []
    start = 0
    end = size - 1
    while start < end:
        start_value = sorted_array[start]
        end_value = sorted_array[end]
        pair_sum =  start_value + end_value
        if pair_sum == wanted_sum:
            pairs.append([start_value, end_value])
            start += 1
            end -= 1
        elif pair_sum > wanted_sum:
            end -= 1
        else:
            start += 1
    return pairs
 