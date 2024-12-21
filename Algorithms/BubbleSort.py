def BubbleSort(arr):
	isSorted : bool = False
	lastUnsorted = len(arr) - 1
	while (isSorted == False):
		isSorted = True
		for i in range(0, lastUnsorted):
			if arr[i] > arr[i + 1]:
				swap(arr, i, i + 1)
				isSorted = False
		lastUnsorted -= 1


def swap(arr, i : int, j: int):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

def main():
	arr = [10, 3, 5, 12, 20, 9]
	BubbleSort(arr)
	print(arr)

if __name__ == '__main__':
	main()


