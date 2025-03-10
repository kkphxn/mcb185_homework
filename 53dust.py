import argparse

parser = argparse.ArgumentParser(description='DNA entropy filter.')  # Fixed missing quote

parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('size', type=int, help='window size')
parser.add_argument('entropy', type=float, help='entropy threshold')

arg = parser.parse_args()

print('dusting with', arg.file, arg.size, arg.entropy)
