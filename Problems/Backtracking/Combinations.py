# Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

# You may return the answer in any order

# ex ->
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

def combine(n, k):
    res = []
    dfs(range(1, n+1), k, 0, [], res)
    return res


def dfs(nums, k, index, path, res):
    if k == 0:
        res.append(path)
        return  # backtracking

    for i in range(index, len(nums)):
        return dfs(nums, k-1, i+1, path + [nums[i]], res)


print(combine(4, 2))
