
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Create directory for graphs
os.makedirs("bmtc_graphs", exist_ok=True)

# 1. Passenger Count per Route
routes = [201, 202, 203, 204, 205, 206]
passengers = [18000, 21000, 15000, 12000, 9000, 7000]
plt.figure(figsize=(8,5))
plt.bar(routes, passengers, color='skyblue')
plt.title('Passenger Count per Route - 2025')
plt.xlabel('Route Number')
plt.ylabel('Passengers per Day')
plt.savefig("bmtc_graphs/1_passenger_count_per_route.png")
plt.close()

# 2. Bus Type Distribution
bus_types = ['Diesel', 'CNG', 'Electric']
counts = [320, 210, 150]
plt.figure(figsize=(6,6))
plt.pie(counts, labels=bus_types, autopct='%1.1f%%', startangle=140)
plt.title('BMTC Bus Type Distribution - 2025')
plt.savefig("bmtc_graphs/2_bus_type_distribution.png")
plt.close()

# 3. Average Speed vs Route
routes = ['201', '202', '203', '204', '205']
speed = [32, 30, 28, 25, 27]
plt.figure(figsize=(8,5))
plt.plot(routes, speed, marker='o', color='orange')
plt.title('Average Speed per Route - 2025')
plt.xlabel('Route Number')
plt.ylabel('Average Speed (km/h)')
plt.savefig("bmtc_graphs/3_average_speed_per_route.png")
plt.close()

# 4. Fuel Efficiency Comparison
bus_type = ['Diesel', 'CNG', 'Electric']
efficiency = [3.5, 4.2, 7.0]
plt.figure(figsize=(8,5))
plt.bar(bus_type, efficiency, color=['red', 'green', 'blue'])
plt.title('Fuel Efficiency by Bus Type (km/L or km/kWh)')
plt.xlabel('Bus Type')
plt.ylabel('Fuel Efficiency')
plt.savefig("bmtc_graphs/4_fuel_efficiency_comparison.png")
plt.close()

# 5. Maintenance Cost
bus_type = ['Diesel', 'CNG', 'Electric']
cost = [25000, 20000, 15000]
plt.figure(figsize=(8,5))
plt.bar(bus_type, cost, color='purple')
plt.title('Average Monthly Maintenance Cost')
plt.xlabel('Bus Type')
plt.ylabel('Cost (₹)')
plt.savefig("bmtc_graphs/5_maintenance_cost.png")
plt.close()

# 6. Yearly Fuel Consumption Trend
years = [2024, 2025]
consumption = [125000, 97000]
plt.figure(figsize=(8,5))
plt.plot(years, consumption, marker='s', color='brown')
plt.title('Yearly Fuel Consumption Trend')
plt.xlabel('Year')
plt.ylabel('Fuel (Litres)')
plt.savefig("bmtc_graphs/6_fuel_consumption_trend.png")
plt.close()

# 7. Bus Age vs Efficiency
age = [1, 3, 5, 7, 9, 11]
efficiency = [7.2, 6.8, 6.3, 5.9, 5.5, 5.0]
plt.figure(figsize=(8,5))
plt.plot(age, efficiency, marker='o', linestyle='--', color='teal')
plt.title('Bus Age vs Fuel Efficiency')
plt.xlabel('Bus Age (Years)')
plt.ylabel('Fuel Efficiency (km/L)')
plt.savefig("bmtc_graphs/7_bus_age_vs_efficiency.png")
plt.close()

# 8. Route with Lowest Buses
routes = ['201', '202', '203', '204', '205', '206']
buses = [40, 35, 25, 20, 15, 10]
plt.figure(figsize=(8,5))
plt.bar(routes, buses, color='crimson')
plt.title('Bus Count per Route (Lowest Highlighted)')
plt.xlabel('Route Number')
plt.ylabel('Number of Buses')
plt.savefig("bmtc_graphs/8_lowest_buses_per_route.png")
plt.close()

# 9. Monthly Fuel Variation
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
fuel = [10800, 10400, 11000, 10600, 9800, 9500, 9600, 9400, 9700, 9800, 9900, 10000]
plt.figure(figsize=(10,5))
plt.plot(months, fuel, marker='o', color='darkgreen')
plt.title('Monthly Fuel Consumption Variation - 2025')
plt.xlabel('Month')
plt.ylabel('Fuel (Litres)')
plt.savefig("bmtc_graphs/9_monthly_fuel_variation.png")
plt.close()

# 10. Passenger Trend (2024 vs 2025)
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
passengers_2024 = np.random.randint(8500, 11000, 12)
passengers_2025 = np.random.randint(9500, 12000, 12)
plt.figure(figsize=(10,5))
plt.plot(months, passengers_2024, label='2024', color='gray', linestyle='--')
plt.plot(months, passengers_2025, label='2025', color='blue', marker='o')
plt.title('Passenger Count Trend (2024 vs 2025)')
plt.xlabel('Month')
plt.ylabel('Passenger Count')
plt.legend()
plt.savefig("bmtc_graphs/10_passenger_trend_2024_2025.png")
plt.close()

# 11. Route-wise Ticket Revenue
routes = ['201', '202', '203', '204', '205', '206']
revenue = [120000, 100000, 85000, 70000, 60000, 40000]
plt.figure(figsize=(8,5))
plt.bar(routes, revenue, color='gold')
plt.title('Route-wise Ticket Revenue')
plt.xlabel('Route Number')
plt.ylabel('Revenue (₹)')
plt.savefig("bmtc_graphs/11_route_wise_revenue.png")
plt.close()

# 12. Fuel Consumption Trend (2024 vs 2025)
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
fuel_2024 = np.random.randint(10000, 12000, 12)
fuel_2025 = np.random.randint(8500, 10000, 12)
plt.figure(figsize=(10,5))
plt.plot(months, fuel_2024, label='2024', color='red', linestyle='--')
plt.plot(months, fuel_2025, label='2025', color='green', marker='o')
plt.title('Monthly Fuel Consumption Trend (2024 vs 2025)')
plt.xlabel('Month')
plt.ylabel('Fuel (Litres)')
plt.legend()
plt.savefig("bmtc_graphs/12_fuel_consumption_trend_2024_2025.png")
plt.close()
