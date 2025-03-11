import sys
import mcb185

least = int(sys.argv[2])

def translate1(seq):
    prots =[]

    frame = 0
    for i in range(0, len(seq)): #find index of first ATG start codon
        pro = [] # need to empty every loop

        if seq[i:i+3] == 'ATG':
            frame = i
            for i in range(frame, len(seq), 3):
                codon = seq[i:i+3]
                if codon in mcb185.GCODE:
                    pro.append(mcb185.GCODE[codon])
                    if mcb185.GCODE[codon] == '*':
                        break
                else:
                    pro.append('X')            
        
        if len(pro) >= least: #add pro to prots
            a = ''.join(pro)
            prots.append(a)
    return prots


for defline, seq in mcb185.read_fasta(sys.argv[1]):
    prots = translate1(seq)

    print(defline)
    for prot in prots:
        print('>', end='')
        for i in range(0, len(prot) +1, 60):
            print(prot[i:i+60])
    print()