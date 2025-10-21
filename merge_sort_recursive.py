seq = [38, 15, 50, 99, 41, 52, 47, 65, 95]

def mergesort_recursive_with_counts(arr):
    counts = {'comparisons': 0, 'assignments': 0}

    def merge(left, right):
        i = 0
        j = 0
        res = []
        while i < len(left) and j < len(right):
            counts['comparisons'] += 1
            if left[i] <= right[j]:
                res.append(left[i])
                counts['assignments'] += 1
                i += 1
            else:
                res.append(right[j])
                counts['assignments'] += 1
                j += 1
        while i < len(left):
            res.append(left[i])
            counts['assignments'] += 1
            i += 1
        while j < len(right):
            res.append(right[j])
            counts['assignments'] += 1
            j += 1
        return res

    def sort(a):
        if len(a) <= 1:
            return a
        mid = len(a) // 2
        L = sort(a[:mid])
        R = sort(a[mid:])
        return merge(L, R)

    sorted_arr = sort(arr)
    return sorted_arr, counts

# Виконання
if __name__ == "__main__":
    sorted_rec, counts_rec = mergesort_recursive_with_counts(seq[:])
    print("РЕКУРСИВНИЙ Merge Sort")
    print("Вхідна послідовність:", seq)
    print("Відсортований масив:", sorted_rec)
    print("comparisons (порівняння):", counts_rec['comparisons'])
    print("assignments (записи у результуючі списки):", counts_rec['assignments'])
