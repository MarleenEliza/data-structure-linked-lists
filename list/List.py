from typing import TypeVar, Generic
from typeguard import typechecked


T = TypeVar("T")


@typechecked
class List(Generic[T]):
    def insert(self, index: int, value: T):
        """Add Node to specific index

        Args:
            index: Index for node to be inserted
            value: Value of Node to be added. Has to be type of T

        Raises:
            IndexError: If the index is not in the list, an IndexError will occur
        """
        raise NotImplementedError

    def remove(self, index: int):
        """Remove Node from specific index

        Args:
            index: Index for node to be deleted

        Raises:
            IndexError: If the index is not in the list, an IndexError will occur
        """
        raise NotImplementedError

    def length(self) -> int:
        """Get List Length

        Returns:
            int: number of list length as int
        """
        raise NotImplementedError

    def get(self, index: int) -> T:
        """get value of node of specific index

        Args:
            index: target node index

        Returns:
            T: Value of target node

        Raises:
            IndexError: If the index is not in the list, an IndexError will occur
        """
        raise NotImplementedError

    def clear(self):
        """Clear entire list"""
        raise NotImplementedError

    def display(self):
        """Show entire list in console"""
        raise NotImplementedError
