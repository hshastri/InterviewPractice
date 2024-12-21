def QuickSort(arr):
	return QuickSortHelper(arr, 0, len(arr) - 1)

def QuickSortHelper(arr, left, right):
	if (left >= right):
		print(f" BASE CASE: left: {left}, right: {right}")
		return
	pivot : int = (left + right ) // 2
	print(f"pivot: {pivot}")
	index : int = partition(arr, left, right, pivot)
	print(f"index: {arr[index]}")
	print("Recursive call stack ")
	print(f"left: {arr[left: index]}")
	print(f"right: {arr[index: right + 1]}")
	print()
	QuickSortHelper(arr, left, index - 1)
	QuickSortHelper(arr, index, right)

def partition(arr, left, right, pivot):
	while (left <= right):
		while (arr[left] < arr[pivot]):
			left += 1
		while (arr[right] > arr[pivot]):
			right -= 1
		if (left <= right):
			swap(arr, left, right)
			left += 1
			right -= 1
	return left

def swap(arr, i : int, j: int):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

def main():
	#arr = [10, 7, 3, 12, 0, 69, 11, 2, 6]
	arr = [45, 12, 99, 69, 1, 13]
	QuickSort(arr)
	print(arr)

	"""
	OUTPUT:
	pivot: 2
	index: 69
	Recursive call stack 
	left: [45, 12, 13, 1]
	right: [69, 99]
	
	pivot: 1
	index: 13
	Recursive call stack 
	left: [1, 12]
	right: [13, 45]
	
	pivot: 0
	index: 12
	Recursive call stack 
	left: [1]
	right: [12]
	
	 BASE CASE: left: 0, right: 0
	 BASE CASE: left: 1, right: 1
	pivot: 2
	index: 45
	Recursive call stack 
	left: [13]
	right: [45]
	
	 BASE CASE: left: 2, right: 2
	 BASE CASE: left: 3, right: 3
	pivot: 4
	index: 99
	Recursive call stack 
	left: [69]
	right: [99]
	
	 BASE CASE: left: 4, right: 4
	 BASE CASE: left: 5, right: 5
	[1, 12, 13, 45, 69, 99]
	"""

if __name__ == '__main__':
    main()