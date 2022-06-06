from collections import Counter
# The idea, is that frequency of any element can not be more than n


class Solution:
    def topKFrequent(self, nums, k):
        result = []
        bucket = [[] for _ in range(len(nums)+1)]
        count = Counter(nums).items()

        for num, freq in count:
            bucket[freq].append(num)
        print(bucket)
        bucket.reverse()
        for i in bucket:
            if i != [] and k > 0:
                k -= 1
                # print(elem for elem in i)
                result.append(i)
        # print(result)
        return result


sl = Solution()
sl.topKFrequent([1, 2], 2)
# # import counter class from collections module

# # Creation of a Counter Class object using
# # string as an iterable data container
# x = Counter("geeksforgeeks")

# # printing the elements of counter object
# # for i in x.elements():
# #     print(i, end=" ")

# print(x.items())
