import sys

def dtc(P, Q):
    return sum(abs(p - q) for p, q in zip(P, Q))

def find_closest_color(colorfile, R, G, B):
    min_distance = float('inf')
    closest_color = None

    try:
        with open(colorfile, 'r') as file:
            for line in file:
                if line.startswith('#') or not line.strip():
                    continue
                fields = line.strip().split('\t')
                if len(fields) < 4: 
                    continue
                name = fields[0]
                try:
                    r, g, b = map(int, fields[1:4])
                except ValueError:
                    continue 

                distance = dtc((R, G, B), (r, g, b))
                if distance < min_distance:
                    min_distance = distance
                    closest_color = name
    except FileNotFoundError:
        print(f"Error: File '{colorfile}' not found.")
        sys.exit(1)

    return closest_color

def run():
    if len(sys.argv) != 5:
        print("Usage: python3 45colorname.py <color_file> <R> <G> <B>")
        sys.exit(1)

    colorfile = sys.argv[1]
    try:
        R, G, B = map(int, sys.argv[2:5])
    except ValueError:
        print("Error: RGB values must be integers.")
        sys.exit(1)

    closest_color = find_closest_color(colorfile, R, G, B)
    if closest_color:
        print(closest_color)
    else:
        print("No matching color found.")

run()