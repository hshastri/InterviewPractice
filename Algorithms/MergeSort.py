def MergeSort(arr):
	
	if len(arr) > 1:

		#split the arrays into two sub arrays 
		mid = len(arr) // 2
		left = arr[:mid] 
		right = arr[mid:] 

		#recursive call on each sub array
		MergeSort(left)
		MergeSort(right)

		#copying the sorted halves into the array 
		i = j = k = 0 #i to moniter left, j to moniter right, k to copy into the array

		while (i < len(left) and j < len(right)):
			if left[i] <= right[j]:
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j += 1
			k += 1

		#filling up the remaining of the elements
		while i < len(left):
			arr[k] = left[i]
			i += 1
			k += 1

		while j < len(right):
			arr[k] = right[j]
			j += 1
			k += 1
		"""
		print("call")
		print(left)
		print(right)
		print("done")"""
def main():
	arr = [45,12,99,69,1,13]
	MergeSort(arr)
	print(arr)

if __name__ == '__main__':
	main()

