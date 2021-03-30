from DataStructures.Node import *

class MyQueue:

    def __init__(self):
        self.head : Node = None
        self.tail: Node = None

    def isEmpty(self):
        return self.head == None

    def peek(self):
        if self.head == None:
            return
        data = self.head.data
        return data

    # adding to the tail
    def add(self, data):
        node = Node(data)
        # if the tail is not None add a node right next to it and update the tail (line 21-23)
        if (self.tail != None):
            self.tail.next = node
        self.tail = node

        if (self.head == None):
            self.head = node

        """ when the head is None (when the queue is empty) and a node is added to the queue,
        the head and tail point to the same node. The head pointer will be pointing to the first node added
        to the queue. The tail pointer will move to the next node being added.  HT (Head and Tail ppinting to the same node)
        => H-T => H-N-N-..-N-T (H: head, T: tail and N: nodes in between). We are removing from the head and adding to the tail
        """

    def remove(self):
        if self.head == None:
            #self.tail = None -->not needed
            return
        data = self.head.data
        self.head = self.head.next
        return data

    def printQueue(self):
        arrOfNodes = []
        current = self.head
        arrOfNodes.append(str(current))
        if current == None:
            print(arrOfNodes)
            return
        while (current.next != None):
            current = current.next
            arrOfNodes.append(str(current))
        print(arrOfNodes)

