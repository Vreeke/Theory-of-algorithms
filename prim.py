import heapq

def prim_algorithm():
    # ВХІДНІ ДАНІ
    # Кількість вершин
    num_vertices = 8
    
    # Список ребер: (u, v, weight)
    # Граф неорієнтований, тому тут ми просто описуємо зв'язки
    edges_data = [
        (1, 4, 4), (1, 3, 2), (1, 6, 8),
        (4, 2, 6), (4, 5, 1),
        (5, 2, 7), (5, 7, 4),
        (2, 6, 6),
        (6, 7, 5), (6, 3, 3), (6, 8, 5),
        (3, 8, 4)
    ]

    # Перетворюємо список ребер на список суміжності
    adj = {i: [] for i in range(1, num_vertices + 1)}
    for u, v, w in edges_data:
        adj[u].append((w, v))
        adj[v].append((w, u))

    mst_weight = 0
    mst_edges = []
    visited = set()
    
    # Починаємо з вершини 1
    start_node = 1
    
    # Черга пріоритетів (min-heap): (вага, з_вершини, у_вершину)
    # Початкове значення: вага 0, батька немає (-1), поточна вершина start_node
    min_heap = [(0, -1, start_node)]
    
    print(f"\n{'='*10} АЛГОРИТМ ПРІМА {'='*10}")
    print(f"{'Крок':<5} | {'Обране ребро':<15} | {'Вага'}")
    print("-" * 35)

    step = 0
    
    while min_heap:
        weight, u, v = heapq.heappop(min_heap)

        if v in visited:
            continue

        visited.add(v)
        
        # Якщо u != -1, це не перша (стартова) вершина, отже ми пройшли по ребру
        if u != -1:
            step += 1
            mst_weight += weight
            mst_edges.append((u, v, weight))
            print(f"{step:<5} | ({u} - {v}):{' '*7} | {weight}")

        # Додаємо всіх сусідів поточної вершини до черги
        for neighbor_weight, neighbor in adj[v]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (neighbor_weight, v, neighbor))

    print("-" * 35)
    print(f"Загальна вага МКД: {mst_weight}")
    print(f"Список ребер МКД: {mst_edges}")

if __name__ == "__main__":
    prim_algorithm()
