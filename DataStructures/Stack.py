from DataStructures.Node import *

class Stack:

    def __init__(self, data):
        self.top = Node(data)

    def push(self, data):
        node = Node(data)
        if self.isEmpty():
            self.top = node
            return
        node.next = self.top
        self.top = node

    def isEmpty(self):
        return self.top == None

    def peek(self):
        if self.top == None:
            return
        return self.top.data

    def pop(self):
        if self.top == None:
            return
        data = self.top.data
        self.top = self.top.next
        return data

    def printStack(self):
        arrOfNodes = []
        current = self.top
        arrOfNodes.append(str(current))
        if current == None:
            print(arrOfNodes)
            return None
        while(current.next != None):
            current = current.next
            arrOfNodes.append(str(current))
        print(arrOfNodes)