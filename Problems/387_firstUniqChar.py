from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        mapping = Counter(s)
        for i, ch in enumerate(s):
            if mapping[ch] == 1:
                return i
        return -1
