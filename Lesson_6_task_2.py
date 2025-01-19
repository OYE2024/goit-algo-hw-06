from Lesson_6_task_1 import G
from collections import deque


# Алгоритм ВАІ (обход графа):
def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


path_dfs = dfs_recursive(G, 7)
print(path_dfs)

# Алгоритм DFS (з точки до точки):
# def dfs_routes(graph, vertex, goal, visited=None):
#     if visited is None:
#         visited = []
#     visited.append(vertex)
#     if vertex == goal:
#         return visited
#     for neighbor in graph[vertex]:
#         if neighbor not in visited:
#             result = dfs_routes(graph, neighbor, goal, visited)
#             if result:
#                 return result
#     visited.pop()
#     return None


# path_dfs_routes = dfs_routes(G, 7, 38)
# print(path_dfs_routes)


# Алгоритм BFS
def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    bfs_recursive(graph, queue, visited)


path_bfs = bfs_recursive(G, deque([7]))
print(path_bfs)
