import sys

#ВХІДНІ ДАНІ
INF = float('inf')
num_vertices = 8

edges_data = [
    (1, 4, 4), (1, 3, 2), (1, 6, 8),
    (4, 2, 6), (4, 5, 1),
    (5, 2, 7), (5, 7, 4),
    (2, 6, 6),
    (6, 7, 5), (6, 3, 3), (6, 8, 5),
    (3, 8, 4)
]

def print_matrix(matrix, title="Matrix"):
    print(f"\n{title}:")
    print("   ", end="")
    for i in range(1, len(matrix)): 
        print(f"{i:4}", end="")
    print("\n" + "-" * (4 * len(matrix) + 3))
    
    for i in range(1, len(matrix)):
        print(f"{i} |", end="")
        for j in range(1, len(matrix)):
            val = matrix[i][j]
            if val == INF: val = "Inf"
            print(f"{val:4}", end="")
        print()

def floyd_warshall_algorithm():
    print(f"\n{'='*10} АЛГОРИТМ ФЛОЙДА-ВОРШЕЛЛА {'='*10}")

    # 1. Ініціалізація матриці D0
    # Розмір (n+1)x(n+1) для зручності індексації з 1
    dist_matrix = [[INF] * (num_vertices + 1) for _ in range(num_vertices + 1)]
    
    for i in range(1, num_vertices + 1):
        dist_matrix[i][i] = 0
        
    for u, v, w in edges_data:
        dist_matrix[u][v] = w
        dist_matrix[v][u] = w # Граф неорієнтований

    print_matrix(dist_matrix, "Початкова матриця D(0)")

    # 2. Основний цикл алгоритму
    # k - проміжна вершина
    for k in range(1, num_vertices + 1):
        for i in range(1, num_vertices + 1):
            for j in range(1, num_vertices + 1):
                # Формула Флойда: D[i][j] = min(D[i][j], D[i][k] + D[k][j])
                if dist_matrix[i][k] != INF and dist_matrix[k][j] != INF:
                    dist_matrix[i][j] = min(dist_matrix[i][j], dist_matrix[i][k] + dist_matrix[k][j])

    # 3. Вивід фінальної матриці
    print_matrix(dist_matrix, f"Фінальна матриця найкоротших шляхів D({num_vertices})")

if __name__ == "__main__":
    floyd_warshall_algorithm()
