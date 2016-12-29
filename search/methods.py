def binary_search(needle, haystack):
    return rec_binary_search(needle, haystack, 0, len(haystack)-1)

def rec_binary_search(needle, haystack, left, right):
    if left > right:
        return -1
    else:
        center = (left+right)/2

        if haystack[center] == needle:
            return center
        elif haystack[center] < needle:
            return rec_binary_search(needle, haystack, center+1, right)
        else:
            return rec_binary_search(needle, haystack, left, center-1)
