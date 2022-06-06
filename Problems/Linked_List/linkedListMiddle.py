# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        curr = head
        count = 0
        while(curr != None):
            count += 1
            curr = curr.next

        mid = count//2
        curr = head
        # print(mid)
        while(mid > 0):
            # print(curr.val)
            mid -= 1
            curr = curr.next
        return curr

    # Beautiful solution

    # def middleNode(self, head):
    #     slow = fast = head
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #     return slow
