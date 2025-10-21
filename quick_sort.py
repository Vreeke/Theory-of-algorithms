seq = [38, 15, 50, 99, 41, 52, 47, 65, 95]

def quicksort_hoare_with_counts(a):
    counts = {'comparisons': 0, 'assignments': 0}

    def partition(a, l, r):
        pivot = a[(l + r) // 2]
        i = l - 1
        j = r + 1
        while True:
            # рух вліво-направо
            while True:
                i += 1
                counts['comparisons'] += 1
                if a[i] >= pivot:
                    break
            # рух справа-наліво
            while True:
                j -= 1
                counts['comparisons'] += 1
                if a[j] <= pivot:
                    break
            if i >= j:
                return j
            # обмін елементів
            a[i], a[j] = a[j], a[i]
            counts['assignments'] += 2   # дві записи при swap

    def quicksort(a, l, r):
        if l < r:
            p = partition(a, l, r)
            quicksort(a, l, p)
            quicksort(a, p + 1, r)

    quicksort(a, 0, len(a) - 1)
    return a, counts

# Виконання
if __name__ == "__main__":
    sorted_qs, counts_qs = quicksort_hoare_with_counts(seq[:])
    print("АЛГОРИТМ ШВИДКОГО СОРТУВАННЯ (СХЕМА ХОАРА)")
    print("Вхідна послідовність:", seq)
    print("Відсортований масив:", sorted_qs)
    print("comparisons (порівняння):", counts_qs['comparisons'])
    print("assignments (обміни swap):", counts_qs['assignments'])
