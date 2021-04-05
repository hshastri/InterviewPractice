from DataStructures.MyQueue import *

def bfs(graph, startingNodeData):
    myQueue: MyQueue = MyQueue()
    seen: set = set()

    myQueue.add(startingNodeData)

    while not myQueue.isEmpty():
        current = myQueue.remove()

        if current not in seen:
            seen.add(current)
            print(current)

        for neighbor in graph[current]:
            if neighbor not in seen:
                myQueue.add(neighbor)