import unittest
from io import StringIO
from typing import TypeVar
from unittest.mock import patch
from list.DoubleList import DoubleList

T = TypeVar("T")

def list_LS0():
    return DoubleList[str]()
    
def list_LS1(): 
    list = list_LS0()
    list.insert(0, 'A')
    return list

def list_LS2(): 
    list =list_LS1()
    list.insert(1, 'B')
    return list
    
def list_LS3(): 
    list = list_LS2()
    list.insert(2, 'C')
    return list
    
class DoubleTestList(unittest.TestCase):
    """
    このテストクラスは、DoubleListクラスの以下の条件と組み合わせに対する動作をテストする。

    **List Size(LS)に関するケース:**
    - LS0: リストのサイズが0 (リストが空)
    - LS1: リストのサイズが1
    - LS2: リストのサイズが2
    - LS3: リストのサイズが3

    **Node Index(NI) に関するケース:**
    - NI0: ノードがリストの先頭にある場合 (index = 0)
    - NI1: ノードがリストの中間にある場合
    - NI2: ノードがリストの末尾にある場合 (index == size または index == size - 1)
  
    **Error(E) に関数ケース**
    - E1: TypeError, タイプが不適切である場合
    - E2: IndexError, Indexが無効 (Index == -1など)である場合
    - E3: IndexError, Indexが実行対象リストに存在していない場合
    
    **テストマトリックス:**
    |      | LS0  | LS1  | LS2  | LS3  |
    |------|------|------|------|------|
    | NI0  | ○    | ○    | ○    | ○    |
    | NI1  | x    | ○    | ○    | ○    |
    | NI2  | x    | x    | ○    | ○    |
    | E1   | ○    | ×    | ×    | ×    |
    | E2   | ○    | ×    | ×    | ×    |
    | E3   | ○    | ○    | ○    | ○    |

    - ○: 実施するテスト
    - ×: テスト対象外

    """
    def setUp(self):
        self.list = list_LS0()
    
    # INSERT 異常処理
    def test_insert_E1_LS0(self):
        """ INSERT TypeError & ListSize == 0
        事前条件: リストは空 (Size == 0)
        RUN条件: 不適切なタイプの値を挿入する
        期待値: TypeErrorが発生する
        """
        self.list =  list_LS1()
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.list.display()
            self.assertIn("['A']", fake_out.getvalue())
        
        with self.assertRaises(TypeError):
            self.list.insert(0, 10)

    def test_insert_E2_LS0(self):   
        """ INSERT IndexError無効 + ListSize == 0
        事前条件: リストは空 (Size == 0)
        RUN条件: 無効なindex (例: -1) を指定して要素を挿入する
        期待値: IndexErrorが発生する
        """
        self.list =list_LS0()
        with self.assertRaises(IndexError):
            self.list.insert(-1, 'TARGET')
    
    def test_insert_E3_LS0(self):
        """ INSERT IndexError & ListSize == 0
        事前条件: リストは空 (Size == 0)
        RUN条件: 実行対象リストに存在していないindexを指定して要素を挿入する
        期待値: IndexErrorが発生する
        """
        self.list =list_LS0()
        with self.assertRaises(IndexError):
            self.list.insert(1, 'TARGET')

    def test_insert_E3_LS1(self):
        """ INSERT IndexError & ListSize == 1
        事前条件: リストには1つの要素が存在する (Size == 1)
        RUN条件: 実行対象リストに存在していないindexを指定して要素を挿入する
        期待値: IndexErrorが発生する
        """
        self.list =list_LS1()
        with self.assertRaises(IndexError):
            self.list.insert(2, 'TARGET')

    def test_insert_E3_LS2(self):
        """ INSERT IndexError & ListSize == 2
        事前条件: リストには2つの要素が存在する (Size == 2)
        RUN条件: 実行対象リストに存在していないindexを指定して要素を挿入する
        期待値: IndexErrorが発生する
        """
        self.list =list_LS2()
        with self.assertRaises(IndexError):
            self.list.insert(3, 'TARGET')

    def test_insert_E3_LS3(self):
        """ INSERT IndexError & ListSize == 3
        事前条件: リストには3つの要素が存在する (Size == 3)
        RUN条件: 実行対象リストに存在していないindexを指定して要素を挿入する
        期待値: IndexErrorが発生する
        """
        self.list =list_LS3()
        with self.assertRaises(IndexError):
            self.list.insert(4, 'TARGET')

    # INSERT 通常処理
    def test_insert_LS0_NI0(self):
        """ INSERT ListSize == 0 & NodeIndex  == 0
        事前条件: リストは空 (Size == 0)
        RUN条件: index = 0 に要素を挿入する
        期待値: リストに要素が1つだけ存在する
        """
        self.list =list_LS0()
        self.list.insert(0, 'TARGET')
        self.assertEqual(self.list.length(), 1)
        self.assertEqual(self.list.get(0), 'TARGET')

    def test_insert_LS1_NI0(self):
        """ INSERT ListSize == 1 & NodeIndex  == 0
        事前条件: リストには1つの要素が存在する (Size == 1)
        RUN条件: index = 0 に要素を挿入する
        期待値: 新しい要素がリストの先頭に挿入される
        """
        self.list = list_LS0()
        self.list.insert(0, 'TARGET')
        self.assertEqual(self.list.length(), 1)
        self.assertEqual(self.list.get(0), 'TARGET')

    def test_insert_LS1_NI1(self):
        """ INSERT ListSize == 1 & NodeIndex  == 2
        事前条件: リストには1つの要素が存在する (Size == 1)
        RUN条件: index = 1 に要素を挿入する
        期待値: 新しい要素がリストの末尾に挿入される
        """
        self.list =list_LS1()
        self.list.insert(1, 'TARGET')
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(self.list.get(1), 'TARGET')

    def test_insert_LS2_NI0(self):
        """ INSERT ListSize == 2 & NodeIndex == 0
        事前条件: リストには2つの要素が存在する (Size == 2)
        RUN条件: index = 0 に要素を挿入する
        期待値: 新しい要素がリストの先頭に挿入される
        """
        self.list =list_LS2()
        
        self.list.insert(0, 'TARGET')
        self.assertEqual(self.list.length(), 3)
        self.assertEqual(self.list.get(0), 'TARGET')

    def test_insert_LS2_NI1(self):
        """ INSERT ListSize == 2 & NodeIndex == 1
        事前条件: リストには2つの要素が存在する (Size == 2)
        RUN条件: index = 1 に要素を挿入する
        期待値: 新しい要素がリストの中間に挿入される
        """
        self.list =list_LS2()
        
        self.list.insert(1, 'TARGET')
        self.assertEqual(self.list.length(), 3)
        self.assertEqual(self.list.get(1), 'TARGET')

    def test_insert_LS2_NI2(self):
        """ INSERT ListSize == 2 & NodeIndex == 2
        事前条件: リストには2つの要素が存在する (Size == 2)
        RUN条件: index = 2 に要素を挿入する
        期待値: 新しい要素がリストの末尾に挿入される
        """
        self.list =list_LS2()
        
        self.list.insert(1, 'TARGET')
        self.assertEqual(self.list.length(), 3)
        self.assertEqual(self.list.get(1), 'TARGET')

    def test_insert_LS3_NI0(self):
        """ INSERT ListSize == 3 & NodeIndex == 0
        事前条件: リストには3つの要素が存在する (Size == 3)
        RUN条件: index = 0 に要素を挿入する
        期待値: 新しい要素がリストの先頭に挿入される
        """
        self.list =list_LS3()
        
        self.list.insert(0, 'TARGET')
        self.assertEqual(self.list.length(), 4)
        self.assertEqual(self.list.get(0), 'TARGET')

    def test_insert_LS3_NI1(self):
        """ INSERT ListSize == 3 & NodeIndex == 1
        事前条件: リストには3つの要素が存在する (Size == 3)
        RUN条件: index = 2 に要素を挿入する
        期待値: 新しい要素がリストの中間に挿入される
        """
        self.list =list_LS3()
        
        self.list.insert(1, 'TARGET')
        self.assertEqual(self.list.length(), 4)
        self.assertEqual(self.list.get(1), 'TARGET')

    def test_insert_LS3_NI2(self):
        """INSERT ListSize == 3 & NodeIndex == 2
        事前条件: リストには3つの要素が存在する (Size == 3)
        RUN条件: index = 3 に要素を挿入する
        期待値: 新しい要素がリストの末尾に挿入される
        """
        self.list =list_LS3()
        
        self.list.insert(2, 'TARGET')
        self.assertEqual(self.list.length(), 4)
        self.assertEqual(self.list.get(2), 'TARGET')
    
    # REMOVE 異常処理
    def test_remove_E2_LS0(self):
        """REMOVE IndexError（無効なIndex） & ListSize == 0
        事前条件: リストは空 (Size == 0)
        RUN条件: 無効なindex (例: -1) を指定して要素を削除する
        期待値: IndexErrorが発生する
        """
        self.list =list_LS0()
        
        with self.assertRaises(IndexError):
            self.list.remove(-1)

    def test_remove_E3_LS0(self):
        """ REMOVE IndexError（存在していないIndex） & ListSize == 0    
        事前条件: リストは空 (Size == 0)
        RUN条件: 実行対象リストに存在していないindex (例: 1) を指定して要素を削除する
        期待値: IndexErrorが発生する
        """
        self.list =list_LS0()
        
        with self.assertRaises(IndexError):
            self.list.remove(1)

    def test_remove_E3_LS1(self):
        """ REMOVE IndexError（存在していないIndex） & ListSize == 1   
        事前条件: リストには1つの要素が存在する (Size == 1)
        RUN条件: 実行対象リストに存在していないindex (例: 2) を指定して要素を削除する
        期待値: IndexErrorが発生する
        """
        self.list =list_LS1()
        
        with self.assertRaises(IndexError):
            self.list.remove(2)

    def test_remove_E3_LS2(self):
        """ REMOVE IndexError（存在していないIndex） & ListSize == 2    
        事前条件: リストには2つの要素が存在する (Size == 2)
        RUN条件: 実行対象リストに存在していないindex (例: 3) を指定して要素を削除する
        期待値: IndexErrorが発生する
        """
        self.list =list_LS2()
        
        with self.assertRaises(IndexError):
            self.list.remove(3)

    def test_remove_E3_LS3(self):
        """ REMOVE IndexError（存在していないIndex） & ListSize == 3   
        事前条件: リストには3つの要素が存在する (Size == 3)
        RUN条件: 実行対象リストに存在していないindex (例: 4) を指定して要素を削除する
        期待値: IndexErrorが発生する
        """
        self.list =list_LS3()
        
        with self.assertRaises(IndexError):
            self.list.remove(4)
    
    # REMOVE　通常処理
    def test_remove_LS1_NI0(self):
        """ REMOVE NodeIndex == 0 & ListSize == 1
        事前条件: リストには1つの要素が存在する (Size == 1)
        RUN条件: index = 0 の要素を削除する
        期待値: リストが空になる
        """
        self.list =list_LS1()
        
        self.list.remove(0)
        self.assertEqual(self.list.length(), 0)

    def test_remove_LS2_NI0(self):
        """ REMOVE NodeIndex == 0 & ListSize == 2
        事前条件: リストには2つの要素が存在する (Size == 2)
        RUN条件: index = 0 の要素を削除する
        期待値: リストの先頭要素が削除され、次の要素が先頭になる
        """
        self.list =list_LS2()
        
        self.list.remove(0)
        self.assertEqual(self.list.length(), 1)
        self.assertEqual(self.list.get(0), 'B')

    def test_remove_LS2_NI1(self):
        """ REMOVE NodeIndex == 1 & ListSize == 2
        事前条件: リストには2つの要素が存在する (Size == 2)
        RUN条件: index = 1 の要素を削除する
        期待値: リストの末尾要素が削除される
        """
        self.list =list_LS2()
        
        self.list.remove(1)
        self.assertEqual(self.list.length(), 1)
        self.assertEqual(self.list.get(0), 'A')

    def test_remove_LS3_NI0(self):
        """ REMOVE NodeIndex == 0 & ListSize == 3
        事前条件: リストには3つの要素が存在する (Size == 3)
        RUN条件: index = 0 の要素を削除する
        期待値: リストの先頭要素が削除され、次の要素が先頭になる
        """
        self.list =list_LS3()
        
        self.list.remove(0)
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(self.list.get(0), 'B')
        self.assertEqual(self.list.get(1), 'C')
        
    def test_remove_LS3_NI1(self):
        """ REMOVE NodeIndex == 1 & ListSize == 3
        事前条件: リストには3つの要素が存在する (Size == 3)
        RUN条件: index = 1 の要素を削除する
        期待値: リストの中間要素が削除され、他の要素が繰り上がる
        """
        self.list =list_LS3()
        
        self.list.remove(1)
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(self.list.get(0), 'A')
        self.assertEqual(self.list.get(1), 'C')

    def test_remove_LS3_NI2(self):
        """ REMOVE NodeIndex == 2 & ListSize == 3
        事前条件: リストには3つの要素が存在する (Size == 3)
        RUN条件: index = 2 の要素を削除する
        期待値: リストの末尾要素が削除される
        """
        self.list = list_LS3()
        
        self.list.remove(2)
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(self.list.get(0), 'A')
        self.assertEqual(self.list.get(1), 'B')

    # REVERSE　通常処理
    def test_reverse_LS0(self):
        self.list = list_LS0()
        self.list.reverse()
        self.assertEqual(self.list.length(), 0)
        
        expected_output = "[]"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.list.display()
            self.assertIn(expected_output, fake_out.getvalue())
    
    def test_reverse_LS1(self):
        self.list = list_LS1()
        self.list.reverse()
        self.assertEqual(self.list.length(), 1)
        
        expected_output = "['A']"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.list.display()
            self.assertIn(expected_output, fake_out.getvalue())
    
    def test_reverse_LS2(self):
        self.list = list_LS2()
        self.list.reverse()
        self.assertEqual(self.list.length(), 2)
        
        expected_output = "['B', 'A']"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.list.display()
            self.assertIn(expected_output, fake_out.getvalue())
    
    def test_reverse_LS3(self):
        self.list = list_LS3()
        self.list.reverse()
        self.assertEqual(self.list.length(), 3)
        
        expected_output = "['C', 'B', 'A']"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.list.display()
            self.assertIn(expected_output, fake_out.getvalue())
        
    # LENGTH 通常処理 
    def test_length_LS0(self):
        """ LENGTH ListSize == 0
        事前条件: リストは空 (Size == 0)
        RUN条件: リストのサイズを取る
        期待値: リストのサイズが０である
        """
        self.list =list_LS0()
        
        self.assertEqual(self.list.length(), 0)
    
    def test_length_LS1(self):
        """ LENGTH ListSize == 1
        事前条件: リストには1つの要素が存在する (Size == 1)
        RUN条件: リストのサイズを取る
        期待値: リストのサイズが1である
        """
        self.list =list_LS1()

        self.assertEqual(self.list.length(), 1)

    def test_length_LS2(self):
        """ LENGTH ListSize == 2
        事前条件: リストには2つの要素が存在する (Size == 2)
        RUN条件: リストのサイズを取る
        期待値: リストのサイズが3である
        """
        self.list =list_LS2()

        self.assertEqual(self.list.length(), 2)

    def test_length_LS3(self):
        """ LENGTH ListSize == 3
        事前条件: リストには3つの要素が存在する (Size == 3)
        RUN条件: リストのサイズを取る
        期待値: リストのサイズが3である
        """
        self.list =list_LS3()

        self.assertEqual(self.list.length(), 3)

    # GET 異常処理
    def test_get_E1_LS0(self):
        """ LENGTH TypeError & ListSize == 0
        事前条件: リストは空 (Size == 0)
        RUN条件: 無効なタイプの値を取得する
        期待値: TypeErrorが発生する
        """
        self.list =list_LS0()
        
        with self.assertRaises(TypeError):
            self.list.get("invalid_type")

    def test_get_E2_LS0(self):
        """ LENGTH IndexError（無効なIndex） & ListSize == 0
        事前条件: リストは空 (Size == 0)
        RUN条件: 無効なindex (例: -1) を指定して要素を取得する
        期待値: IndexErrorが発生する
        """
        self.list =list_LS0()
        
        with self.assertRaises(IndexError):
            self.list.get(-1)

    def test_get_E3_LS0(self):
        """ LENGTH IndexError（存在していないIndex） & ListSize == 0
        事前条件: リストは空 (Size == 0)
        RUN条件: 実行対象リストに存在していないindex (例: 1) を指定して要素を取得する
        期待値: IndexErrorが発生する
        """
        self.list =list_LS0()
        
        with self.assertRaises(IndexError):
            self.list.get(1)

    def test_get_E3_LS1(self):
        """ LENGTH IndexError（存在していないIndex） & ListSize == 1
        事前条件: リストには1つの要素が存在する (Size == 1)
        RUN条件: 実行対象リストに存在していないindex (例: 2) を指定して要素を取得する
        期待値: IndexErrorが発生する
        """
        self.list =list_LS1()
        
        with self.assertRaises(IndexError):
            self.list.get(2)

    def test_get_E3_LS2(self):
        """ LENGTH IndexError（存在していないIndex） & ListSize == 2
        事前条件: リストには2つの要素が存在する (Size == 2)
        RUN条件: 実行対象リストに存在していないindex (例: 3) を指定して要素を取得する
        期待値: IndexErrorが発生する
        """
        self.list =list_LS2()
        
        with self.assertRaises(IndexError):
            self.list.get(3)

    def test_get_E3_LS3(self):
        """ LENGTH IndexError（存在していないIndex） & ListSize == 3
        事前条件: リストには3つの要素が存在する (Size == 3)
        RUN条件: 実行対象リストに存在していないindex (例: 4) を指定して要素を取得する
        期待値: IndexErrorが発生する
        """
        self.list =list_LS3()
        
        with self.assertRaises(IndexError):
            self.list.get(4)
    
    #  GET 通常処理
    def test_get_LS1_NI0(self):
        """ GET NodeIndex == 0 & ListSize == 0
        事前条件: リストには1つの要素が存在する (Size == 1)
        RUN条件: index = 0 の要素を取得する
        期待値: リストの先頭要素が返される
        """
        self.list =list_LS1()
        
        self.assertEqual(self.list.get(0), 'A')

    def test_get_LS2_NI0(self):
        """ GET NodeIndex == 0 & ListSize == 2
        事前条件: リストには2つの要素が存在する (Size == 2)
        RUN条件: index = 0 の要素を取得する
        期待値: リストの先頭要素が返される
        """
        self.list =list_LS2()
        
        self.assertEqual(self.list.get(0), 'A')

    def test_get_LS2_NI1(self):
        """ GET NodeIndex == 1 & ListSize == 2
        事前条件: リストには2つの要素が存在する (Size == 2)
        RUN条件: index = 1 の要素を取得する
        期待値: リストの末尾要素が返される
        """
        self.list =list_LS2()
        
        self.list.insert(0, 'A')
        self.list.insert(1, 'B')
        self.assertEqual(self.list.get(1), 'B')

    def test_get_LS3_NI0(self):
        """ GET NodeIndex == 0 & ListSize == 3
        事前条件: リストには3つの要素が存在する (Size == 3)
        RUN条件: index = 0 の要素を取得する
        期待値: リストの先頭要素が返される
        """
        self.list =list_LS3()
        
        self.assertEqual(self.list.get(0), 'A')

    def test_get_LS3_NI1(self):
        """ GET NodeIndex == 1 & ListSize == 3
        事前条件: リストには3つの要素が存在する (Size == 3)
        RUN条件: index = 1 の要素を取得する
        期待値: リストの中間要素が返される
        """
        self.list =list_LS3()
        
        self.assertEqual(self.list.get(1), 'B')

    def test_get_LS3_NI2(self):
        """ GET NodeIndex == 2 & ListSize == 3
        事前条件: リストには3つの要素が存在する (Size == 3)
        RUN条件: index = 2 の要素を取得する
        期待値: リストの末尾要素が返される
        """
        self.list =list_LS3()
        
        self.assertEqual(self.list.get(2), 'C')

    #  CLEAR 通常
    def test_clear_LS0(self):
        """ CLEAR ListSize == 0
        事前条件: リストは空 (Size == 0)
        RUN条件: リストをクリアする
        期待値: リストが空になる
        """
        self.list =list_LS0()
        
        self.list.clear()
        self.assertEqual(self.list.length(), 0)

    def test_clear_LS1(self):
        """ CLEAR ListSize == 1
        事前条件: リストには1つの要素が存在する (Size == 1)
        RUN条件: リストをクリアする
        期待値: リストが空になる
        """
        self.list =list_LS1()
        
        self.list.clear()
        self.assertEqual(self.list.length(), 0)

    def test_clear_LS2(self):
        """ CLEAR ListSize == 2
        事前条件: リストには2つの要素が存在する (Size == 2)
        RUN条件: リストをクリアする
        期待値: リストが空になる
        """
        self.list =list_LS2()
        
        self.list.clear()
        self.assertEqual(self.list.length(), 0)

    def test_clear_LS3(self):
        """ CLEAR ListSize == 3
        事前条件: リストには3つの要素が存在する (Size == 3)
        RUN条件: リストをクリアする
        期待値: リストが空になる
        """
        self.list =list_LS3()
        
        self.list.clear()
        self.assertEqual(self.list.length(), 0)

    # DISPLAY 通常
    def test_display_LS0(self):
        """ DISPLAY ListSize == 0
        事前条件: リストは空 (Size == 0)
        RUN条件: リストの要素を表示する
        期待値: 要素が正しく表示される
        """
        self.list =list_LS0()
        
        expected_output = "[]"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.list.display()
            self.assertIn(expected_output, fake_out.getvalue())

    def test_display_LS1(self):
        """ DISPLAY ListSize == 1
        事前条件: リストには1つの要素が存在する (Size == 1)
        RUN条件: リストの要素を表示する
        期待値: 要素が正しく表示される
        """
        self.list =list_LS1()
        
        expected_output = "['A']"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.list.display()
            self.assertIn(expected_output, fake_out.getvalue())

    def test_display_LS2(self):
        """ DISPLAY ListSize == 2
        事前条件: リストには2つの要素が存在する (Size == 2)
        RUN条件: リストの要素を表示する
        期待値: 要素が正しく表示される
        """
        self.list =list_LS2()

        expected_output = "['A', 'B']"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.list.display()
            self.assertIn(expected_output, fake_out.getvalue())
            
    def test_display_LS3(self):
        """ DISPLAY ListSize == 3
        事前条件: リストには3つの要素が存在する (Size == 3)
        RUN条件: リストの要素を表示する
        期待値: 要素が正しく表示される
        """
        self.list = list_LS3()

        expected_output = "['A', 'B', 'C']"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.list.display()
            self.assertIn(expected_output, fake_out.getvalue())
