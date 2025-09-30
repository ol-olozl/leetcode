class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ret = s[0]

        for i in range(n):
            left = i
            right = n - 1

            while left < right:
                if s[left] != s[right]:
                    right -= 1
                    continue

                l, r = left, right
                half = []
                while l < r and s[l] == s[r]:
                    half.append(s[l])
                    l += 1
                    r -= 1

                if l < r and s[l] != s[r]:
                    right -= 1
                    continue

                if l == r:
                    cand = "".join(half) + s[l] + "".join(reversed(half))
                else:
                    cand = "".join(half) + "".join(reversed(half))

                if len(cand) > len(ret):
                    ret = cand
                break

        return ret
