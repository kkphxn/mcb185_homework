import sys
import mcb185
import math

win = int(sys.argv[2])
thres = float(sys.argv[3])

def entropy(dna):
    h = 0

    if len(dna) == 0:   
        return 0

    probs = [0,0,0,0]
    probs[0] = dna.count('A') / len(dna)
    probs[1] = dna.count('G') / len(dna)
    probs[2] = dna.count('C') / len(dna)
    probs[3] = dna.count('T') / len(dna)

    for prob in probs:
        if prob > 0:
            h -= prob * math.log2(prob)

    return h


for defline, seq in mcb185.read_fasta(sys.argv[1]):
    # print(defline, seq)
    sq = list(seq) #convert string into seq
    for i in range(0, len(seq) - win + 1, 1):
        #print(''.join(sq[i:i+win]))
        if entropy( sq[i:i+win] ) < thres:
            #print(entropy(sq[i:i+win]))
            for j in range(i, i + win):
                sq[i] = 'N'
    print(defline)
    seq1 = ''.join(sq)
    #print(seq1)
    for i in range(0, len(seq1) + 61, 60):
        print(seq1[i:i+60])
    print() #line delim btw seq