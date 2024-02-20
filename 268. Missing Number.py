from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i

    def missingNumberUsingXOR(self, nums: List[int]) -> int:
        ans = len(nums)

        for idx, num in enumerate(nums):
            ans ^= idx ^ num
        return ans

    def missingNumberUsingAP(self, nums: List[int]) -> int:
        expected_total_sum = (len(nums) * (len(nums) + 1)) // 2
        actual_total_sum = sum(nums)
        return expected_total_sum - actual_total_sum


nums = [0, 1]
solution = Solution().missingNumberUsingAP(nums)
print(solution)
