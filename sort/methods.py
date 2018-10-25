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

def quicksort(a):
    rec_quicksort(a, 0, len(a)-1)

def rec_quicksort(a, i, j):
    if i < j:
        pivot = partition(a, i, j)
        rec_quicksort(a, i, pivot-1)
        rec_quicksort(a, pivot+1, j)

def partition(a, i, j):
    pivot = a[j]
    left = i

    for k in range(i, j):
        if a[k] <= pivot:
            swap(a, k, left)
            left += 1
    swap(a, j, left)
    return left

def swap(a, i, j):
    aux = a[i]
    a[i] = a[j]
    a[j] = aux
