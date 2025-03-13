import sys
import mcb185
import itertools
import sequence

def missing_kmer(seq,k):
	kcount = {}
	for i in range(len(seq) - k + 1):
		kmer = seq[i:i+k]
		kcount[kmer] = 1 
	rc_seq = sequence.revcomp(seq)
	for i in range(len(rc_seq) - k + 1):
		kmer = rc_seq[i:i+k]
		kcount[kmer] = 1
	# Generate all possible k-mers
	all_kmers = set(''.join(nts) for nts in itertools.product('ACGT',repeat=k))
	# Find missing k-mers
	missing_kmer = all_kmers - set(kcount.keys()) # Convert dictionary keys to a set
	return missing_kmer # Return the set of missing k-mers

ecoligenome = sys.argv[1]
for defline, seq in mcb185.read_fasta(ecoligenome):
	k = 1 # Start with k=1
	while True:
		mis_kmer = missing_kmer(seq,k) # use the function to find missing kmers
		if mis_kmer:
			print(f'k={k}: {len(mis_kmer)} missing k-mer')
			for kmer in sorted(mis_kmer):
				print(kmer)
			break 
		k += 1 


