from typing import List

# Constraints:
# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 10^9
# 0 <= k <= arr.length


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if k == 0:
            return len(set(arr))

        frequency = {}
        for num in arr:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        def custom_sort(x):
            return (frequency[x], x)

        arr.sort(key=custom_sort)

        arr = arr[k:]
        # unique_integer = []
        # for i in arr:
        #     if i not in unique_integer:
        #         unique_integer.append(i)

        return len(set(arr))


arr = [245600, 50000, 245600]
k = 1
solution = Solution()
print(solution.findLeastNumOfUniqueInts(arr, k))
