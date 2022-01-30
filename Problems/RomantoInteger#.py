from sympy import re


class Solution:
    # largetst to smaller:add them up
    # smaller before larger:subtract smaller
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10,
                 "L": 50, "C": 100, "D": 500, "M": 1000}

        res = 0
        for i in range(len(s)):
            if i+1 < len(s) and roman[s[i+1]] > roman[s[i]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
            #     print(res)
            # print(s[i], i, res)
        return res


sl = Solution()
print(sl.romanToInt("MCMXCIV"))
