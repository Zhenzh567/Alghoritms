def func(x):
	for k in range(0,100):
		for l in range(0,100):
			for m in range(0,100):
				for i in range(1, x + 1):
					if 3**k * 5**l * 7**m == i:
						print(i)

def func1(x):
	result = []
	for i in range(1,x + 1):
		n = i
		while n % 3 == 0:
			n = n // 3
		while n % 5 == 0:
			n = n // 5 
		while n % 7 == 0:
			n = n // 7
		if n == 1:
			result.append(i)
	return result
print(func(30))
print(func1(30))
