class Solution:
    def firstUniqChar(self, s: str) -> int:
        char = {}
        for ch in s:
            char[ch] = char.get(ch, 0) + 1

        for i, ch in enumerate(s):
            if char[ch] == 1:
                return i

        return -1


s = "leetcode"
solution = Solution()
print(solution.firstUniqChar(s))
