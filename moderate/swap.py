def swap(array, i, j):
    # array[i] = a
    # array[j] = b
    array[j] = array[i] + array[j] # array[j] = a + b
    array[i] = array[j] - array[i] # array[i] = a + b - a = b 
    array[j] = array[j] - array[i] # array[j] = a + b - b = a
    return array
