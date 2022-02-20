from sqlalchemy import null
from torch import ne


class Node():
    def __init__(self, val):
        self.val = val
        self.next = null


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.next = b
b.next = c
c.next = d

# Iterative Time: O(n) space: O(1)

# def reverse(head):
#     # current, next, prev
#     curr = head
#     prev = null

#     while(curr != null):
#         next = curr.next
#         curr.next = prev
#         prev = curr
#         curr = next

#     return prev.val


# Recursive Time: O(n) space: O(n)

def reverse(head, prev=null):
    if head == null:
        return prev.val
    curr = head
    next = curr.next
    return reverse(next, curr)


print(reverse(a))
