import random

def roll_dice():
    return random.randint(1, 6)

def monte_carlo_simulation(num_trials):
    results = {i: 0 for i in range(2, 13)}
    for _ in range(num_trials):
        result = roll_dice() + roll_dice()
        results[result] += 1
    probabilities = {key: value / num_trials * 100 for key, value in results.items()}
    return probabilities

def print_probabilities(probabilities):
    print("Сума\tІмовірність")
    for key, value in probabilities.items():
        print(f"{key}\t{value:.2f}% ({value / 100:.2f})")

# Проведемо симуляцію для великої кількості кидків кубиків
num_trials = 1000000
probabilities = monte_carlo_simulation(num_trials)

# Виведемо результати
print_probabilities(probabilities)
