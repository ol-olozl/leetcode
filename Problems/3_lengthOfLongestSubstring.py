class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_len = 0
        subs = set()

        for end in range(len(s)):
            while s[end] in subs:
                subs.remove(s[start])
                start += 1
            subs.add(s[end])
            max_len = max(max_len, end-start+1)
        return max_len
