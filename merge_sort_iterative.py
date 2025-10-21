seq = [38, 15, 50, 99, 41, 52, 47, 65, 95]

def mergesort_iterative_with_counts(arr):
    a = arr[:]  # робоча копія
    n = len(a)
    counts = {'comparisons': 0, 'assignments': 0}
    width = 1
    while width < n:
        left = 0
        while left < n:
            mid = min(left + width, n)
            right = min(left + 2 * width, n)
            # якщо підмасивів для злиття немає — пропускаємо
            if mid >= right:
                left += 2 * width
                continue
            i = left
            j = mid
            temp = []
            while i < mid and j < right:
                counts['comparisons'] += 1
                if a[i] <= a[j]:
                    temp.append(a[i])
                    counts['assignments'] += 1
                    i += 1
                else:
                    temp.append(a[j])
                    counts['assignments'] += 1
                    j += 1
            while i < mid:
                temp.append(a[i])
                counts['assignments'] += 1
                i += 1
            while j < right:
                temp.append(a[j])
                counts['assignments'] += 1
                j += 1
            # копіювання назад у масив a
            for k, val in enumerate(temp):
                a[left + k] = val
                counts['assignments'] += 1
            left += 2 * width
        width *= 2
    return a, counts

# Виконання
if __name__ == "__main__":
    sorted_it, counts_it = mergesort_iterative_with_counts(seq[:])
    print("ІТЕРАТИВНИЙ (bottom-up) Merge Sort")
    print("Вхідна послідовність:", seq)
    print("Відсортований масив:", sorted_it)
    print("comparisons (порівняння):", counts_it['comparisons'])
    print("assignments (записи у temp та копіювання назад):", counts_it['assignments'])
