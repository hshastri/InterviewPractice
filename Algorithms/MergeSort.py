def MergeSort(arr):
    # consider a sub array: [1,3,4] which is divided into [1], [3,4]. You can't perform merge sort on [1] since you
    # can't split [1] in two subarrays so len(arr) must be greater than 1
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]  # this splitting causes extra space to be created in the memory
        right = arr[mid:]

        MergeSort(left)
        # print(left)
        MergeSort(right)
        # print(right)

        i = j = k = 0
        # i for the left sub array which is sorted, j for the right and k for the original array to be modified

        while (i < len(left) and j < len(right)):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1

            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # fill the rest of the elements from either of the two sorted arrays
        # trace this on a piece of paper and you'll see only one of these while loops will run
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
