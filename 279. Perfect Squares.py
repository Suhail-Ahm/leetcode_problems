class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        squares = [i**2 for i in range(1, int(n**0.5) + 1)]
        for i in range(1, n + 1):
            min_squares = float("inf")
            for square in squares:
                if square > i:
                    break
                min_squares = min(min_squares, dp[i - square] + 1)
            dp[i] = min_squares
        return dp[n]


solution = Solution()
print(solution.numSquares(12))
