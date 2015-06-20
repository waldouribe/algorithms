def closest_pair(array):
    length = len(array)

    if length < 2:
        return []

    a_sorted = sorted(array)
    min_distance = abs(a_sorted[1] - a_sorted[0])
    current_closet_pair = [a_sorted[0], a_sorted[1]]

    for i in range(1, length-1):
        distance = abs(a_sorted[i+1] - a_sorted[i])
        if distance < min_distance:
            current_closet_pair = [a_sorted[i], a_sorted[i+1]]
            min_distance = distance

    return current_closet_pair
