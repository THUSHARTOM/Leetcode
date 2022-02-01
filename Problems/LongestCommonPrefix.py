
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
# strs = ["Thushar", "Tom"]
# for i in zip(*strs):
#     print(set(i))
#     if len(set(i)) != 1:
#         print(set(i))
#         break

# print(len(set(zip(*strs))))


# for i in zip(*strs):
#     print(i)
