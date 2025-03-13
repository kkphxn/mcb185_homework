import argparse
import mcb185
import math
import sys

def calculate_entropy(sequence):
	nts = 'ACGT'
	counts = [0] * len(nts) # Initialize counts for A, C, G, T
	for nt in sequence:
		idx = nts.find(nt)
		if idx != -1: # ignore non-ACGT characters
			counts[idx] += 1
	
	total = sum(counts)
	if total == 0:
		return 0
	
	entropy = 0 
	for count in counts:
		if count > 0:
			p = count / total
			entropy -= p * math.log2(p)
	return entropy
	
def mask_low_complexity(sequence, window_size, entropy_threshold):
	masked_sequence = list(sequence) 
	for i in range(len(sequence) - window_size + 1):
		window = sequence[i:i + window_size]
		entropy = calculate_entropy(window)
		if entropy < entropy_threshold:
			for j in range(i, i + window_size):
				masked_sequence[j] = 'N'
	return ''.join(masked_sequence)

def wrap_sequence(sequence, line_length=60):
    return '\n'.join(sequence[i:i + line_length] 
    for i in range(0, len(sequence), line_length))

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('--size', type=int, default=20,
    help='window size [%(default)i]')
parser.add_argument('--entropy', type=float, default=1.4,
    help='entropy threshold [%(default).3f]')
arg = parser.parse_args()

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    new_seq = mask_low_complexity(seq,arg.size, arg.entropy)
    wrapped_seq = wrap_sequence(new_seq)
    print(wrapped_seq)