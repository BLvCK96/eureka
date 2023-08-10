import numpy as np

# Given distance matrix
distance_matrix = [
    [0, 10.0, 10.8, 6.3, 13.0, 13.4, 16.4, 5.1, 6.4, 8.2, 7.1],
    [0, 0, 7.1, 10.6, 3.6, 5.4, 9.5, 4.4, 7.2, 10.6, 3.0],
    [0, 0, 0, 7.0, 6.4, 12.4, 16.5, 6.4, 12.1, 15.7, 7.3],
    [0, 0, 0, 0, 12.1, 15.6, 19.4, 5.8, 11.2, 14.0, 8.6],
    [0, 0, 0, 0, 0, 7.1, 11.0, 8.0, 10.8, 14.2, 6.3],
    [0, 0, 0, 0, 0, 0, 4.1, 9.9, 8.1, 10.2, 7.1],
    [0, 0, 0, 0, 0, 0, 0, 13.6, 10.3, 11.2, 10.8],
    [0, 0, 0, 0, 0, 0, 0, 0, 6.1, 9.5, 2.8],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3.6, 5.0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8.6]
]

num_customers = len(distance_matrix) - 1

# Calculate savings values
savings = np.zeros((num_customers + 1, num_customers + 1))
for i in range(1, num_customers + 1):
    for j in range(i + 1, num_customers + 1):
        savings[i][j] = distance_matrix[i][0] + distance_matrix[0][j] - distance_matrix[i][j]

# Create a list of savings values with corresponding customer pairs
savings_list = []
for i in range(1, num_customers):
    for j in range(i + 1, num_customers + 1):
        savings_list.append((savings[i][j], i, j))

# Sort the savings list in descending order
savings_list.sort(reverse=True)

# Initialize routes (each customer is initially assigned to a separate route)
routes = [[i] for i in range(1, num_customers + 1)]

# Merge routes based on savings values
for saving, i, j in savings_list:
    for route in routes:
        if i in route and j not in route:
            idx_i = route.index(i)
            new_route = route[:idx_i + 1] + [j] + route[idx_i + 1:]
            if all(new_route in r for r in routes):
                route[:] = new_route
                break

# Print the final routes
for idx, route in enumerate(routes):
    print(f"Route {idx + 1}: {' -> '.join(map(str, route))}")
  # Sort the savings list in descending order
savings_list.sort(reverse=True)

# Extract the highest saving value and corresponding customer pair
highest_saving, i, j = savings_list[0]

# Print the highest saving value and corresponding customer pair
print(f"Highest Saving Value: {highest_saving}")
print(f"Corresponding Customer Pair: ({i}, {j})")
