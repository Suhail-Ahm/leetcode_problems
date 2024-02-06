# description

# A subarray is a contiguous part of array, i.e., Subarray is an array that is inside another array.

# In general, for an array of size n, there are n*(n+1)/2 non-empty subarrays.


# iterative method
# time complexity Big O(n*n)
def subarray(arr):
    sublists = []
    for start in range(len(arr)):
        for end in range(start + 1, len(arr) + 1):
            sublists.append(arr[start:end])
    return sublists


# recursion method
# time complexity Big O(n)
def recursion_subarray(arr, start, end, sublists):
    if end == len(arr):
        return sublists
    elif start > end:
        return recursion_subarray(arr, 0, end + 1, sublists)
    else:
        sublists.append(arr[start : end + 1])
        return recursion_subarray(arr, start + 1, end, sublists)


arr = [1, 2, 3, 4]
print(recursion_subarray(arr, 0, 0, []))
