import random
import sys

def has_duplicate_birthdays(people, days):
    birthdays = []
    for _ in range(people):
        birthday = random.randint(1, days)
        if birthday in birthdays:
            return True  # Short-circuit if duplicate found
        birthdays.append(birthday)
    return False

def simulate(trials, days, people):
    duplicate_count = 0
    for _ in range(trials):
        if has_duplicate_birthdays(people, days):
            duplicate_count += 1
    return duplicate_count / trials

def main():
    if len(sys.argv) != 4:
        print("Usage: python 33birthday.py <trials> <days> <people>")
        sys.exit(1)
    
    trials = int(sys.argv[1])
    days = int(sys.argv[2])
    people = int(sys.argv[3])
    
    probability = simulate(trials, days, people)
    print(f"Probability of at least two people sharing a birthday: {probability:.4f}")

if __name__ == "__main__":
    main()