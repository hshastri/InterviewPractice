from Algorithms.BinarySearch import *

def IceCreamParlor(arr, money):

    tempArr = [i for i in arr]
    tempArr.sort()
    indices = []
    for i in range(0, len(tempArr)):
        complement = money - tempArr[i]
        complementExists = BinarySearchRecursive(tempArr, complement, i + 1, len(tempArr) - 1)
        if complementExists:
            complementIndex = tempArr.index(complement)
            indexA = arr.index(tempArr[i])
            indexB = arr.index(tempArr[complementIndex])
            # indices.append((i, complementIndex))
            indices.append((indexA, indexB))
    return indices
