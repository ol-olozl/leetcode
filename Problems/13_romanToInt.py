class Solution:
    def romanToInt(self, s: str) -> int:
        dct = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        tot = 0
        prev = float(inf)
        for sym in s:
            val = dct[sym]
            if prev >= val:
                tot += val
            else:
                tot += val - prev*2
            prev = val
        return tot
