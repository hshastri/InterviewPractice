
def BinarySearchIterative(arr, value):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == value:
            print("This value is found at: {}".format(mid))
            return True
        elif value < arr[mid]:
            right = mid - 1
        elif value > arr[mid]:
            left = mid + 1
    return False

def BinarySearchRecursive(arr, value, left, right):
    if left > right:
        return False
    mid = (left + right) // 2
    if arr[mid] == value:
        print("This value is found at: {}".format(mid))
        return True
    elif value < arr[mid]:
        return BinarySearchRecursive(arr, value, left, mid - 1)
    elif value > arr[mid]:
        return BinarySearchRecursive(arr, value, mid + 1, right)