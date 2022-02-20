from sqlalchemy import null


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

# Iterative time:O(n) space: O(1)

# def valInTarget(head, index):
#     curr = head
#     count = 0
#     while(curr != null):
#         if count == index:
#             return curr.val
#         else:
#             count += 1
#             curr = curr.next
#     return "Not Found"

# Recursive time: O(n) space: O(n)


def valInTarget(head, index):
    curr = head
    count = index
    if curr == null:
        return False
    if count == 0:
        return curr.val
    curr = curr.next
    count -= 1

    return valInTarget(curr, count)


print(valInTarget(a, 4))
