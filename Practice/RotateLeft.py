def rotLeft(a, d):
    newArr = []
    startIndex = d
    currentIndex = d
    while(currentIndex < len(a)):
        newArr.append(a[currentIndex])
        currentIndex += 1
    for i in range(0, startIndex):
        newArr.append(a[i])
    return newArr

    """count = 0
    while(count < d):
        shiftRight(a)
        count += 1
        print(a)
    return a

def shiftRight(a):
    firstElement = a[0]
    for i in range(0, len(a) - 1):
        a[i] = a[i + 1]
    a[len(a) - 1] = firstElement

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp"""