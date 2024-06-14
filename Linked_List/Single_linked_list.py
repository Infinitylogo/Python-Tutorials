# Single list creation
# time complexity O(1) and SC -- O(1)
class Node:
    def __init__(self, Value =None):
        self.Value  = Value
        self.next = None 


class Sing_linked_list:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def print_list(self):
        cr_node = self.head
        while(cr_node):
            print(cr_node.Value)
            cr_node = cr_node.next

class Linked_list: 
    def __init__(self, value):
        new_node = Node(value)  # O(1)
        self.head  = new_node # O(1)
        self.tail =  new_node # O(1)
        self.length = 1 # O(1)

sll = Sing_linked_list()
node1= Node(1)
node2 = Node(2)

sll.head = node1
sll.head.next = node2
sll.tail = node2

sll.print_list()