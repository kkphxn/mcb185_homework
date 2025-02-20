import random

def birthday_simulation(num_people, num_trials):
    shared_birthdays = 0  # Counter for trials where at least one shared birthday occurs

    for _ in range(num_trials):
        calendar = [0] * 365  # Initialize a list representing each day of the year

        for _ in range(num_people):
            birthday = random.randint(0, 364)  # Randomly assign a birthday
            calendar[birthday] += 1  # Increment the count for that day

        # Check if any day has more than one birthday
        if any(day > 1 for day in calendar):
            shared_birthdays += 1

    probability = shared_birthdays / num_trials  # Calculate probability
    return probability

# Example usage
num_people = 23  # Number of people in a room
num_trials = 10000  # Number of simulations
prob = birthday_simulation(num_people, num_trials)
print(f"Probability of at least one shared birthday among {num_people} people: {prob:.4f}")