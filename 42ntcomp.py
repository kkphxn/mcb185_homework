import sys
import mcb185 

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split()
    name = defwords[0]
    gc = sum(1 for nt in seq if nt in 'GC')
    print(name, gc / len(seq))
