# My answer

class Solution:
    def sortedSquares(self, nums):
        sorted = []
        for i in range(len(nums)):
            sorted.append((nums[i]**2))
        sorted.sort()
        # print(sorted)
        return sorted

# Best answer


class Solution:
    def sortedSquares(self, nums):
        answer = [0]*len(nums)
        l, r = 0, len(nums)-1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:

                answer[r-l] = left * left
                l += 1
            else:
                answer[r-l] = right*right
                r -= 1
        return answer


sl = Solution()
print(sl.sortedSquares([-4, -1, 0, 3, 10]))
