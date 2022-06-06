
class Solution:
    def combinationSum(self, candidates, target):
        path = []
        index = 0
        res = []
        candidates.sort()
        self.dfs(candidates, target, index, path, res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return  # succesfully got a solution and returning 1 step back for recursion
        for i in range(index, len(nums)):
            # target is subtracted and path is added
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)


sl = Solution()
print(sl.combinationSum([1, 2], 3))
