import matplotlib.pyplot as plt  # For local visualization

# Define the race data based on provided 2025 results, adjusted for new information
races = {
    'British': [
        {'driver': 'Lando Norris', 'team': 'McLaren', 'points': 25},
        {'driver': 'Oscar Piastri', 'team': 'McLaren', 'points': 18},  # Penalized but still P2
        {'driver': 'N. Hülkenberg', 'team': 'Kick Sauber', 'points': 15}
    ],
    'Belgian': [
        {'driver': 'Oscar Piastri', 'team': 'McLaren', 'points': 25},
        {'driver': 'Lando Norris', 'team': 'McLaren', 'points': 18},
        {'driver': 'Charles Leclerc', 'team': 'Ferrari', 'points': 15}
    ],
    'Hungarian': [
        {'driver': 'Lando Norris', 'team': 'McLaren', 'points': 25},
        {'driver': 'Oscar Piastri', 'team': 'McLaren', 'points': 18},
        {'driver': 'George Russell', 'team': 'Mercedes', 'points': 15}
    ],
    'Dutch': [
        {'driver': 'Oscar Piastri', 'team': 'McLaren', 'points': 25},
        {'driver': 'Max Verstappen', 'team': 'Red Bull', 'points': 18},
        {'driver': 'Isack Hadjar', 'team': 'Racing Bulls', 'points': 15}
        # Norris DNF: 0 points (originally 18 for P2)
    ]
}

# Define weights for each race (more recent races have higher weights)
weights = {
    'Dutch': 4,
    'Hungarian': 3,
    'Belgian': 2,
    'British': 1
}

# Initialize a dictionary to store total weighted points for each driver
driver_points = {}

# Calculate weighted points for each driver
for race, results in races.items():
    for result in results:
        driver = result['driver']
        points = result['points']
        weighted_points = points * weights[race]
        
        # Add weighted points to driver's total
        if driver in driver_points:
            driver_points[driver] += weighted_points
        else:
            driver_points[driver] = weighted_points

# Apply adjustments for external factors
# 1. Penalty for Piastri (British GP): Reduce British GP points by 10%
if 'Oscar Piastri' in driver_points:
    for result in races['British']:
        if result['driver'] == 'Oscar Piastri':
            driver_points['Oscar Piastri'] -= int(0.1 * result['points'] * weights['British'])

# 2. Monza track factor: Boost McLaren (10%) and Ferrari (15%) based on 2024 Italian GP
monza_boost = {'McLaren': 1.1, 'Ferrari': 1.15, 'Red Bull': 1.05, 'Racing Bulls': 1.0, 'Mercedes': 1.0, 'Kick Sauber': 1.0}
for driver, points in driver_points.items():
    for race, results in races.items():
        for result in results:
            if result['driver'] == driver:
                team = result['team']
                driver_points[driver] = int(points * monza_boost.get(team, 1.0))
                break

# 3. Reliability penalty: Reduce points for drivers with DNFs (Leclerc)
if 'Charles Leclerc' in driver_points:
    driver_points['Charles Leclerc'] = int(driver_points['Charles Leclerc'] * 0.9)  # 10% penalty for DNF

# 4. Qualifying boost: 15% for Norris (2024 Italian pole), 10% for Leclerc/Verstappen (2025 poles)
qualifying_boost = {'Lando Norris': 1.15, 'Charles Leclerc': 1.1, 'Max Verstappen': 1.1}
for driver, points in driver_points.items():
    if driver in qualifying_boost:
        driver_points[driver] = int(points * qualifying_boost[driver])

# Find the driver with the highest weighted points
predicted_winner = max(driver_points, key=driver_points.get)
max_points = driver_points[predicted_winner]

# Print the results
print("Weighted points for each driver (after adjustments):")
for driver, points in sorted(driver_points.items(), key=lambda x: x[1], reverse=True):
    print(f"{driver}: {points} points")

print(f"\nPredicted winner for the Italian Grand Prix: {predicted_winner} with {max_points} points")

# Generate a matplotlib bar chart for local visualization
plt.figure(figsize=(10, 6))
drivers = list(driver_points.keys())
points = list(driver_points.values())
colors = ['#FF6F61', '#6B7280', '#22D3EE', '#34D399', '#FBBF24', '#F472B6', '#60A5FA']
plt.bar(drivers, points, color=colors[:len(drivers)])
plt.xlabel('Drivers')
plt.ylabel('Weighted Points')
plt.title('F1 Italian Grand Prix 2025 Prediction: Driver Points')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()