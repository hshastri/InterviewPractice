def QuickSort(arr):
    return QuickSortHelper(arr, 0, len(arr) - 1)


def QuickSortHelper(arr, left, right):
    if left >= right:
        return
    pivot = (left + right) // 2
    index = partition(arr, left, right, pivot)
    QuickSortHelper(arr, left, index - 1)
    # print(arr[left:index])
    QuickSortHelper(arr, index, right)
    # print(arr[index: right + 1])

    """if left < right:
        pivot = (left + right) // 2
        index = partition(arr, left, right, pivot)
        QuickSortHelper(arr, left, index - 1)
        # print(arr[left:index])
        QuickSortHelper(arr, index, right)
        # print(arr[index: right + 1])"""


def partition(arr, left, right, pivot):
    while left <= right:
        while arr[left] < arr[pivot]:
            left += 1
        while arr[right] > arr[pivot]:
            right -= 1
        if left <= right:
            swap(arr, left, right)
            left += 1
            right -= 1
    return left


def swap(arr, i: int, j: int):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
