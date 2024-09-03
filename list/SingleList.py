from typing import Generic, Optional, TypeVar
from list.List import List

T = TypeVar("T")


class SingleNode(Generic[T]):
    def __init__(self, data: T):
        # データへの参照
        self.data = data
        # 次の要素への参照
        self.next: Optional[SingleNode[T]] = None


class SingleList(List[T]):
    def __init__(self):
        # 先頭要素への参照
        self.head: Optional[SingleNode[T]] = None
        # リストの長さ
        self.size: int = 0

    def __get_node(self, index: int) -> SingleNode[T]:
        self.__validate_index(index)

        current_node = self.head
        for _i in range(index):
            current_node = current_node.next
        return current_node

    def __validate_index(self, index: int, inserting: bool = False):
        if (
            index < 0
            or (inserting and index > self.size)
            or (not inserting and index >= self.size)
        ):
            raise IndexError("Index out of bounds")

    def insert(self, index: int, value: T):
        if not isinstance(value, self.__orig_class__.__args__[0]):
            raise TypeError(f"Expected value of type {self.__orig_class__.__args__[0]}, got {type(value)}")
    
        self.__validate_index(index, inserting=True)

        new_node = SingleNode(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev_node = self.__get_node(index - 1)
            new_node.next = prev_node.next
            prev_node.next = new_node

        self.size += 1

    def remove(self, index: int):
        self.__validate_index(index)

        if index == 0:
            self.head = self.head.next
        else:
            prev_node = self.__get_node(index - 1)
            prev_node.next = prev_node.next.next

        self.size -= 1

    def length(self) -> int:
        return self.size

    def get(self, index: int) -> T:
        current_node = self.__get_node(index)
        return current_node.data

    def clear(self):
        self.head = None
        self.size = 0

    def display(self):
        elements = []
        for i in range(self.size):
            elements.append(self.get(i))
        print(elements)
