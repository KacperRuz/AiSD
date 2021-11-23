from typing import Any

from lab2 import LinkedList


class Stack:
    def __init__(self) -> None:
        self.storage = LinkedList()

    def __str__(self) -> str:
        self.storage.list()
        return ""

    def __len__(self) -> int:
        return self.storage.size

    def push(self, value: Any) -> None:
        self.storage.push(value)

    def pop(self) -> Any:
        return self.storage.pop()


# s = Stack()
# s.push(2)
# s.push(4)
#
# print(s)
#
# s.pop()
# s.pop()
#
# print(len(s))
