class BinarySearchNode:

    def __init__(self, data):
        self.root = data
        self.left: BinarySearchNode = None
        self.right: BinarySearchNode = None

    def insert(self, data):
        BinarySearchNodeNode: BinarySearchNode = BinarySearchNode(data)
        if self.root > data:
            if self.left == None:
                self.left = BinarySearchNodeNode
            else:
                self.left.insert(data)
        elif self.root < data:
            if self.right == None:
                self.right = BinarySearchNodeNode
            else:
                self.right.insert(data)

    def find(self, data):
        if self.root == data:
            return True

        if self.root > data:
            if self.left == None:
                return False
            else:
                return self.left.find(data)
        elif self.root < data:
            if self.right == None:
                return False
            else:
                return self.right.find(data)

    def printInOrder(self):
        if self.left != None:
            self.left.printInOrder()
        print(self.root)
        if self.right != None:
            self.right.printInOrder()


