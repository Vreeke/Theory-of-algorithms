import sys

# ВХІДНІ ДАНІ
INF = float('inf')
num_vertices = 8

# Список суміжності: вершина -> [(сусід, вага), ...]
# (1, 4): 4, (1, 3): 2, (1, 6): 8, ... і т.д.
edges_data = [
    (1, 4, 4), (1, 3, 2), (1, 6, 8),
    (4, 2, 6), (4, 5, 1),
    (5, 2, 7), (5, 7, 4),
    (2, 6, 6),
    (6, 7, 5), (6, 3, 3), (6, 8, 5),
    (3, 8, 4)
]

# Створення графа
adj_list = {i: [] for i in range(1, num_vertices + 1)}
for u, v, w in edges_data:
    adj_list[u].append((v, w))
    adj_list[v].append((u, w)) # Граф неорієнтований

def dijkstra_algorithm(start_node):
    print(f"n{'='*10} АЛГОРИТМ ДЕЙКСТРИ (Start: {start_node}) {'='*10}")
    
    # 1. Ініціалізація
    distances = {i: INF for i in range(1, num_vertices + 1)}
    predecessors = {i: -1 for i in range(1, num_vertices + 1)}
    distances[start_node] = 0
    
    visited = set()
    
    print(f"{'Крок':<5} | {'Обрана (u)':<10} | {'Distances (1..8)'}")
    print("-" * 60)

    # 2. Основний цикл
    step = 0
    for _ in range(num_vertices):
        # Пошук вершини з мін. відстанню серед невідвіданих
        min_dist = INF
        u = -1
        for i in range(1, num_vertices + 1):
            if i not in visited and distances[i] < min_dist:
                min_dist = distances[i]
                u = i
        
        if u == -1:
            break # Більше немає досяжних вершин
        
        visited.add(u)
        step += 1
        
        # Вивід поточного стану для звіту
        d_str = ", ".join([str(distances[v]) if distances[v] != INF else "inf" for v in range(1, 9)])
        print(f"{step:<5} | {u:<10} | [{d_str}]")
        
        # 3. Релаксація сусідів
        for v, weight in adj_list[u]:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                predecessors[v] = u

    # 4. Вивід результатів
    print("-" * 60)
    print("Результати (Найкоротші шляхи):")
    for v in range(1, num_vertices + 1):
        path = []
        curr = v
        while curr != -1:
            path.append(str(curr))
            curr = predecessors[curr]
        path.reverse()
        
        path_str = " -> ".join(path)
        print(f"До вершини {v}: вага {distances[v]}, шлях: {path_str}")

if __name__ == "__main__":
    dijkstra_algorithm(start_node=1)
