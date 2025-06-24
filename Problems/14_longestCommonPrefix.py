class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            for i in range(len(prefix)):
                if (len(s) <= i) or (prefix[i] != s[i]):
                    prefix = prefix[:i]
                    break
        return prefix
