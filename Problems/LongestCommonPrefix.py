# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         prefx = ""
#         for i in range(len(strs)):
#             strs[i]


# class Solution:
#     def longestCommonPrefix(self, strs) -> str:
#         bestString = ''

#         for i in zip(*strs):
#             print(i)
#             if len(set(i)) != 1:
#                 break
#             bestString += i[0]
#         return bestString


# sl = Solution()
# print(sl.longestCommonPrefix(["hi", "hello"]))
strs = "Thushar"

for i in zip(*strs):
    print(i)
