'''ou are given a sorted array of integers and a target value.

First, use Linear Search to find the index of the target and count the number of comparisons made.

Then, use Binary Search to find the same target and count the number of comparisons made.

Finally, print which algorithm was more efficient for this particular search.'''


def binarySearch(arr, targetVal):
    left = 0 
    right = len(arr) - 1
    iter = 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == targetVal:
            iter += 1
            return mid, iter
        if arr[mid] < targetVal:
            iter+=1
            left = mid + 1
        else:
            iter+=1
            right = mid - 1

    return -1


def linearSearch(arr, targetVal):
    iter = 0
    print(binarySearch(arr, target))
    for i in range(len(arr)):
        if arr[i] == targetVal:
            iter += 1
            return i, iter
        else:
            iter += 1
            i += 1



arr = list(range(1, 1001))   # [1, 2, 3, ..., 1000]
target = 999


print(binarySearch(arr, target))
# print(binarySearch(arr, target))