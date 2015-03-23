def largest_sum(array):
    max_sum = array[0]
    sumatory = max_sum
    for i in range(1, len(array)):
        sumatory += array[i]
        if sumatory >= max_sum:
            max_sum = sumatory
        if array[i] >= max_sum:
            sumatory = array[i]
            max_sum = sumatory

    return max_sum
