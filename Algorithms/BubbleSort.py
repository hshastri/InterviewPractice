def BubbleSort(arr):
    isSorted = False
    while(isSorted != True):
        isSorted = True
        lastUnsorted = len(arr) - 1
        for i in range(0,lastUnsorted): # last iteration is i = len(arr) - 2
            if arr[i] > arr[i + 1]:
                swap(arr, i, i + 1)
                isSorted = False
        lastUnsorted -= 1

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp