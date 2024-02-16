# import
from collections import defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        _dict = defaultdict(list)
        for ch in s:
            _dict[ch].append(ch)

        _dict = sorted(_dict.values(), key=len, reverse=True)
        _dict = "".join(["".join(inner_list) for inner_list in _dict])
        return _dict


s = "tree"
solution = Solution()
print(solution.frequencySort(s))
