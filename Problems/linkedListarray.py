from sqlalchemy import null


class Node:
    def __init__(self, val):
        self.val = val
        self.next = null


a = Node("1")
b = Node("2")
c = Node("3")
d = Node("4")

a.next = b
b.next = c
c.next = d

arr = []


def traverse(head):
    curr = head
    while(curr != null):
        print(".")
        arr.append(curr.val)
        curr = curr.next
    print(arr)


traverse(a)
