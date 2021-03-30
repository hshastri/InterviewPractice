def Fib(n):
    if n < 2:
        return n
    else:
        return Fib(n - 1) + Fib (n - 2)

def FibBottomUp(n):
    memo = [0, 1]
    for i in range(1, n):
        memo.append(memo[i] + memo[i - 1])
    # print(memo)
    return memo[n]

def FibMemo(n):
    memo = [None for i in range(n + 1)]
    # memo => 0....n
    return FibMemoRecur(n, memo)

def FibMemoRecur(n, memo):
    if n < 2:
        # memo[n] = n => this line works as well. Don't return n if you do this since this func returns memo[n] later anyways and memo[n] = memo[n - 1] + memo[n - 2]
        return n
    elif memo[n] != None:
        return memo[n]
    else:
        memo[n] = FibMemoRecur(n - 1, memo) + FibMemoRecur(n - 2, memo)
    # print(memo)
    return memo[n]