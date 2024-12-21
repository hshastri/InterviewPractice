from Node import *
from Stack import *

def DepthFirstSearch(graph, startingNodeData):
    searchStack : Stack = Stack()
    seen : set = set([]) #visited elements

    searchStack.push(startingNodeData)

    while searchStack.isEmpty() == False:
        currentNodeData = searchStack.pop()

        if currentNodeData not in seen:
            seen.add(currentNodeData)
            print(currentNodeData)

        for neighbor in graph[currentNodeData]:
            if neighbor not in seen:
                searchStack.push(neighbor)

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

    #put neighbors in a reverse order for now
    graph2 = {
        'A' : ['E', 'D', 'C', 'B'],
        'B' : ['G', 'C', 'A'],
        'C' : ['D', 'B', 'A'],
        'D' : ['H', 'E', 'C', 'A'],
        'E' : ['F', 'D', 'A'],
        'F' : ['H', 'G', 'E'],
        'G' : ['F', 'B'],
        'H' : ['F', 'D']
    }
    DepthFirstSearch(graph2, 'A')

if __name__ == '__main__':
	main()