'''sort.py'''
import random
from time import perf_counter
from recursioncounter import RecursionCounter

SIZE = 10 # set to 10 for debugging

def selection_sort(lyst):
    '''selection sort'''
    validate_params(lyst)

    for i in range(len(lyst)):
        min_index = i

        for j in range(i+1, len(lyst)):
            if lyst[min_index] > lyst[j]:
                min_index = j

        lyst[i], lyst[min_index] = lyst[min_index], lyst[i]

    return lyst

def insertion_sort(lyst):
    '''insertion sort'''
    validate_params(lyst)

    for i in range(1, len(lyst)):

        item = lyst[i]
        for j in range(0, i):
            if item < lyst[j]:
                lyst.pop(i)
                lyst.insert(j, item)
                break
    return lyst

def mergesort(lyst):
    '''merge sort'''
    validate_params(lyst)
    RecursionCounter()

    if len(lyst) > 1:
        middle = len(lyst) // 2
        side1 = lyst[:middle]
        side2 = lyst[middle:]

        mergesort(side1)
        mergesort(side2)

        i = 0
        j = 0
        k = 0

        while i < len(side1) and j < len(side2):
            if side1[i] < side2[j]:
                lyst[k] = side1[i]
                i += 1
            else:
                lyst[k] = side2[j]
                j += 1
            k += 1

        while i < len(side1):
            lyst[k] = side1[i]
            i += 1
            k += 1

        while j < len(side2):
            lyst[k] = side2[j]
            j += 1
            k += 1

    return lyst

def quicksort(lyst):
    '''quick sort'''
    validate_params(lyst)

    def quicksort_helper(low, high, lyst):
        RecursionCounter()

        if low < high:

            pivot = lyst[high]
            i = low - 1

            for j in range(low, high):

                if lyst[j] < pivot:

                    i = i + 1
                    lyst[i], lyst[j] = lyst[j], lyst[i]

            lyst[i+1], lyst[high] = lyst[high], lyst[i+1]
            quicksort_helper(low, i, lyst)
            quicksort_helper(i+2, high, lyst)
        return lyst

    return quicksort_helper(0, (len(lyst) - 1), lyst)

def is_sorted(lyst):
    '''checks if lyst was successfully sorted'''
    validate_params(lyst)

    for i, item in enumerate(lyst):
        if i < len(lyst) - 1:
            if item > lyst[i + 1]:
                return False

    return True

def create_big_list(list_size):
    '''create list'''

    print(f"Creating a random array of {list_size}")

    random.seed(0)
    lyst = random.sample(range(list_size * 3), k=list_size)

    print(f"Finished creating a random array of {list_size}\n")

    return lyst

def validate_params(lyst):
    '''validate parameters'''

    if not isinstance(lyst, list):
        raise ValueError('lyst is not a list')

    for i in range(0, len(lyst)):
        if not isinstance(lyst[i], int):
            raise ValueError('lyst has a non-integer')

def main():
    '''main'''

    # ---SELECTION---
    lyst = create_big_list(SIZE)
    print("Selection Sort")
    start = perf_counter()
    result = selection_sort(lyst)
    print(result)
    print(is_sorted(result))
    time = perf_counter() - start
    print(f"\tselection_sort() completed in {time:.7f} seconds\n")

    # ---INSERTION---
    lyst = create_big_list(SIZE)
    print("Insertion Sort")
    start = perf_counter()
    result = insertion_sort(lyst)
    print(result)
    print(is_sorted(result))

    time = perf_counter() - start
    print(f"\tinsertion_sort() completed in {time:.7f} seconds\n")

    # ---MERGE---
    lyst = create_big_list(SIZE)
    print("Merge Sort")
    start = perf_counter()
    result = mergesort(lyst)
    print(result)
    print(is_sorted(result))

    time = perf_counter() - start
    print(f"\tmergesort() completed in {time:.7f} seconds\n")

    # ---QUICK---
    lyst = create_big_list(SIZE)
    print("Quick Sort")
    start = perf_counter()
    result = quicksort(lyst)
    print(result)
    print(is_sorted(result))
    time = perf_counter() - start
    print(f"\tquicksort() completed in {time:.7f} seconds\n")


if __name__ == '__main__':
    main()
