class Solution:
    def reverseString(self, s):

        # lb = 0
        # ub = len(s)-1
        # while(lb < ub):
        #     s[lb], s[ub] = s[ub], s[lb]
        #     lb += 1
        #     ub -= 1
        # print(s)
        # return s

        # easiest sol
        s[:] = s[::-1]
        print(s)


sl = Solution
st = ["h", "e", "l", "l", "o"]
st = st[:: -1]
print(st)
sl.reverseString(sl, st)
