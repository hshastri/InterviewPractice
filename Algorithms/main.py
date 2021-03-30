from DataStructures.Node import *
from BubbleSort import *
from MergeSort import *
from QuickSort import *
from BinarySearch import *
from DepthFirstSearch import *
from BreadthFirstSearch import *

def main():
    print("TEST")
    node: Node = Node('A')
    node.next = Node('B')
    print(str(node))
    print()

    print("BUBBLE SORT")
    arr = [10, 3, 5, 12, 20, 9]
    BubbleSort(arr)
    print(arr)
    print()

    print("MERGE SORT")
    arr2 = [45, 12, 99, 69, 1, 13]
    MergeSort(arr2)
    print(arr2)
    print()

    print("QUICK SORT")
    arr3 = [45, 12, 99, 69, 1, 13]
    QuickSort(arr3)
    print(arr3)
    print()

    print("BINARY SEARCH")
    arr4 = [1,2,6,8,14]
    #print(BinarySearchRecursive(arr4, 2, 0, len(arr) - 1))
    print(BinarySearchIterative(arr4, 8))
    print(BinarySearchRecursive(arr4, 2, 0, len(arr4) - 1))
    print()

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

    # put neighbors in a reverse order for now
    graph2 = {
        'A': ['E', 'D', 'C', 'B'],
        'B': ['G', 'C', 'A'],
        'C': ['D', 'B', 'A'],
        'D': ['H', 'E', 'C', 'A'],
        'E': ['F', 'D', 'A'],
        'F': ['H', 'G', 'E'],
        'G': ['F', 'B'],
        'H': ['F', 'D']
    }

    print("BREADTH FIRST SEARCH")
    bfs(graph, 'A')
    print()

    print("DEPTH FIRST SEARCH")
    dfs(graph2, 'A')
    print()

if __name__ == '__main__':
    main()