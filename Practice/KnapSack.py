import math

def KnapSack(knapSack : dict, weight : int):
    weights = list(knapSack.keys())
    print(weights)
    values = list(knapSack.values())
    print(values)
    table = [[None for col in range(0, weight + 1)] for rows in range(0, len(weights))]

    for row in range(len(weights)):
        for col in range(weight + 1):
            if row == 0:
                if weights[row] > col:
                    table[row][col] = 0
                elif weights[row] <= col:
                    table[row][col] = values[row]
            elif weights[row] > col:
                table[row][col] = table[row - 1][col]
            elif col >= weights[row]:
                table[row][col] = max(table[row - 1][col], table[row - 1][col - weights[row]] + values[row])
    print(table)
    return table[len(weights) - 1][weight]
