def BinarySearchIterative(arr, value):
    left : int = 0
    right : int = len(arr) - 1
    #print(mid)

    while left <= right:
        mid: int = (left + right) // 2
        if value == arr[mid]:
            print("The value is found at {}".format(mid))
            return True

        elif value < arr[mid]:
            right = mid - 1

        elif value > arr[mid]:
            left = mid + 1

    return False


def BinarySearchRecursive(arr, value, left : int, right : int):

    if left > right:
        return False
    mid: int = (left + right) // 2
    if value == arr[mid]:
        print("The value is found at {}".format(mid))
        return True
    elif value < arr[mid]:
        return BinarySearchRecursive(arr, value, left, mid - 1)
    elif value > arr[mid]:
        return BinarySearchRecursive(arr, value, mid + 1, right)

def BinarySearchIterative2(arr, value, left, right):

    while left <= right:
        mid: int = (left + right) // 2
        if value == arr[mid]:
            return mid

        elif value < arr[mid]:
            right = mid - 1

        elif value > arr[mid]:
            left = mid + 1

    return -1 #if not found

def main():
    arr = [1,2,6,8,14]
    BinarySearchIterative(arr, 8)
    BinarySearchRecursive(arr, 2, 0, len(arr) - 1)
    BinarySearchIterative(arr, 14)
    print(BinarySearchRecursive(arr, 13, 0, len(arr)-1))
    print(BinarySearchRecursive(arr, 14, 0, len(arr) - 1))
    print(BinarySearchIterative(arr, 14) == BinarySearchRecursive(arr, 14, 0, len(arr) - 1))
    index = BinarySearchIterative2(arr, 8, 0, len(arr) - 1)
    print(index)

if __name__ == '__main__':
    main()