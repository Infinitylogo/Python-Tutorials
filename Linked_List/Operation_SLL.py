# Adding at first position, middle and last node of single linked list

"""
Will know about insertion operation in linked lists
"""

class Node:
    def __init__(self, data) -> None:
        self.data = data # O(1)
        self.next = None # O(1)

    # insert at first node

# class Linked_list: 
#     def __init__(self, value):
#         new_node = Node(value)  # O(1)
#         self.head  = new_node # O(1)
#         self.tail =  new_node # O(1)
#         self.length = 1 # O(1)


class linked_list:
    def __init__(self) -> None: # O(1)
        self.head = None # O(1)
        self.tail = None # O(1)
        self.length =0 # O(1)
    
    def append(self, value):
        new_node = Node(value) # O(1)
        if self.head is None: # O(1) 
            self.head = new_node # O(1)
            self.tail = new_node # O(1)

        else:
            self.tail.next = new_node # O(1)
            self.tail = new_node # O(1)

        self.length+=1 # O(1)

    def __str__(self) -> str: # string 
        current_node = self.head
        res =''
        while (current_node):
            res+=str(current_node.data)
            if current_node.next is not None:
                res+=" -> "
            current_node = current_node.next
        return res

sll1 = linked_list()
sll1.append(1)
sll1.append(2)
sll1.append(3)
print(sll1.length, sll1.head.data)# appending at last and first # O(1)
print(sll1)