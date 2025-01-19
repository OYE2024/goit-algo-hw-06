import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import csv
import ast

# Відкриваємо базу даних на считку
# with open(file_path, 'r', encoding='utf-8') as file:
#     bus_routes = csv.reader(file)
#     for row in bus_routes:
#         print(row)

# Відкриваємо базу даних на считку
bus_routes = pd.read_csv('bus_routes.csv')
# print(bus_routes)
# print(bus_routes.dtypes)
# print(bus_routes['stops'])
bus_routes['stops'] = bus_routes['stops'].apply(ast.literal_eval)
# print(bus_routes['stops'])

# Отримуємо унікальні зупинки
all_stops = sorted({stop for stops in bus_routes['stops'] for stop in stops})

# Створюємо список суміжності
adj_list = {stop: [] for stop in all_stops}
for stops in bus_routes['stops']:
    for i in range(len(stops) - 1):
        adj_list[stops[i]].append(stops[i + 1])
        adj_list[stops[i + 1]].append(stops[i])

print("\nAdjective list:")
for stop, neighbors in adj_list.items():
    print(f"{stop}: {neighbors}")

G = nx.Graph()  # Неорієнтований граф

# Додаємо ребра на основі маршрутів
for stops in bus_routes['stops']:
    for i in range(len(stops) - 1):
        # Додаємо ребро між сусідніми зупинками
        G.add_edge(stops[i], stops[i + 1])

# Візуалізуємо граф
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
ax = plt.gca()
nx.draw(
    G, pos, with_labels=True, node_color='skyblue', node_size=500, font_size=10, font_weight='bold'
)
ax.set_title("Граф автобусних маршрутів", fontsize=16)
plt.show()

# Аналіз графа
print(f'Number of nodes for buses routes graph are: {G.number_of_nodes()}')
print(f'Number of adges for buses routes graph are: {G.number_of_edges()}')
degrees = dict(G.degree())
for node, degree in degrees.items():
    print(f"Node {node} has degrees {degree}")
