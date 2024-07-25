"""
Intro To Linked List
A linked list is a linear data structure where elements are not stored in contiguous memory locations. Instead, each element (called a node) contains data and a reference (or link) to the next node in the sequence.
"""


class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
    


# Create Node
a = Node(1)
b = Node(2)
c = Node(3)

print(a.data)

a.next = b
b.next = c
print(a)


class LinkedList:
    def __int__(self):
        self.head = None
        self.n = 0
        
    def __len__(self):
        return self.n



        