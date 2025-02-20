import sys
import statistics

def main():
    if len(sys.argv) < 2:
        print("Usage: python stats_report.py <numbers>")
        sys.exit(1)
    
    try:
        numbers = list(map(float, sys.argv[1:]))
    except ValueError:
        print("Error: Please enter valid numbers.")
        sys.exit(1)
    
    num_values = len(numbers)
    min_value = min(numbers)
    max_value = max(numbers)
    mean_value = statistics.mean(numbers)
    std_dev = statistics.stdev(numbers) if num_values > 1 else 0.0
    median_value = statistics.median(numbers)
    
    print(f"Number of values: {num_values}")
    print(f"Minimum value: {min_value}")
    print(f"Maximum value: {max_value}")
    print(f"Mean: {mean_value}")
    print(f"Standard Deviation: {std_dev}")
    print(f"Median: {median_value}")
    
if __name__ == "__main__":
    main()