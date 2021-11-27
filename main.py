from typing import Any, List, Callable


class Tree:
    def __init__(self):
        self.root = TreeNode


class TreeNode:
    children = []

    def __init__(self, value: Any, children: List['TreeNode'], parent: 'TreeNode') -> None:
        self.value = value
        self.children = children
        self.parent = parent

    def __str__(self) -> str:
        return str(self.value)

    # todo: visit self
    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]):
        if self.is_leaf() is False:
            for x in self.children:
                visit(x)
                x.for_each_deep_first(visit)

    def is_leaf(self) -> bool:
        if len(self.children) == 0:
            return True
        return False

    def add(self, child: 'TreeNode') -> None:
        child.parent = self
        self.children.append(child)


def test(node: 'TreeNode') -> None:
    print(node.value)


a = TreeNode(10, [], None)
b = TreeNode(20, [], None)
c = TreeNode(30, [], None)

a.add(b)
a.add(c)

d = TreeNode(40, [], None)
e = TreeNode(50, [], None)
b.add(d)
b.add(e)

# print(len(t.children))
# print(a.children)

a.for_each_deep_first(test)


