
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


def merge(head1, head2):
    curr1 = head1
    curr2 = head2
    count = 0
    while(curr1 != None and curr2 != None):
        if count == 0:
            count = 1
            tail.next = curr1
            tail = tail.next
            curr1 = curr1.next
        else:
            count = 0
            tail.next = curr2
            tail = tail.next
            curr2 = curr2.next
    if curr1 == None:
        tail.next = curr2
    if curr2 == None:
        tail.next = curr1
    return tail.val


print(merge(a, q))
