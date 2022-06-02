class Node:
    def __init__(self, data):  # Constructor
        self.data = data
        self.next = None #Address of next element

class LinkedList:
    def __init__(self):   # Constructor
        self.head = None

    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next

    def insert_at_specific(self, value, pos):
        if pos >= 2:
            np = Node(value)
            temp = self.head
            for i in range(0, pos-1):
                temp = temp.next
            np.next = temp.next
            temp.next = np
        else:
            print("Enter position greater than or equal to 2 for inserting element in specific position")
    
    def insert_at_begin(self, value):
        np = Node(value)
        np.next = self.head
        self.head = np

    def insert_at_end(self, value):
        ne = Node(value)
        temp = self.head
        while temp.next is not None:  # temp goes till the LAST node
            temp = temp.next
        temp.next = ne
    
    def delete_at_begin(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
    
    def delete_at_end(self):
        temp = self.head
        while temp.next.next is not None:  # temp goes till the SECOND LAST node
            temp = temp.next
        temp.next = None
    
    def delete_at_specific(self, pos):
        if pos >= 2:
            fast = self.head.next
            slow = self.head
            for i in range(1, pos-1):
                slow = slow.next
                fast = fast.next
            # for i in range(1, pos):
            #     fast = fast.next
            slow.next = fast.next
            fast.next = None
        else:
            print("Enter position greater than or equal to 2 for deleting element in specific position")
    


l = LinkedList()
n1 = Node(10)   #create node with value 10 and next NULLx
l.head = n1     #pointing head pointer to node1 i.e 10
n2 = Node(20)   #create node with value 20 and next NULL
n1.next = n2    #pointing n1.next to n2 for linking n1 and n2
n3 = Node(30)
n2.next = n3
n4 = Node(40)
n3.next = n4
l.insert_at_specific(50, 3)
l.insert_at_begin(5)
l.insert_at_end(65)
l.delete_at_begin()
l.delete_at_end()
l.delete_at_specific(2)
l.display()


'''
class LinkedList

-> head (pointer)

Class Node

|---|---|
| d | n |
|---|---|

'''

# Double LinkedList Implementation is similar, create prev and next pointer in class
# Then few logic changes - understandable