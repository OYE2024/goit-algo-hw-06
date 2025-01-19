from Lesson_6_task_1 import G
import networkx as nx

# Перетворюємо граф у словник
graph_dict = nx.to_dict_of_dicts(G)

# Додаємо вагу ребер
for u, v in G.edges():
    G[u][v]['weight'] = 1


# Функція пошуку найкоротшого шляху в графі:
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        if distances[current_vertex] == float('infinity'):
            break
        for neighbor, attributes in graph[current_vertex].items():
            weight = attributes['weight']
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
        unvisited.remove(current_vertex)

    return distances


result = dijkstra(graph_dict, 72)
# Фільтруємо значення словника по зростанню.
sorted_result = sorted(result.items(), key=lambda item: item[1])
print(sorted_result)
