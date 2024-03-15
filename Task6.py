def greedy_algorithm(items, budget):
    selected_items = []
    remaining_budget = budget

    # Сортування страв за калорійністю у спадаючому порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'], reverse=True)

    for item, info in sorted_items:
        if info['cost'] <= remaining_budget:
            selected_items.append(item)
            remaining_budget -= info['cost']

    max_calories = sum(items[item]['calories'] for item in selected_items)
    return selected_items, max_calories

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(budget + 1):
            item_name = list(items.keys())[i - 1]
            cost = items[item_name]['cost']
            calories = items[item_name]['calories']

            if cost <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)
            else:
                dp[i][j] = dp[i - 1][j]

    selected_items = []
    j = budget
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            item_name = list(items.keys())[i - 1]
            selected_items.append(item_name)
            j -= items[item_name]['cost']

    max_calories = dp[n][budget]
    return selected_items, max_calories


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

selected_items_greedy, max_calories_greedy = greedy_algorithm(items, budget)
selected_items_dynamic, max_calories_dynamic = dynamic_programming(items, budget)

print("Greedy Algorithm:")
print("Selected items:", selected_items_greedy)
print("Maximum calories:", max_calories_greedy)

print("\nDynamic Programming:")
print("Selected items:", selected_items_dynamic)
print("Maximum calories:", max_calories_dynamic)
