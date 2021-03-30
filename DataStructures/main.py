from Node import *
from LinkedList import *
from Stack import *
from MyQueue import *
from Heap import *
from BinarySearch import *

class Test:
    classVar = 23

    def __init__(self):
        self.a = "test1"
        self.b = "test2"

    @classmethod
    def testMethod(cls, num):
        cls.classVar = num
        print(cls.classVar)

def main():
    testArr = ['a', 'b', 'c', 'd']

    print("NODE")
    package1: Node = Node(1)
    print(str(package1))
    package2: Node = Node(2)
    package1.next = package2
    print(str(package1))
    print(repr(package2))
    package2.next = Node(3)
    print(str(package2))
    print()

    print("LINKED LIST")
    linkedList :LinkedList = LinkedList('A')
    linkedList.printLinkedList()
    linkedList.append('B')
    linkedList.append('C')
    linkedList.printLinkedList()
    linkedList.prepend('Alpha')
    linkedList.printLinkedList()

    linkedList.remove('B')
    linkedList.printLinkedList()
    linkedList.remove('C')
    linkedList.printLinkedList()
    linkedList.remove('Alpha')
    linkedList.printLinkedList()
    linkedList.remove('A')
    linkedList.printLinkedList()
    linkedList.remove('A')
    testArr = ['a', 'b', 'c', 'd']
    for i in testArr:
        linkedList.append(i)
    linkedList.printLinkedList()
    print()

    print("STACK")
    stackOfEmails: Stack = Stack('A')
    #stackOfEmails.pop()
    #print(stackOfEmails.isEmpty())
    #stackOfEmails.printStack()
    for i in testArr:
        stackOfEmails.push(i)
    stackOfEmails.printStack()
    #print(stackOfEmails.isEmpty())
    while(stackOfEmails.isEmpty() == False):
        print("The Node with the data '{}' will be deleted".format(stackOfEmails.peek()))
        stackOfEmails.pop()
        stackOfEmails.printStack()
    print(stackOfEmails.isEmpty())
    stackOfEmails.push('Z')
    stackOfEmails.printStack()
    print()

    print("QUEUE")
    myQueue : MyQueue = MyQueue()
    print(myQueue.isEmpty())
    for i in testArr:
        myQueue.add(i)
    myQueue.printQueue()
    while(myQueue.isEmpty()==False):
        print("The node with the data '{}' will be removed".format(myQueue.remove()))
        myQueue.printQueue()
    print(myQueue.isEmpty())
    myQueue.remove()
    print()

    print("HEAP")
    testArr2 = [17, 10, 20, 15, 25]
    myHeap : Heap = Heap()
    for i in testArr2:
        myHeap.add(i)
    myHeap.printHeap()
    myHeap.poll()
    myHeap.printHeap()
    print()

    print("BINARY SEARCH TREE")
    testArr3 = [8, 15, 5]
    binaryTree : BinarySearch = BinarySearch(10)
    #binaryTree.printInOrder()
    for i in testArr3:
        binaryTree.insert(i)
    binaryTree.printInOrder()
    print(binaryTree.find(10))
    for i in testArr3:
        print(binaryTree.find(i))
    print(binaryTree.find(100))
    print()

    print("TEST")
    test1 = Test()
    test2 = Test()
    print(Test.__dict__)
    print(test1.__dict__)
    test1.classVar = 34
    print(Test.__dict__)
    print(test1.__dict__)
    print(test2.__dict__)
    print(test2.classVar)
    print()

if __name__ == '__main__':
    main()
