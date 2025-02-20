import random

def birthday_simulation(num_people, num_trials):
    shared_birthdays = 0  

    for _ in range(num_trials):
        calendar = [0] * 365  

        for _ in range(num_people):
            birthday = random.randint(0, 364)  
            calendar[birthday] += 1  

        if any(day > 1 for day in calendar):
            shared_birthdays += 1

    probability = shared_birthdays / num_trials  
    return probability

num_people = 23  
num_trials = 10000 
prob = birthday_simulation(num_people, num_trials)
print(f"Probability of at least one shared birthday among {num_people} people: {prob:.4f}")