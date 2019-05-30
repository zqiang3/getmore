class Node(object):
    def __init__(self, value):
        self.next = None
        self.value = value


class List:
    def __init__(self):
        self.head = None

    def insert(self, value):
        newnode = Node(value)
        newnode.next = self.head
        self.head = newnode

    def display(self):
        cursor = self.head
        while cursor != None:
            print cursor.value
            cursor = cursor.next


def check_recurve(la):
    if la.head == None:
        return False

    lb = List()
    cursor = la.head
    while cursor != None:
        lb.insert(cursor.value)
        cursor = cursor.next

    ca = la.head
    cb = lb.head

    flag = True
    while ca != None:
        if ca.value != cb.value:
            flag = False
            break
        ca = ca.next
        cb = cb.next

    return flag


def reverse_list(root):
    if not root:
        return root

    if root.next is None:
        return root

    pre = root
    cur = pre.next
    next = cur.next
    root.next = None
    while True:
        cur.next = pre
        if next is None:
            break
        pre = cur
        cur = next
        next = next.next

    return cur


def check_recurve_v2(la):
    if la.head is None:
        return False

    if la.head.next is None:
        return True

    length = 0
    cur = la.head
    while cur:
        length += 1
        cur = cur.next

    mid = length / 2
    if length % 2 != 0:
        mid += 1
    mid_cur = la.head
    for i in range(length / 2):
        mid_cur = mid_cur.next

    cb = reverse_list(mid_cur)
    ca = la.head
    flag = True
    while cb != None:
        if ca.value != cb.value:
            flag = False
            break

        ca = ca.next
        cb = cb.next

    return flag
        

#====================
al = List()
al.insert(2)
al.insert(3)
al.insert(5)
al.insert(3)
al.insert(2)
al.display()

print check_recurve_v2(al)
