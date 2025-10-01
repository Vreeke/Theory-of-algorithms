def selection_sort(a):
    n = len(a)
    comparisons = 0
    assignments = 0

    for i in range(n - 1):
        min_index = i
        assignments += 1  # min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_index]:
                min_index = j
                assignments += 1  # min_index change
        comparisons += 1  # if min_index != i
        if min_index != i:
            # swap
            a[i], a[min_index] = a[min_index], a[i]
            assignments += 3  # swap = 3 assignments
        print(f"Selection i={i}: {a}")

    return a, comparisons, assignments


if __name__ == "__main__":
    arr = [38, 15, 50, 99, 41, 52, 47, 65, 95]
    arr_copy = arr.copy()
    print("=== Selection Sort ===")
    res, cmp, asg = selection_sort(arr_copy)
    print("Відсортований:", res)
    print("Порівнянь:", cmp, "Присвоєнь:", asg)
