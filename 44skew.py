import sys
import mcb185

w = int(sys.argv[2])

"""
import sequence

def gc_cmp1(g, c):
    return g + c / len(seq)

def gc_skw1(g, c):
    if g+c == 0: return 0
    return (g-c)/ (g+c)

def gc_sum(seq):
    g = seq.count('G')
    c = seq.count('C')

    return g, c

seq1 = 'ACGTACGTGGGGGACGTACGTCCCCC'


og = seq1[0:w]
print(0, sequence.gc_comp(og), sequence.gc_skw(og))

g = gc_sum(og)[0]
c = gc_sum(og)[1]

x = 1
for i in range(0, len(seq1) - w + 1, 1):
    s1 = seq1[w:w + i]
    if s1 == 'G': g += 1
    if s1 == 'C': c += 1
    
    
    s2 = seq[i:i+1]
    if s1 == 'G': g -= 1
    if s1 == 'C': c -= 1



    print(x, gc_cmp1(g, c), gc_skw1(g, c))
    x += 1

"""
import sys
import mcb185

w = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    g = 0
    c = 0
    x = 0

    og = seq[0:w]

    g = og.count('G')
    c = og.count('C')

    if g+c != 0:
        print(x, g+c/len(og), (g-c)/(g+c))
    else:
        print(x, 0, 0)

    
    for i in range(w, len(seq)+1):
        off =seq[i-w]
        on = seq[i]

        if on == 'G':
            g += 1
        if on == 'C':
            c += 1
        
        if off == 'G':
            g -= 1
        if off == 'C':
            c -= 1
        
        x += 1
        if g+c != 0:
            print(x, g+c/len(og), (g-c)/(g+c))
        else:
            print(x, 0, 0)
    print()