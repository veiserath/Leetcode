def flipAndInvertImage(A):
	B = []
	C = []
	for matrix in A:
		mylist = []
		for i in reversed(matrix):
			mylist += [i]
		B.append(mylist)
		# print(B)
	for matrix1 in B:
		for n, i in enumerate(matrix1):
			if i == 1:
				matrix1[n] = 0
			if i == 0:
				matrix1[n] = 1
		C.append(matrix1)
	return C
A = [[1,1,0],[1,0,1],[0,0,0],[1,0,0]]
print(flipAndInvertImage(A))