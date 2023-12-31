# NOTE: Change this file however you want.  I won't be grading it at
# all.  It's only used to generate the data for filling in the table.
import random
import time

from sorts import selection_sort, insertion_sort, merge_sort


def time_sort(sort_function, size: int) -> tuple[float, int]:
    """Times the sort function on a random list of the given size.

    Returns the time and the number of camparisons as a tuple.
    """
    # Give the random number generator a seed, so the same sequence of
    # random numbers is generated each time.  This makes for a fair
    # comparison between sort functions, they'll be sorting the same
    # lists.  You're welcome to change the seed, but for a fair
    # comparison you'll want the same seed for each sort algorithm.
    random.seed(1234)
    my_list = random.choices(range(1000000), k=size)

    start_time = time.time()
    comparisons = sort_function(my_list)
    end_time = time.time()

    return end_time - start_time, comparisons


def main():
    # Runs merge_sort on a list of size 5000.  I would suggest making
    # some loops here.
    size = 1000
    duration, comparison = time_sort(selection_sort, size)
    print('Selection sort (%d elements): %.3f s, %d comparisons' %
        (size, duration, comparison))

    while size < 32000:
        duration_1, comparisons_1 = time_sort(selection_sort, size)
        size = size * 2
        print('Selection sort (%d elements): %.3f s, %d comparisons' %
        (size, duration_1, comparisons_1))

    """size = 100000
    duration, comparison = time_sort(selection_sort, size)
    print('Selection sort (%d elements): %.3f s, %d comparisons' %
        (size, duration, comparison))

    size = 500000
    duration, comparison = time_sort(selection_sort, size)
    print('Selection sort (%d elements): %.3f s, %d comparisons' %
        (size, duration, comparison))

    size = 1000000
    duration, comparison = time_sort(selection_sort, size)
    print('Selection sort (%d elements): %.3f s, %d comparisons' %
        (size, duration, comparison))

    size = 10000000
    duration, comparison = time_sort(selection_sort, size)
    print('Selection sort (%d elements): %.3f s, %d comparisons' %
        (size, duration, comparison))"""
    
    size = 1000
    duration, comparison = time_sort(insertion_sort, size)
    print('Insertion sort (%d elements): %.3f s, %d comparisons' %
        (size, duration, comparison))

    while size < 32000:
        duration_1, comparisons_1 = time_sort(insertion_sort, size)
        size = size * 2
        print('Insertion sort (%d elements): %.3f s, %d comparisons' %
        (size, duration_1, comparisons_1))

    """size = 100000
    duration, comparison = time_sort(insertion_sort, size)
    print('Insertion sort (%d elements): %.3f s, %d comparisons' %
        (size, duration, comparison))

    size = 500000
    duration, comparison = time_sort(insertion_sort, size)
    print('Insertion sort (%d elements): %.3f s, %d comparisons' %
        (size, duration, comparison))

    size = 1000000
    duration, comparison = time_sort(insertion_sort, size)
    print('Insertion sort (%d elements): %.3f s, %d comparisons' %
        (size, duration, comparison))

    size = 10000000
    duration, comparison = time_sort(insertion_sort, size)
    print('Insertion sort (%d elements): %.3f s, %d comparisons' %
        (size, duration, comparison)"""

    size = 1000
    duration, comparison = time_sort(merge_sort, size)
    print('Merge sort (%d elements): %.3f s, %d comparisons' %
        (size, duration, comparison))

    while size < 32000:
        duration_1, comparisons_1 = time_sort(merge_sort, size)
        size = size * 2
        print('Merge sort (%d elements): %.3f s, %d comparisons' %
        (size, duration_1, comparisons_1))

    """size = 100000
    duration, comparison = time_sort(merge_sort, size)
    print('Merge sort (%d elements): %.3f s, %d comparisons' %
        (size, duration, comparison))

    size = 500000
    duration, comparison = time_sort(merge_sort, size)
    print('Merge sort (%d elements): %.3f s, %d comparisons' %
        (size, duration, comparison))

    size = 1000000
    duration, comparison = time_sort(merge_sort, size)
    print('Merge sort (%d elements): %.3f s, %d comparisons' %
        (size, duration, comparison))

    size = 10000000
    duration, comparison = time_sort(merge_sort, size)
    print('Merge sort (%d elements): %.3f s, %d comparisons' %
        (size, duration, comparison))"""

if __name__ == '__main__':
    main()
