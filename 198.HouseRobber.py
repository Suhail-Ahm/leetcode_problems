from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # Create an array to store the maximum amount of money robbed up to each house
        dp = [0] * n

        # Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Dynamic programming to fill in the rest of the array
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        # The final result is the maximum amount of money that can be robbed without alerting the police
        return dp[-1]


# Example usage:
solution = Solution()
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([2, 7, 9, 3, 1]))  # Output: 12
