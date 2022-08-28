# Find the length of a cycle in a linked list
# Possible number of cycles is 0 or 1


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def lengthofcycle(head: Node) -> int:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if not fast or not fast.next:
        return 0

    l = 1
    slow = slow.next
    while slow != fast:
        slow = slow.next
        l += 1
    return l


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    head.next.next.next.next.next.next.next.next = Node(9)
    head.next.next.next.next.next.next.next.next.next = head.next.next.next
    print(lengthofcycle(head))

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print(lengthofcycle(head))

    head = Node(1)
    head.next = Node(18)
    head.next.next = Node(34)
    head.next.next.next = Node(234)
    head.next.next.next.next = head.next
    print(lengthofcycle(head))

    head = Node(2)
    head.next = Node(3)
    head.next.next = Node(4)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(6)
    head.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next = Node(8)
    head.next.next.next.next.next.next.next = head
    print(lengthofcycle(head))
