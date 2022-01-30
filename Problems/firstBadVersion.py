# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lb = 1
        ub = n
        if n == 1:
            mid = 1
        while lb <= ub:
            mid = (lb + ub)//2
            if isBadVersion(mid):
                if isBadVersion(mid-1):
                    ub = mid-1

                else:
                    return mid

            else:
                lb = mid + 1
        return mid
