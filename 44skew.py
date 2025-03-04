import sys
import mcb185  

def gc_skew_optimized(seq, window):
    """Efficient GC-skew and GC composition calculation using a sliding window approach."""
    if len(seq) < window:
        return

    g_count = seq[:window].count('G')
    c_count = seq[:window].count('C')

    gc_comp = (g_count + c_count) / window
    gc_skew = (g_count - c_count) / (g_count + c_count) if (g_count + c_count) != 0 else 0
    print(0, gc_comp, gc_skew)

    for i in range(1, len(seq) - window + 1):
        left_nt = seq[i - 1]
        right_nt = seq[i + window - 1]

        if left_nt == 'G': g_count -= 1
        if left_nt == 'C': c_count -= 1
        if right_nt == 'G': g_count += 1
        if right_nt == 'C': c_count += 1

        gc_comp = (g_count + c_count) / window
        gc_skew = (g_count - c_count) / (g_count + c_count) if (g_count + c_count) != 0 else 0
        print(i, gc_comp, gc_skew)

def run():
    if len(sys.argv) != 3:
        print("Usage: python 44skew.py <fasta_file> <window_size>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    window_size = int(sys.argv[2])

    for defline, seq in mcb185.read_fasta(fasta_file):
        gc_skew_optimized(seq, window_size)

run()
