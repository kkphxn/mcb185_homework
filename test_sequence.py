import sequence

print(sequence.transcribe('ACGT'))
print(sequence.revcomp('AAAACGT'))

def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if   codon == 'ATG': aas.append('M')
		elif codon == 'TAA': aas.append('*')
		elif codon == 'TAG': aas.append('*')
		elif codon == 'TGA': aas.append('*')
		else:                aas.append('X')
	return ''.join(aas)

def translate(dna):
	codons = ('ATG', 'TAA', 'TAG', 'TGA')
	aminos = 'M***'
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon in codons:
			idx = codons.index(codon)
			aa = aminos[idx]
			aas.append(aa)
		else:
			aas.append('X')
	return ''.join(aas)