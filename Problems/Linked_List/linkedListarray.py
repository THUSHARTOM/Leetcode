from sqlalchemy import null


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def make_list(elements):
    head = Node(elements[0])
    for element in elements[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = Node(element)
    return head

# a = Node("1")
# b = Node("2")
# c = Node("3")
# d = Node("4")

# a.next = b
# b.next = c
# c.next = d


arr = []


def traverse(head):
    curr = head
    while(curr != None):
        print(".")
        arr.append(curr.val)
        curr = curr.next
    print(arr)


a = make_list([1, 2, 3, 4])
traverse(a)
