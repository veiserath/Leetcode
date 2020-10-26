def SortArrayByParity(A):
	B = []
	C = []
	D = []
	for number in A:
		if number % 2 == 0:
			B.append(number)
		if number % 2 != 0:
			C.append(number)
	D = B + C
	return D
A = [3,1,2,4]
print(SortArrayByParity(A))
