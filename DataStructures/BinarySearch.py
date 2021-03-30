class BinarySearch:

    def __init__(self, data):
        self.root = data
        self.left: BinarySearch = None
        self.right: BinarySearch = None

    def insert(self, data):
        binarySearchNode: BinarySearch = BinarySearch(data)
        if self.root > data:
            if self.left == None:
                self.left = binarySearchNode
            else:
                self.left.insert(data)
        elif self.root < data:
            if self.right == None:
                self.right = binarySearchNode
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


