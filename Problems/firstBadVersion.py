# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lb = 1
        ub = n
        while lb <= ub:
            mid = (lb + ub)//2
            if isBadVersion(mid):
                ub = mid-1
            else:
                lb = mid + 1
        return lb
