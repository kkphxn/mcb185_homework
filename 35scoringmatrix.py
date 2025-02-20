import sys

def generate_scoring_matrix(alphabet, match, mismatch):
    # Print header row
    print("   " + "  ".join(alphabet))

    # Generate the matrix
    for base1 in alphabet:
        row = [base1]  # Start the row with the character label
        for base2 in alphabet:
            score = match if base1 == base2 else mismatch
            row.append(f"{score:+d}")  # Format to always show sign
        print("  ".join(row))

if __name__ == "__main__":
    # Ensure correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: python3 35scoringmatrix.py <alphabet> <match> <mismatch>")
        sys.exit(1)

    alphabet = sys.argv[1]  # First argument is the alphabet (e.g., "ACGT")
    match = int(sys.argv[2])  # Second argument is the match score
    mismatch = int(sys.argv[3])  # Third argument is the mismatch score

    generate_scoring_matrix(alphabet, match, mismatch)
