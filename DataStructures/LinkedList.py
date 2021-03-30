from DataStructures.Node import *

class LinkedList:

    def __init__(self, data):
        self.head: Node = Node(data)

    def append(self, data):
        node: Node = Node(data)
        if (self.head == None):
            self.head = node
            return
        current: Node = self.head
        while (current.next != None):
            current = current.next
        current.next = node

    def prepend(self, data):
        newHead = Node(data)
        newHead.next = self.head
        self.head = newHead

    def remove(self, data):
        if self.head == None:
            print("The linked list is empty")
            return
        if self.head.data == data:
            """if self.head.next == None:
                self.head = None
                return
            else:"""
            # no need to check the stuff above because of self.head.next is none, and self.head will be set to that
            self.head = self.head.next
            return

        current = self.head

        while (current.next != None):
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def printLinkedList(self):
        arrOfNodes = []
        current: Node = self.head
        arrOfNodes.append(str(current))
        if (current == None):
            print(arrOfNodes)
            return
        while (current.next != None):
            current = current.next
            arrOfNodes.append(str(current))
        print(arrOfNodes)
