from DataStructures.Stack import *


def dfs(graph, startingNode):
    stack: Stack = Stack(startingNode)
    seen: set = set()

    while not stack.isEmpty():
        current = stack.pop()
        if current not in seen:
            seen.add(current)
            print(current)

        for neighbor in graph[current]:
            if neighbor not in seen:
                stack.push(neighbor)