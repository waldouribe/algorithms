def invert(array):
  inverted_array = []
  for i in range(len(array)-1, -1 ,-1):
    inverted_array.append(array[i])
  return inverted_array
