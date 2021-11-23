from typing import Any

from lab2 import LinkedList


class Queue:
    def __init__(self) -> None:
        self.storage = LinkedList()

    def __str__(self) -> str:
        return self.storage.__str__()

    def __len__(self) -> int:
        return self.storage.size

    def peek(self) -> Any:
        return self.storage.head.value

    def enqueue(self, value: Any) -> None:
        self.storage.append(value)

    def dequeue(self) -> Any:
        return self.storage.pop()


q = Queue()

q.enqueue("klient1")
q.enqueue("klient2")
q.enqueue("klient3")

print(q)

print(q.dequeue())
print(len(q))
print(q)

