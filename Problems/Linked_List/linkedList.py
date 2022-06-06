from sqlalchemy import null


class Node:
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

# Itereative

# def printLinkedList(head):
#     curr = head
#     while(curr != null):
#         print(curr.val)
#         curr = curr.next

# Recursive


def printLinkedList(head):
    if head == null:
        return null
    else:
        print(head.val)
        printLinkedList(head.next)


printLinkedList(a)
