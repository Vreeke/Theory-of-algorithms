# Клас для системи неперетинних множин (DSU)
class DSU:
    def __init__(self, n):
        # Спочатку кожна вершина є батьком сама собі
        self.parent = list(range(n + 1))

    # Знайти представника множини (з компресією шляху)
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    # Об'єднати дві множини
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        
        # Якщо корені різні — об'єднуємо і повертаємо True
        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        # Якщо корені однакові — це цикл, повертаємо False
        return False

def kruskal_algorithm():
    # === ВХІДНІ ДАНІ (ВАРІАНТ 1) ===
    num_vertices = 8
    edges_data = [
        (1, 4, 4), (1, 3, 2), (1, 6, 8),
        (4, 2, 6), (4, 5, 1),
        (5, 2, 7), (5, 7, 4),
        (2, 6, 6),
        (6, 7, 5), (6, 3, 3), (6, 8, 5),
        (3, 8, 4)
    ]

    print(f"\n{'='*10} АЛГОРИТМ КРУСКАЛА {'='*10}")
    
    # 1. Сортуємо ребра за зростанням ваги
    # x[2] — це вага w у кортежі (u, v, w)
    sorted_edges = sorted(edges_data, key=lambda x: x[2])
    
    dsu = DSU(num_vertices)
    mst_weight = 0
    mst_edges = []

    print(f"{'Ребро':<10} | {'Вага':<5} | {'Дія'}")
    print("-" * 30)

    # 2. Проходимо по відсортованих ребрах
    for u, v, w in sorted_edges:
        # Якщо вершини в різних множинах — додаємо ребро
        if dsu.union(u, v):
            print(f"({u} - {v}):   | {w:<5} | Додано")
            mst_weight += w
            mst_edges.append((u, v, w))
        else:
            # Якщо вершини вже в одній множині — пропускаємо (щоб не було циклу)
            # print(f"({u} - {v}):   | {w:<5} | Пропущено")
            pass

    print("-" * 30)
    print(f"Загальна вага МКД: {mst_weight}")
    print(f"Список ребер МКД: {mst_edges}")

if __name__ == "__main__":
    kruskal_algorithm()
