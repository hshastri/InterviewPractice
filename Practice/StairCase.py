def countPaths(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        return countPaths(n - 1) + countPaths(n - 2) + countPaths(n - 3)

def countStairsBottomUp(n):
    paths = [1, 1, 2]
    for i in range(3, n + 1):
        paths.append(paths[i - 1] + paths[i - 2] + paths[i - 3])
    # print(paths)
    return paths[n]

def countPathSpaceOptimized(n):
    paths = [1, 1, 2]

    for i in range(3, n + 1):
        ways = paths[2] + paths[1] + paths[0]
        paths[0] = paths[1]
        paths[1] = paths[2]
        paths[2] = ways
    return ways

def countPathsMemo(n):
    memo = [None for i in range(n + 1)]
    return countPathMemoHelper(n, memo)

def countPathMemoHelper(n, memo):
    if n < 0:
        return 0
    if n == 0:
        return 1
    elif memo[n] != None:
        return memo[n]
    else:
        memo[n] = countPathMemoHelper(n - 1, memo) + countPathMemoHelper(n - 2, memo) + countPathMemoHelper(n - 3, memo)
    return memo[n]
