def sortt(arr):
	n = len(arr)
	step = n
	while step > 1:
		step = int(step/1.3)
		for i in range(0,n - step):
			if arr[i] > arr[i + step]:
				tmp = arr[i + step]
				arr[i + step] = arr[i]
				arr[i] = tmp
	return arr
print(sortt([8,4,1]))
