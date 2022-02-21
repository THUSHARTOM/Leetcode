
from sqlalchemy import null


class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

q = Node("Q")
r = Node("R")

a.next = b
b.next = c
c.next = d

q.next = r

# Recursive


def merge(head1, head2):
    if(head1 == None) and (head2 == None):
        return None
    if head1 == None:
        return head2
    if head2 == None:
        return head1

    next1 = head1.next
    next2 = head2. next
    head1.next = head2
    head2.next = merge(next1, next2)
    return head1


# Iterative

# def merge(head1, head2):
#     tail = head1
#     curr1 = tail.next
#     curr2 = head2
#     count = 1
#     while(curr1 != None and curr2 != None):
#         if count == 0:
#             count = 1
#             tail.next = curr1
#             curr1 = curr1.next
#         else:
#             count = 0
#             tail.next = curr2
#             curr2 = curr2.next
#         tail = tail.next
#     if curr1 == None:
#         tail.next = curr2
#         curr = tail.next

#     if curr2 == None:
#         tail.next = curr1

#     return head1


hd = merge(a, q)
curr = hd
while(curr != None):
    print(curr.val)
    curr = curr.next
