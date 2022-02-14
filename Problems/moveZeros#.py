

from numpy import append
from sqlalchemy import true


def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    # best solutino O(n)

    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0 and nums[slow] == 0:
            nums[fast], nums[slow] = nums[slow], nums[fast]

        if nums[slow] != 0:
            slow += 1

    print(nums)

    # buff = []
    # result = []

    # for i in range(len(nums)):
    #     if nums[i] == 0:
    #         buff.append(0)
    #     else:
    #         result.append(nums[i])
    # result += buff
    # print(result)

    j = 0
    i = 0
    end = len(nums) - 1

    while i < len(nums) and end > 0:

        if nums[i] == 0:

            j = i
            while j+1 < len(nums):
                buff = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = buff
                j += 1
            end -= 1
        else:
            pass
            i += 1

    print(nums)


moveZeroes([1, 0, 2, 0, 0, 0, 3, 5, 7])
