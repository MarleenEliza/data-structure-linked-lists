import unittest
from io import StringIO
from typing import TypeVar
from unittest.mock import patch
from list.SingleList import SingleList

T = TypeVar("T")

def list_LS0():
    return SingleList[str]()
    
def list_LS1(): 
    list = list_LS0()
    list.insert(0, 'A')
    return list

def list_LS2(): 
    list =list_LS1()
    list.insert(1, 'B')
    return list
    
def list_LS3(): 
    list =list_LS2()
    list.insert(2, 'C')
    return list
    
class SingleTestList(unittest.TestCase):
    """
    Unit Test class for SingleList Class.

    **List Size(LS) test cases**
    - LS0: ListSize == 0 (list is empty)
    - LS1: ListSize == 1
    - LS2: ListSize == 2
    - LS3: ListSize == 3

    **Node Index(NI) test cases**
    - NI0: Node is at the beginning of the list -> NodeIndex == 0
    - NI1: Node is at the beginning of the list -> NodeIndex == 1
    - NI2: Node is at the end of the list -> NodeIndex == 2
  
    **Error(E) test cases**
    - E1: TypeError -> Type is faulty
    - E2: IndexError -> Index is faulty (index < 0)
    - E3: IndexError -> Index doesn't exsist in the List
    
    **Test matrix:**
    |      | LS0  | LS1  | LS2  | LS3  |
    |------|------|------|------|------|
    | NI0  | ○    | ○    | ○    | ○    |
    | NI1  | x    | ○    | ○    | ○    |
    | NI2  | x    | x    | ○    | ○    |
    | E1   | ○    | ×    | ×    | ×    |
    | E2   | ○    | ×    | ×    | ×    |
    | E3   | ○    | ○    | ○    | ○    |

    - ○: Test
    - ×: Don't test

    """
    def setUp(self):
        self.list = SingleList[str]()
    
    # INSERT 異常処理
    def test_insert_E1_LS0(self):
        """ INSERT TypeError & ListSize == 0
        Prerequisities: List is empty (Size == 0)
        RUN condition: Type is faulty
        Expected Result: TypeError
        """
        self.list =  list_LS1()
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.list.display()
            self.assertIn("['A']", fake_out.getvalue())
        
        with self.assertRaises(TypeError):
            self.list.insert(0, 10)

    def test_insert_E2_LS0(self):   
        """ INSERT IndexError無効 + ListSize == 0
        Prerequisities: List is empty (Size == 0)
        RUN condition: faulty index (eg: -1)
        Expected Result: IndexError
        """
        self.list =list_LS0()
        with self.assertRaises(IndexError):
            self.list.insert(-1, 'TARGET')
    
    def test_insert_E3_LS0(self):
        """ INSERT IndexError & ListSize == 0
        Prerequisities: List is empty (Size == 0)
        RUN condition: index that doesn't exsist in the List is set as a property
        Expected Result: IndexError
        """
        self.list =list_LS0()
        with self.assertRaises(IndexError):
            self.list.insert(1, 'TARGET')

    def test_insert_E3_LS1(self):
        """ INSERT IndexError & ListSize == 1
        Prerequsities: List has 1 item (Size == 1)
        RUN condition: index that doesn't exsist in the List is set as a property
        Expected Result: IndexError
        """
        self.list =list_LS1()
        with self.assertRaises(IndexError):
            self.list.insert(2, 'TARGET')

    def test_insert_E3_LS2(self):
        """ INSERT IndexError & ListSize == 2
        Prerequsities: List has 2 item (Size == 2)
        RUN condition: index that doesn't exsist in the List is set as a property
        Expected Result: IndexError
        """
        self.list =list_LS2()
        with self.assertRaises(IndexError):
            self.list.insert(3, 'TARGET')

    def test_insert_E2_LS3(self):
        """ INSERT IndexError & ListSize == 3
        Prerequsities: List has 3 items (Size == 3)
        RUN condition: index that doesn't exsist in the List is set as a property
        Expected Result: IndexError
        """
        self.list =list_LS3()
        with self.assertRaises(IndexError):
            self.list.insert(4, 'TARGET')

    # INSERT 通常処理
    def test_insert_LS0_NI0(self):
        """ INSERT ListSize == 0 & NodeIndex  == 0
        Prerequisities: List is empty (Size == 0)
        RUN condition: index is set to 0
        Expected Result: List only has 1 item
        """
        self.list =list_LS0()
        self.list.insert(0, 'TARGET')
        self.assertEqual(self.list.length(), 1)
        self.assertEqual(self.list.get(0), 'TARGET')

    def test_insert_LS1_NI0(self):
        """ INSERT ListSize == 1 & NodeIndex  == 0
        Prerequsities: List has 1 item (Size == 1)
        RUN condition: index is set to 0
        Expected Result: new node is at head of the list
        """
        self.list = list_LS0()
        self.list.insert(0, 'TARGET')
        self.assertEqual(self.list.length(), 1)
        self.assertEqual(self.list.get(0), 'TARGET')

    def test_insert_LS1_NI1(self):
        """ INSERT ListSize == 1 & NodeIndex  == 2
        Prerequsities: List has 1 item (Size == 1)
        RUN condition: Node is at index = 1 
        Expected Result: new node is at tail of the list
        """
        self.list =list_LS1()
        self.list.insert(1, 'TARGET')
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(self.list.get(1), 'TARGET')

    def test_insert_LS2_NI0(self):
        """ INSERT ListSize == 2 & NodeIndex == 0
        Prerequsities: List has 2 item (Size == 2)
        RUN condition: index is set to 0
        Expected Result: new node is at head of the list
        """
        self.list =list_LS2()
        
        self.list.insert(0, 'TARGET')
        self.assertEqual(self.list.length(), 3)
        self.assertEqual(self.list.get(0), 'TARGET')

    def test_insert_LS2_NI1(self):
        """ INSERT ListSize == 2 & NodeIndex == 1
        Prerequsities: List has 2 item (Size == 2)
        RUN condition: Node is at index = 1 
        Expected Result: Node is at the center of the list
        """
        self.list =list_LS2()
        
        self.list.insert(1, 'TARGET')
        self.assertEqual(self.list.length(), 3)
        self.assertEqual(self.list.get(1), 'TARGET')

    def test_insert_LS2_NI2(self):
        """ INSERT ListSize == 2 & NodeIndex == 2
        Prerequsities: List has 2 item (Size == 2)
        RUN condition: Node is at index = 2
        Expected Result: new node is at tail of the list
        """
        self.list =list_LS2()
        
        self.list.insert(1, 'TARGET')
        self.assertEqual(self.list.length(), 3)
        self.assertEqual(self.list.get(1), 'TARGET')

    def test_insert_LS3_NI0(self):
        """ INSERT ListSize == 3 & NodeIndex == 0
        Prerequsities: List has 3 items (Size == 3)
        RUN condition: index is set to 0
        Expected Result: new node is at head of the list
        """
        self.list =list_LS3()
        
        self.list.insert(0, 'TARGET')
        self.assertEqual(self.list.length(), 4)
        self.assertEqual(self.list.get(0), 'TARGET')

    def test_insert_LS3_NI1(self):
        """ INSERT ListSize == 3 & NodeIndex == 1
        Prerequsities: List has 3 items (Size == 3)
        RUN condition: Node is at index = 2
        Expected Result: Node is at the center of the list
        """
        self.list =list_LS3()
        
        self.list.insert(1, 'TARGET')
        self.assertEqual(self.list.length(), 4)
        self.assertEqual(self.list.get(1), 'TARGET')

    def test_insert_LS3_NI2(self):
        """INSERT ListSize == 3 & NodeIndex == 2
        Prerequsities: List has 3 items (Size == 3)
        RUN condition: Node is at index = 3
        Expected Result: new node is at tail of the list
        """
        self.list =list_LS3()
        
        self.list.insert(2, 'TARGET')
        self.assertEqual(self.list.length(), 4)
        self.assertEqual(self.list.get(2), 'TARGET')
    
    # REMOVE 異常処理
    def test_remove_E2_LS0(self):
        """REMOVE IndexError（無効なIndex） & ListSize == 0
        Prerequisities: List is empty (Size == 0)
        RUN conditions: remove node with invalid index
        Expected Result: IndexError
        """
        self.list =list_LS0()
        
        with self.assertRaises(IndexError):
            self.list.remove(-1)

    def test_remove_E3_LS0(self):
        """ REMOVE IndexError（Non exsisting Index） & ListSize == 0    
        Prerequisities: List is empty (Size == 0)
        RUN conditions: remove node with non exsisting index
        Expected Result: IndexError
        """
        self.list =list_LS0()
        
        with self.assertRaises(IndexError):
            self.list.remove(1)

    def test_remove_E3_LS1(self):
        """ REMOVE IndexError（Non exsisting Index） & ListSize == 1   
        Prerequsities: List has 1 item (Size == 1)
        RUN conditions: remove node with non exsisting index
        Expected Result: IndexError
        """
        self.list =list_LS1()
        
        with self.assertRaises(IndexError):
            self.list.remove(2)

    def test_remove_E3_LS2(self):
        """ REMOVE IndexError（Non exsisting Index） & ListSize == 2    
        Prerequsities: List has 2 item (Size == 2)
        RUN conditions: remove node with non exsisting index
        Expected Result: IndexError
        """
        self.list =list_LS2()
        
        with self.assertRaises(IndexError):
            self.list.remove(3)

    def test_remove_E3_LS3(self):
        """ REMOVE IndexError（Non exsisting Index） & ListSize == 3   
        Prerequsities: List has 3 items (Size == 3)
        RUN conditions: remove node with non exsisting index
        Expected Result: IndexError
        """
        self.list =list_LS3()
        
        with self.assertRaises(IndexError):
            self.list.remove(4)
    
    # REMOVE　通常処理
    def test_remove_LS1_NI0(self):
        """ REMOVE NodeIndex == 0 & ListSize == 1
        Prerequsities: List has 1 item (Size == 1)
        RUN conditions: remove Node at head of list
        Expected Result: list becomes empty
        """
        self.list =list_LS1()
        
        self.list.remove(0)
        self.assertEqual(self.list.length(), 0)

    def test_remove_LS2_NI0(self):
        """ REMOVE NodeIndex == 0 & ListSize == 2
        Prerequsities: List has 2 item (Size == 2)
        RUN conditions: remove Node at head of list
        Expected Result: list head is removed, the next node becomes the head
        """
        self.list =list_LS2()
        
        self.list.remove(0)
        self.assertEqual(self.list.length(), 1)
        self.assertEqual(self.list.get(0), 'B')

    def test_remove_LS2_NI1(self):
        """ REMOVE NodeIndex == 1 & ListSize == 2
        Prerequsities: List has 2 item (Size == 2)
        RUN conditions: remove index = 1 Node
        Expected result: tail of list is deleted
        """
        self.list =list_LS2()
        
        self.list.remove(1)
        self.assertEqual(self.list.length(), 1)
        self.assertEqual(self.list.get(0), 'A')

    def test_remove_LS3_NI0(self):
        """ REMOVE NodeIndex == 0 & ListSize == 3
        Prerequsities: List has 3 items (Size == 3)
        RUN conditions: remove Node at head of list
        Expected Result: list head is removed, the next node becomes the head
        """
        self.list =list_LS3()
        
        self.list.remove(0)
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(self.list.get(0), 'B')
        self.assertEqual(self.list.get(1), 'C')
        
    def test_remove_LS3_NI1(self):
        """ REMOVE NodeIndex == 1 & ListSize == 3
        Prerequsities: List has 3 items (Size == 3)
        RUN conditions: remove index = 1 Node
        Expected result: Node is deleted from middle of list, remaining nodes are connected
        """
        self.list =list_LS3()
        
        self.list.remove(1)
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(self.list.get(0), 'A')
        self.assertEqual(self.list.get(1), 'C')

    def test_remove_LS3_NI2(self):
        """ REMOVE NodeIndex == 2 & ListSize == 3
        Prerequsities: List has 3 items (Size == 3)
        RUN conditions: index = 2 node is deleted
        Expected result: tail of list is deleted
        """
        self.list =list_LS3()
        
        self.list.remove(2)
        self.assertEqual(self.list.length(), 2)
        self.assertEqual(self.list.get(0), 'A')
        self.assertEqual(self.list.get(1), 'B')

    # LENGTH 通常処理 
    def test_length_LS0(self):
        """ LENGTH ListSize == 0
        Prerequisities: List is empty (Size == 0)
        RUN conditions: take size of list
        Expected Result: List has size of０
        """
        self.list =list_LS0()
        
        self.assertEqual(self.list.length(), 0)
    
    def test_length_LS1(self):
        """ LENGTH ListSize == 1
        Prerequsities: List has 1 item (Size == 1)
        RUN conditions: take size of list
        Expected Result: List has size of1
        """
        self.list =list_LS1()

        self.assertEqual(self.list.length(), 1)

    def test_length_LS2(self):
        """ LENGTH ListSize == 2
        Prerequsities: List has 2 item (Size == 2)
        RUN conditions: take size of list
        Expected Result: List has size of3
        """
        self.list =list_LS2()

        self.assertEqual(self.list.length(), 2)

    def test_length_LS3(self):
        """ LENGTH ListSize == 3
        Prerequsities: List has 3 items (Size == 3)
        RUN conditions: take size of list
        Expected Result: List has size of3
        """
        self.list =list_LS3()

        self.assertEqual(self.list.length(), 3)

    # GET 異常処理
    def test_get_E1_LS0(self):
        """ LENGTH TypeError & ListSize == 0
        Prerequisities: List is empty (Size == 0)
        RUN conditions: get with invalid type
        Expected Result: TypeError
        """
        self.list =list_LS0()
        
        with self.assertRaises(TypeError):
            self.list.get("invalid_type")

    def test_get_E2_LS0(self):
        """ LENGTH IndexError（無効なIndex） & ListSize == 0
        Prerequisities: List is empty (Size == 0)
        RUN conditions: set invalid index
        Expected Result: IndexError
        """
        self.list =list_LS0()
        
        with self.assertRaises(IndexError):
            self.list.get(-1)

    def test_get_E3_LS0(self):
        """ LENGTH IndexError（Non exsisting Index） & ListSize == 0
        Prerequisities: List is empty (Size == 0)
        RUN conditions: set non exsisting index
        Expected Result: IndexError
        """
        self.list =list_LS0()
        
        with self.assertRaises(IndexError):
            self.list.get(1)

    def test_get_E3_LS1(self):
        """ LENGTH IndexError（Non exsisting Index） & ListSize == 1
        Prerequsities: List has 1 item (Size == 1)
        RUN conditions: set non exsisting index
        Expected Result: IndexError
        """
        self.list =list_LS1()
        
        with self.assertRaises(IndexError):
            self.list.get(2)

    def test_get_E3_LS2(self):
        """ LENGTH IndexError（Non exsisting Index） & ListSize == 2
        Prerequsities: List has 2 item (Size == 2)
        RUN conditions: set non exsisting index
        Expected Result: IndexError
        """
        self.list =list_LS2()
        
        with self.assertRaises(IndexError):
            self.list.get(3)

    def test_get_E3_LS3(self):
        """ LENGTH IndexError（Non exsisting Index） & ListSize == 3
        Prerequsities: List has 3 items (Size == 3)
        RUN conditions: set non exsisting index
        Expected Result: IndexError
        """
        self.list =list_LS3()
        
        with self.assertRaises(IndexError):
            self.list.get(4)
    
    #  GET 通常処理
    def test_get_LS1_NI0(self):
        """ GET NodeIndex == 0 & ListSize == 0
        Prerequsities: List has 1 item (Size == 1)
        RUN conditions: get Node with index == 0
        Expected Result: Head of list will be returned
        """
        self.list =list_LS1()
        
        self.assertEqual(self.list.get(0), 'A')

    def test_get_LS2_NI0(self):
        """ GET NodeIndex == 0 & ListSize == 2
        Prerequsities: List has 2 item (Size == 2)
        RUN conditions: get Node with index == 0
        Expected Result: Head of list will be returned
        """
        self.list =list_LS2()
        
        self.assertEqual(self.list.get(0), 'A')

    def test_get_LS2_NI1(self):
        """ GET NodeIndex == 1 & ListSize == 2
        Prerequsities: List has 2 item (Size == 2)
        RUN conditions: get Node with index == 1
        Expected Result: Tail of list will be returned
        """
        self.list =list_LS2()
        
        self.list.insert(0, 'A')
        self.list.insert(1, 'B')
        self.assertEqual(self.list.get(1), 'B')

    def test_get_LS3_NI0(self):
        """ GET NodeIndex == 0 & ListSize == 3
        Prerequsities: List has 3 items (Size == 3)
        RUN conditions: get Node with index == 0
        Expected Result: Head of list will be returned
        """
        self.list =list_LS3()
        
        self.assertEqual(self.list.get(0), 'A')

    def test_get_LS3_NI1(self):
        """ GET NodeIndex == 1 & ListSize == 3
        Prerequsities: List has 3 items (Size == 3)
        RUN conditions: get Node with index == 1
        Expected Result: Middle of list will be returned
        """
        self.list =list_LS3()
        
        self.assertEqual(self.list.get(1), 'B')

    def test_get_LS3_NI2(self):
        """ GET NodeIndex == 2 & ListSize == 3
        Prerequsities: List has 3 items (Size == 3)
        RUN conditions: return Node with index == 2 
        Expected Result: Tail of list will be returned
        """
        self.list =list_LS3()
        
        self.assertEqual(self.list.get(2), 'C')

    #  CLEAR 通常
    def test_clear_LS0(self):
        """ CLEAR ListSize == 0
        Prerequisities: List is empty (Size == 0)
        RUN conditions: clear the list
        Expected Result: list becomes empty
        """
        self.list =list_LS0()
        
        self.list.clear()
        self.assertEqual(self.list.length(), 0)

    def test_clear_LS1(self):
        """ CLEAR ListSize == 1
        Prerequsities: List has 1 item (Size == 1)
        RUN conditions: clear the list
        Expected Result: list becomes empty
        """
        self.list =list_LS1()
        
        self.list.clear()
        self.assertEqual(self.list.length(), 0)

    def test_clear_LS2(self):
        """ CLEAR ListSize == 2
        Prerequsities: List has 2 item (Size == 2)
        RUN conditions: clear the list
        Expected Result: list becomes empty
        """
        self.list =list_LS2()
        
        self.list.clear()
        self.assertEqual(self.list.length(), 0)

    def test_clear_LS3(self):
        """ CLEAR ListSize == 3
        Prerequsities: List has 3 items (Size == 3)
        RUN conditions: clear the list
        Expected Result: list becomes empty
        """
        self.list =list_LS3()
        
        self.list.clear()
        self.assertEqual(self.list.length(), 0)

    # DISPLAY 通常
    def test_display_LS0(self):
        """ DISPLAY ListSize == 0
        Prerequisities: List is empty (Size == 0)
        RUN conditions: display the list
        Expected Result: values will be correctly displayed
        """
        self.list =list_LS0()
        
        expected_output = "[]"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.list.display()
            self.assertIn(expected_output, fake_out.getvalue())

    def test_display_LS1(self):
        """ DISPLAY ListSize == 1
        Prerequsities: List has 1 item (Size == 1)
        RUN conditions: display the list
        Expected Result: values will be correctly displayed
        """
        self.list =list_LS1()
        
        expected_output = "['A']"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.list.display()
            self.assertIn(expected_output, fake_out.getvalue())

    def test_display_LS2(self):
        """ DISPLAY ListSize == 2
        Prerequsities: List has 2 item (Size == 2)
        RUN conditions: display the list
        Expected Result: values will be correctly displayed
        """
        self.list =list_LS2()

        expected_output = "['A', 'B']"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.list.display()
            self.assertIn(expected_output, fake_out.getvalue())
            
    def test_display_LS3(self):
        """ DISPLAY ListSize == 3
        Prerequsities: List has 3 items (Size == 3)
        RUN conditions: display the list
        Expected Result: values will be correctly displayed
        """
        self.list = list_LS3()

        expected_output = "['A', 'B', 'C']"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.list.display()
            self.assertIn(expected_output, fake_out.getvalue())
