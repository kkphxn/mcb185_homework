import random
import math

for a in range(1, 101):
	for b in range(a, 101):
		c = math.sqrt(a**2 + b**2)
		if c % 1 == 0: print(a, b, c)