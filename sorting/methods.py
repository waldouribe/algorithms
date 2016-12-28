def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        j = i
        while j > 0 and a[j-1] > a[j]:
            swap(a, j-1, j)
            j = j-1
    return a

def selection_sort(a):
    n = len(a)
    for i in range(0, n):
        min_index = i
        for j in range(i+1, n):
            if a[j] < a[min_index]:
                min_index = j
        swap(a, i, min_index)
    return a

def quicksort(a)
    return a

def swap(a, i, j):
    aux = a[i]
    a[i] = a[j]
    a[j] = aux