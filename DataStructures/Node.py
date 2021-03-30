class Node:
    def __init__(self, data):
        self.data = data
        self.next : Node = None

    def __str__(self):
        if self.next == None:
            return "Current Node data: {} and the next Node is: None".format(self.data)
        else:
            return "Current Node data: {} and the next Node is: {}".format(self.data, self.next.data)

    def __repr__(self):
        return "Node({})".format(self.data)
