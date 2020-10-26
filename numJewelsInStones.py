def numJewelsInStones(J: 'str', S: 'str') -> 'int':
	x = 0
	for master_letter in J:
		for letter in S:
			if letter == master_letter:
				x += 1
	return x
J = ['a', 'A']
S = ['a', 'a', 'A', 'b', 'z']
print(numJewelsInStones(J,S))
