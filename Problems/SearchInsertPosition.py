class Solution:
    def searchInsert(self, nums, target: int) -> int:
        lb = 0
        ub = len(nums)
        limit = ub
        while lb <= ub:
            mid = int((lb+ub)/2)
            if mid < limit:
                if target <= nums[mid]:
                    ub = mid-1
                else:
                    lb = mid+1
            else:
                return limit

        return lb


sl = Solution()
print(sl.searchInsert([1, 3, 5, 6], 2))
