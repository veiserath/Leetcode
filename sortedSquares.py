def sortedSquares(A):
	B = []
	for number in A:
		number = number**2
		B.append(number)
	B.sort(reverse=False)
	return B
A = [-4,-1,0,3,10]
print(sortedSquares(A))
