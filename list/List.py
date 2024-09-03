from typing import TypeVar, Generic
from typeguard import typechecked


T = TypeVar("T")


@typechecked
class List(Generic[T]):
    def insert(self, index: int, value: T):
        """指定IndexにNode追加

        Args:
            index: ノードを削除する位置のインデックス。
            value: 追加するノードのデータ。T 型に従う

        Raises:
            IndexError: Index がリスト範囲外の場合にエラーとなる。
        """
        raise NotImplementedError

    def remove(self, index: int):
        """指定IndexのNode削除

        Args:
            index: ノードを削除する位置のインデックス。

        Raises:
            IndexError: Index がリスト範囲外の場合にエラーとなる。
        """
        raise NotImplementedError

    def length(self) -> int:
        """Listの長さ取得

        Returns:
            int: リスト内のノードの数。
        """
        raise NotImplementedError

    def get(self, index: int) -> T:
        """指定IndexのNodeがあるかを確認

        Args:
            index: 値を取得する位置のインデックス。

        Returns:
            T: 指定されたインデックスにあるノードの値。

        Raises:
            IndexError: Index がリスト範囲外の場合にエラーとなる。
        """
        raise NotImplementedError

    def clear(self):
        """List全体を空にする"""
        raise NotImplementedError

    def display(self):
        """List全体のString表示

        Note:
            リスト全体の要素を表示する。（現場では必要ない処理となってしまいケースが多いと思いますが、テストする時に便利で一応用意することとしました。）
        """
        raise NotImplementedError
