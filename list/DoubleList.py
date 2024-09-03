from typing import Generic, Optional, TypeVar
from list.List import List

T = TypeVar("T")

class DoubleNode(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.prev: Optional[DoubleNode[T]] = None
        self.next: Optional[DoubleNode[T]] = None

class DoubleList(List[T]):
    def __init__(self):
        self.head: Optional[DoubleNode[T]] = None
        self.tail: Optional[DoubleNode[T]] = None
        self.size = 0

    def __validate_index(self, index: int, inserting: bool = False):
         if (
            index < 0
            or (inserting and index > self.size)
            or (not inserting and index >= self.size)
        ):
            raise IndexError("Index out of bounds")

    def __get_node(self, index: int) -> DoubleNode[T]:
        self.__validate_index(index)
        
        current_node = self.head
        for _i in range(index):
            current_node = current_node.next
        return current_node

    def insert(self, index: int, value: T):
        if not isinstance(value, self.__orig_class__.__args__[0]):
            raise TypeError(f"Expected value of type {self.__orig_class__.__args__[0]}, got {type(value)}")

        self.__validate_index(index, inserting=True)
        
        new_node = DoubleNode(value)

        if index == 0:
            if self.head:
                self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            prev_node = self.__get_node(index - 1)
            next_node = prev_node.next

            new_node.next = next_node
            new_node.prev = prev_node
            
            if next_node:
                next_node.prev = new_node
            else:
                self.tail = new_node

            if prev_node:
                prev_node.next = new_node

        self.size += 1

    def reverse(self):
        if(self.size > 1):
            current_node = self.head
            self.head, self.tail = self.tail, self.head

            for i in range(self.size):        
                current_node.prev, current_node.next = current_node.next, current_node.prev
                current_node = current_node.prev
    
    def remove(self, index: int):
        self.__validate_index(index)

        current_node = self.__get_node(index)
        print(current_node)

        if current_node.prev:
            current_node.prev.next = current_node.next
        else:
            self.head = current_node.next

        if current_node.next:
            current_node.next.prev = current_node.prev
        else:
            self.tail = current_node.prev

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