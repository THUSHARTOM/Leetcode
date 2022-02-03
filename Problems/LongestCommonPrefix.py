
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        bestString = ""
        for i in zip(*strs):
            print(i)
            if len(set(i)) != 1:  # As set() deletes duplicate
                break
            bestString += i[0]
        return bestString


sl = Solution()
print(sl.longestCommonPrefix(["flower", "flow", "flight"]))
