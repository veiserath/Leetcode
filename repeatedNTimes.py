# problem 961
from collections import Counter
def repeatedNTimes(A):
	success = False
	B = Counter(A)
	for word, count in B.most_common(1):
		if len(A)/2 == count:
			return count