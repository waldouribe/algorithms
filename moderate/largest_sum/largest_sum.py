def largest_sum(array):
    current_sum = current_largest_sum = array[0]

    for i in range(1, len(array)):
        current_sum = max(array[i], array[i] + current_sum)
        current_largest_sum = max(current_largest_sum, current_sum)

    return current_largest_sum
