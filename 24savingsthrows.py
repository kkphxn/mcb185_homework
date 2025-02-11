import math
import random

def max_roll(r1, r2):
	if r1 < r2: return 1
	return 2

def min_roll(r1, r2):
	if r1 > r2: return r1
	return r2

def saving_throw(dc, event):
	roll1 = random.radint(1, 20)
	roll2 = random.randint(1,20)
	if event == 'none':
		roll = roll1
		print(roll)
		if roll >= dc: return 'success'
		else: return 'fail'
	if event == 'advantage':
		roll = max_roll(roll1, roll2)
		print(roll)
		if roll >= dc: return 'success'
		else: return 'fail'
	if event == 'disadvantage':
		roll = min_roll(roll1, roll2)
		print(roll)
		if roll >= dc: return 'success'
		else: return 'fail'
print(saving_throw(10, 'none'))
print(savong_throw(15, 'advantage'))