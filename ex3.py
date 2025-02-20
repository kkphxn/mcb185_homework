import sys
import statistics

def calculate_z_scores(numbers, mean, std_dev):
    if std_dev == 0:
        return [0] * len(numbers) 
    return [(x - mean) / std_dev for x in numbers]

def main():
    if len(sys.argv) < 2:
        print("python3 32stats.py num1 num2 num3 ...")
        return

    try:
        numbers = list(map(float, sys.argv[1:]))
    except ValueError:
        print("error: enter valid numbers")
        return

    count = len(numbers)
    min_value = min(numbers)
    max_value = max(numbers)
    mean_value = statistics.mean(numbers)
    std_dev = statistics.stdev(numbers) if count > 1 else 0
    median_value = statistics.median(numbers)
    z_scores = calculate_z_scores(numbers, mean_value, std_dev)

    print(f"numb of values: {count}")
    print(f"min value: {min_value}")
    print(f"max value: {max_value}")
    print(f"mean: {mean_value}")
    print(f"standard deviation: {std_dev}")
    print(f"median: {median_value}")
    print("\nZ-scores:")
    for num, z in zip(numbers, z_scores):
        print(f"value: {num}, z-score: {z:.2f}")

if __name__ == "__main__":
    main()