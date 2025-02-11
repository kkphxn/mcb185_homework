import math

chr(33)
print(chr(33))
print(ord('!'))

def phred_to_error(symbol):
	q = ord(symbol) - 33
	
	p = 10**(q / -10)
	return p
print(phred_to_error('^'))
print(phred_to_error('0'))
print(phred_to_error('@'))
print(phred_to_error('!'))
print(phred_to_error('('))

def error_to_phred(p):
	g = -10 * (math.log10(p))
	i = int(g//1) * 33
	return chr(i)
print(error_to_phred(0.006))
print(error_to_phred(0.003))
print(error_to_phred(0.05))
print(error_to_phred(0.50))
print(error_to_phred(0.25))