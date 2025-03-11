import sys
import mcb185


let = [
    "I", "V", "L", "F", "C", "M", "A", "G", "T", "S", "W", "Y", "P", 
    "H", "E", "Q", "D", "N", "K", "R"]

phobs = [
    4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, -0.9, -1.3, 
    -1.6, -3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5]


def kd(seq):
    tot = 0
    for nt in seq:
        if nt in let:
            tot += phobs[let.index(nt)]
    return tot / len(seq)

"""
aas = []
defline = []

#print(aa, defline)

with gzip.open(sys.argv[1], 'rt') as fp:
    #print(fp.read()) #string
    #print('placeholder')
    #print(fp.read().split()[])
    #print()

    cont = 0 
    i = 0

    per = [] #temporary storage of a list per defline
    seq = ''
    for f in fp:
        if f.count('>') != 0:
            defline.append(f)
            cont = 0
            seq = ''
            i += 1

        else:
            cont += 1
            if cont > 0:
                seq += f
            
        sqs = list(seq)
        #print(seq)
        if seq != '':
            for j, sq in enumerate(sqs):
                if sq ==  '\n':
                    sqs[j] = ''
            #print(sqs)
            per.append(''.join(sqs))

        
        if len(defline) > len(aas):
            aas.append(per)

    
#print(len(defline))
#print(len(aas))
#print(aas)

#print('1')

for line, aa in zip(defline, aas):

"""

x = 0
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    #print(seq)
    #print(defline, '\n', seq)

    signal = False
    trans = False

    Nterm = seq[0:30]
    Cterm = seq[30:]

    for i in range(0, len(Nterm)-8+1, 1):
        if kd(Nterm[i:i+8]) >= 2.5:
            signal = True

    for i in range(0, len(Cterm)-11+1, 1):
        if kd(Cterm[i:i+11]) >= 2.0:
            trans = True 

    if signal == True and trans == True:
        print(defline)
        x += 1
                        
print(x) #521 proteins
            
    








#print(kd('MKKTAAGGCTAGGAGGTAGGAGGAGGGAGGAGGAGGAGGAGGGGAG'))



"""
seq = 'MKKTAAGGCTAGGAGGTAGGAGGAGGGAGGAGGAGGAGGAGGGGAG'

tot = 0
for nt in seq:
    if nt in aas:
        idx = aas.index(nt)
        #print(idx)
        tot += phobs[idx]

"""