# insert at the begining of the linked list
# meaning of creating a node is 

# Time complxity for adding node at the begining is O(1)
"""
______
|     | 
| Data|   ------------- > None 
-------
This is a Node
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def _append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head  = new_node
            self.tail  = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1

    def add_at_begining(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1

    def __str__(self):
        current_node = self.head
        res = ""
        while current_node:
            res+=str(current_node.data)
            if current_node.next is not None:
                res+=" -> " 
            current_node = current_node.next
        return res
        
ll = linked_list()
ll._append(1)
ll._append(2)
ll._append(3)
ll._append(4)
ll.add_at_begining(5)
ll.add_at_begining(6)
ll.add_at_begining(7)

print(ll.length)
print(ll)


