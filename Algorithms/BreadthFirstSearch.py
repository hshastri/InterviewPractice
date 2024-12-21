from Node import *
from MyQueue import *

def BreadthFirstSearch(graph, startingNodeData):
    searchQueue : MyQueue = MyQueue()
    seen : set = set([])

    searchQueue.add(startingNodeData)

    while searchQueue.isEmpty() == False:
        currentNodeData = searchQueue.remove()

        if currentNodeData not in seen:
            seen.add(currentNodeData)
            print(currentNodeData)

        for neighbor in graph[currentNodeData]:
            if neighbor not in seen:
                searchQueue.add(neighbor)


def main():
    graph = {
        'A': ['B', 'C', 'D', 'E'],
        'B': ['A', 'C', 'G'],
        'C': ['A', 'B', 'D'],
        'D': ['A', 'C', 'E', 'H'],
        'E': ['A', 'D', 'F'],
        'F': ['E', 'G', 'H'],
        'G': ['B', 'F'],
        'H': ['D', 'F']
    }

    BreadthFirstSearch(graph, 'A')

if __name__ == '__main__':
    main()
