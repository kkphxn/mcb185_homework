import math

def a():
	for i in range(51, 1, -2):
		for j in range(2, (i // 2) + 1):
			if (i % j == 0):
				print (i)
				break
		else:
			print(i, "*")
a()
	