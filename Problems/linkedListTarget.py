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

# Iterative solution

# def findTargert(head, target):
#     curr = head
#     while(curr != null):
#         if curr.val == target:
#             return True
#         curr = curr.next
#     return False

# Recursive Solution


def findTarget(head, target):
    curr = head
    # print(curr.val)
    if curr == null:
        return False
    if curr.val == target:
        print(curr.val)
        return True

    curr = curr.next
    return findTarget(curr, target)


print(findTarget(a, "B"))
