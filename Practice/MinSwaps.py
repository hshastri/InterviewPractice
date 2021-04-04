def minimumSwaps(arr):
    swaps = 0
    for i in range(0, len(arr) - 1):
        while(i + 1 != arr[i]):
            swapIndex = arr[i] - 1  # index where the arr[i] should be at
            valAtIndex = arr[i]
            valAtSwapIndex = arr[swapIndex]
            arr[i] = valAtSwapIndex
            arr[swapIndex] = valAtIndex
            swaps += 1
            # print(arr)
    return swaps

