def MakeChange(arr, amount):
    ways = [[-1 for j in range(0, amount + 1)] for i in range(0, len(arr) + 1)]

    for i in range(0, len(arr) + 1):
        ways[i][0] = 1 # one way to make 0 out of any collection

    for row in range(0, len(arr) + 1):
        for col in range(0, amount + 1):
            if row == 0 and col != 0:
                ways[row][col] = 0
            elif col - arr[row - 1] >= 0:
                ways[row][col] = ways[row - 1][col] + ways[row][col - arr[row - 1]]
            else:
                ways[row][col] = ways[row - 1][col]

    # print(ways)
    return ways[len(arr)][amount]