A_orig = [38, 15, 50, 99, 41, 52, 47, 65, 95]

comparisons = 0
assignments = 0

def dbg_print(step, arr):
    """Друкує короткий опис кроку та масив."""
    print(f"{step}: {arr}")

def swap(arr, i, j):
    global assignments
    temp = arr[i]
    arr[i] = arr[j]; assignments += 1
    arr[j] = temp; assignments += 1
    print(f"  swap indices {i} <-> {j} -> {arr[i]} <-> {arr[j]}")

def sink(arr, i, n, trace_tag=""):
    global comparisons, assignments
    k = i
    while True:
        j = 2 * k + 1  # лівий син (index)
        if j >= n:
            break
        if j + 1 < n:
            comparisons += 1
            if arr[j + 1] > arr[j]:
                j = j + 1
        comparisons += 1
        if arr[k] >= arr[j]:
            break
        swap(arr, k, j)
        k = j

def heapsort_with_trace(arr):
    global comparisons, assignments
    n = len(arr)
    print("Початковий масив:", arr.copy())
    print("\n--- Фаза 1: Побудова максимальної купи ---")
    for i in range(n // 2 - 1, -1, -1):
        print(f"\nПеред Sink(i={i}): {arr}")
        sink(arr, i, n, trace_tag=f"heapify i={i}")
        print(f"Після Sink(i={i}): {arr}")

    print("\nМасив після побудови max-купи:", arr)
    print("\n--- Фаза 2: Сортування ---")
    for i in range(n - 1, 0, -1):
        print(f"\nКрок сортування: обмін root (індекс 0) з індексом {i}")
        swap(arr, 0, i)
        print(f"Після swap: {arr} (елемент на індексі {i} вважається відсортованим)")
        sink(arr, 0, i, trace_tag=f"sort step i={i}")
        print(f"Після sink(size={i}): {arr}")

    print("\nВідсортований масив:", arr)
    print("\n--- Підрахунок операцій ---")
    print(f"Порівнянь між елементами: {comparisons}")
    print(f"Присвоєнь у масиві (записів arr[...] = ...): {assignments}")

A = A_orig.copy()
heapsort_with_trace(A)
