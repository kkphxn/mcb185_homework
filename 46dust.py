import sys
import math

def calculate_entropy(sequence):
    seq_length = len(sequence)
    counts = {}
    for base in sequence:
        counts[base] = counts.get(base, 0) + 1

    entropy = 0.0
    for base in counts:
        prob = counts[base] / seq_length
        entropy -= prob * math.log(prob, 2)

    return entropy

def mask_low_complexity(sequence, window_size, entropy_threshold):
    seq_list = list(sequence)  # Convert to list for easier mutation
    for i in range(len(sequence) - window_size + 1):
        window = sequence[i:i + window_size]
        entropy = calculate_entropy(window)
        
                if entropy < entropy_threshold:
            seq_list[i:i + window_size] = ['N'] * window_size
    
    return ''.join(seq_list)

def parse_fasta(input_file):
    sequences = []
    with open(input_file, 'r') as file:
        header = None
        sequence = []
        
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if header is not None:
                    sequences.append((header, ''.join(sequence)))
                header = line
                sequence = []
            else:
                sequence.append(line)
        
        if header is not None:
            sequences.append((header, ''.join(sequence)))  

    print(f"Found {len(sequences)} sequences.")  
    if len(sequences) == 0:
        print("No sequences found in the file.")
    return sequences

def write_output(output_records, output_file):
    with open(output_file, 'w') as out_handle:
        for header, sequence in output_records:
            out_handle.write(f"{header}\n")
            for i in range(0, len(sequence), 60):
                out_handle.write(f"{sequence[i:i+60]}\n")
    print(f"Output written to {output_file}")  

def process_fasta(input_file, window_size, entropy_threshold):
    sequences = parse_fasta(input_file)
    output_records = []

    for header, sequence in sequences:
        print(f"Processing sequence: {header}") 
        masked_sequence = mask_low_complexity(sequence, window_size, entropy_threshold)
        
        print(f"Masked sequence (first 100 chars): {masked_sequence[:100]}")  
        output_records.append((header, masked_sequence))

    return output_records

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 46dust.py <input_fasta_file> <window_size> <entropy_threshold>")
        sys.exit(1)

    input_fasta = sys.argv[1]
    window_size = int(sys.argv[2])
    entropy_threshold = float(sys.argv[3])

    print(f"Processing file: {input_fasta}")
    output_records = process_fasta(input_fasta, window_size, entropy_threshold)

    output_file = "masked_" + input_fasta
    write_output(output_records, output_file)