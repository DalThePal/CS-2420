'''search.py'''

import random
from time import perf_counter
from math import sqrt
from recursioncounter import RecursionCounter

SIZE = 10000000 # set to 10 for debugging

def linear_search(lyst, target):
    '''preforms a linear search finding the target item in the list'''

    validate_params(lyst, target)
    found = False

    for item in lyst:
        if item == target:
            found = True
            break

    return found

def recursive_binary_search(lyst, target):
    '''preforms a binary search finding the target item in the list'''

    validate_params(lyst, target)
    low = 0
    high = len(lyst) - 1

    def recursive_binary_search_helper(low_index, high_index, lyst, target):
        '''the recursive helper function'''

        RecursionCounter()
        mid = (low_index + high_index) // 2
        new_low = low_index
        new_high = high_index

        if high_index >= low_index:
            if lyst[mid] == target:
                return True

            if target < lyst[mid]:
                new_high = mid - 1

            else:
                new_low = mid + 1

            return recursive_binary_search_helper(new_low, new_high, lyst, target)
        return False
    found = recursive_binary_search_helper(low, high, lyst, target)

    return found

def jump_search(lyst, target):
    '''preforms a jump search finding the target item in the list'''

    validate_params(lyst, target)
    step = int(sqrt(len(lyst)))
    prev_index = 0
    next_index = step + prev_index

    while next_index < len(lyst) and lyst[next_index] < target:
        prev_index = next_index
        next_index += step
    return linear_search(lyst[prev_index : min(next_index, len(lyst))], target)


def create_big_list(list_size):
    '''creates a random sorted list based on the size passed in'''

    print(f"Creating a sorted array of {list_size}")

    random.seed(0)
    lyst = random.sample(range(list_size * 3), k=list_size)
    lyst.sort()

    print(f"Finished creating a sorted array of {list_size}\n")

    return lyst

def validate_params(lyst, target):
    '''throes an error if lyst is not an array of ints or if target is not an int'''

    if not isinstance(target, int):
        raise ValueError('target is not an integer')

    for i in range(0, len(lyst) - 1):
        if not isinstance(lyst[i], int):
            raise ValueError('lyst has a non-integer')

def main():
    '''runs all of the search algorithms'''


    lyst = create_big_list(SIZE)

  # ---LINEAR---
    print("Starting Linear\n")

  # start
    print("Searching for a number at the start of the array")
    start = perf_counter()
    result = linear_search(lyst, lyst[0])
    time = perf_counter() - start
    print(f"\tlinear_search() returned {result} in {time:.7f} seconds\n")

  # mid
    print("Searching for a number in the middle of the array")
    start = perf_counter()
    result = linear_search(lyst, lyst[len(lyst) // 2])
    time = perf_counter() - start
    print(f"\tlinear_search() returned {result} in {time:.7f} seconds\n")

  # end
    print("Searching for a number at the end of the array")
    start = perf_counter()
    result = linear_search(lyst, lyst[-1])
    time = perf_counter() - start
    print(f"\tlinear_search() returned {result} in {time:.7f} seconds \n")

  # NA
    print("Searching for a number not in the array")
    start = perf_counter()
    result = linear_search(lyst, -1)
    time = perf_counter() - start
    print(f"\tlinear_search() returned {result} in {time:.7f} seconds \n")

  # ---BINARY---
    print("Starting Binary\n")

  # start
    print("Searching for a number at the start of the array")
    start = perf_counter()
    result = recursive_binary_search(lyst, lyst[0])
    time = perf_counter() - start
    print(f"\trecursive_binary_search() returned {result} in {time:.7f} seconds\n")

  # mid
    print("Searching for a number in the middle of the array")
    start = perf_counter()
    result = recursive_binary_search(lyst, lyst[len(lyst) // 2])
    time = perf_counter() - start
    print(f"\trecursive_binary_search() returned {result} in {time:.7f} seconds\n")

  # end
    print("Searching for a number at the end of the array")
    start = perf_counter()
    result = recursive_binary_search(lyst, lyst[-1])
    time = perf_counter() - start
    print(f"\trecursive_binary_search() returned {result} in {time:.7f} seconds \n")

  # NA
    print("Searching for a number not in the array")
    start = perf_counter()
    result = recursive_binary_search(lyst, -1)
    time = perf_counter() - start
    print(f"\trecursive_binary_search() returned {result} in {time:.7f} seconds \n")

  # ---JUMP---
    print("Starting Jump\n")

  # start
    print("Searching for a number at the start of the array")
    start = perf_counter()
    result = jump_search(lyst, lyst[0])
    time = perf_counter() - start
    print(f"\tjump_search() returned {result} in {time:.7f} seconds\n")

  # mid
    print("Searching for a number in the middle of the array")
    start = perf_counter()
    result = jump_search(lyst, lyst[len(lyst) // 2])
    time = perf_counter() - start
    print(f"\tjump_search() returned {result} in {time:.7f} seconds\n")

  # end
    print("Searching for a number at the end of the array")
    start = perf_counter()
    result = jump_search(lyst, lyst[-1])
    time = perf_counter() - start
    print(f"\tjump_search() returned {result} in {time:.7f} seconds \n")

  # NA
    print("Searching for a number not in the array")
    start = perf_counter()
    result = jump_search(lyst, -1)
    time = perf_counter() - start
    print(f"\tjump_search() returned {result} in {time:.7f} seconds \n")


if __name__ == '__main__':
    main()
