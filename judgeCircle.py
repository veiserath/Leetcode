#problem 657 leetcode
def judgeCircle(moves):
	L = 0
	R = 0
	U = 0
	D = 0
	origin = False
	for letter in moves:
		if letter == 'U':
			U += 1
		if letter == 'D':
			U -= 1
		if letter == 'R':
			R += 1
		if letter == 'L':
			R -= 1
	if U == 0 and R == 0:
		origin = True
	return origin
moves = "LR"
print(judgeCircle(moves))
