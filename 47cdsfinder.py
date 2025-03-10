import sys
import gzip

# Standard DNA codon table
CODON_TABLE = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*', 'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

def reverse_complement(dna):
    """Returns the reverse complement of a DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement.get(base, base) for base in reversed(dna))

def translate_dna(dna_seq):
    """Translate a DNA sequence into a protein sequence."""
    protein = []
    for i in range(0, len(dna_seq) - 2, 3):
        codon = dna_seq[i:i+3]
        if codon in CODON_TABLE:
            protein.append(CODON_TABLE[codon])
        else:
            protein.append('X')  # Unknown codon
    return ''.join(protein)

def six_frame_translation(dna_seq):
    """Generate six-frame translations of a DNA sequence."""
    frames = [
        dna_seq, 
        dna_seq[1:], 
        dna_seq[2:], 
        reverse_complement(dna_seq), 
        reverse_complement(dna_seq)[1:], 
        reverse_complement(dna_seq)[2:]
    ]
    return [translate_dna(frame) for frame in frames]

def extract_orfs(protein_seq, min_length):
    """Extract ORFs from a protein sequence that start with 'M' and end with '*'."""
    orfs = []
    start = None
    for i, aa in enumerate(protein_seq):
        if aa == 'M' and start is None:
            start = i
        elif aa == '*' and start is not None:
            if (i - start) >= min_length:
                orfs.append(protein_seq[start:i+1])
            start = None
    return orfs

def parse_fasta(file_path):
    """Manually parse a FASTA file without Biopython."""
    sequences = {}
    current_id = None
    current_seq = []
    
    if file_path.endswith(".gz"):
        handle = gzip.open(file_path, "rt")
    else:
        handle = open(file_path, "r")

    for line in handle:
        line = line.strip()
        if line.startswith(">"):
            if current_id:
                sequences[current_id] = "".join(current_seq)
            current_id = line[1:]
            current_seq = []
        else:
            current_seq.append(line)
    
    if current_id:
        sequences[current_id] = "".join(current_seq)
    
    handle.close()
    return sequences

def find_orfs_in_fasta(input_file, min_length, output_file):
    """Process a FASTA file to find and output ORFs."""
    sequences = parse_fasta(input_file)

    with open(output_file, "w") as out_f:
        protein_id = 0
        for seq_id, dna_seq in sequences.items():
            translations = six_frame_translation(dna_seq)
            for frame_idx, protein_seq in enumerate(translations):
                orfs = extract_orfs(protein_seq, min_length)
                for orf in orfs:
                    out_f.write(f">{seq_id}-prot-{protein_id}\n{orf}\n")
                    protein_id += 1

def run():
    """Execute the script from command line."""
    if len(sys.argv) != 3:
        print("Usage: python3 47cdsfinder.py <input_fasta> <min_length>")
        sys.exit(1)

    input_fasta = sys.argv[1]
    min_length = int(sys.argv[2])

    output_fasta = input_fasta.replace(".fa", "_proteins.fa").replace(".gz", "")

    find_orfs_in_fasta(input_fasta, min_length, output_fasta)

    print(f"Output written to {output_fasta}")

run()