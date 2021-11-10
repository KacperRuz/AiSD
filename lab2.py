from typing import Any


class Node:
    value: Any
    next: 'Node'

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    head: Node
    tail: Node
    data: Node

    def __init__(self):
        self.head = None
        self.tail = None
        self.data = None

    def list(self):
        d = self.data
        while True:
            if d is None:
                break
            else:
                print(d.value)
                d = d.next

    def append(self, value: Any):
        n = Node(value)
        if self.data is None:
            self.data = n
        else:
            d = self.data
            while True:
                if d.next is None:
                    d.next = n
                    break
                else:
                    d = d.next


l = LinkedList()
l.append(10)
l.append(32)
l.append("jebac damiana")
l.list()
