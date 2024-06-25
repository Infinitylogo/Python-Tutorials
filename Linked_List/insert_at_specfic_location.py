# inserting node at any location 

# Time com is O(N) for inserting at any location


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedll:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def _append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1

    def _append_at_beg(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
    
    def insert_at_any_loc(self, index, data):
        new_node = Node(data)
        if index <0 or self.length < index:
            return False
        elif self.head is None: # another cond -- self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index ==0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next  # reach where we need to make the changes
            new_node.next = temp_node.next # now new_node ref to temp_node next
            temp_node.next = new_node # and temp node next linked to new node 
        self.length+=1
        return True

    def __str__(self):
        curr_node = self.head
        res=""
        while curr_node:
            res+=str(curr_node.data)
            if curr_node.next is not None:
                res+=" -> "
            curr_node = curr_node.next
        return res
    
ll = Linkedll()
ll.insert_at_any_loc(0, 50)
ll._append(1)
ll._append(2)
ll._append(3)
ll._append(4)
ll._append_at_beg(5)
ll._append_at_beg(6)
ll._append_at_beg(7)
ll.insert_at_any_loc(3, 50)
ll.insert_at_any_loc(7, 51)
ll.insert_at_any_loc(0, 52)
ll.insert_at_any_loc(0, 54)
print(ll.length)
print(ll)



    