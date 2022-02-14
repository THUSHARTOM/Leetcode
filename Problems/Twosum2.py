class Solution:
    def twoSum(self, numbers, target: int):
        # dictionary

        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            else:
                dic[num] = i

        # Binary search

        # for i in range(0, len(numbers)):
        #     lb = i+1
        #     ub = len(numbers)-1
        #     mid = len(numbers)//2
        #     tmp = target - numbers[i]
        #     while lb <= ub:
        #         mid = (lb+ub)//2
        #         if numbers[i]+numbers[mid] < target:
        #             lb = mid+1
        #         elif numbers[i]+numbers[mid] > target:
        #             ub = mid - 1

        #         if numbers[i]+numbers[mid] == target and i != mid:
        #             result = [i+1, mid+1]
        #             result.sort()
        #             return result
        # print(lb, ub)

        # best sol
        # lb = 0
        # ub = len(numbers)-1
        # while(numbers[lb]+numbers[ub] != target):
        #     if(numbers[lb]+numbers[ub] < target):
        #         lb += 1
        #     else:
        #         ub -= 1
        # return [lb+1, ub+1]


sl = Solution()
print(sl.twoSum([1, 2, 3, 7, 11, 15], 9))
