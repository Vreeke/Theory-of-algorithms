def insertion_sort(a):
    n = len(a)
    comparisons = 0
    assignments = 0

    for i in range(1, n):
        key = a[i]
        assignments += 1  # key = a[i]
        j = i - 1
        assignments += 1  # j = i-1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                assignments += 1
                j -= 1
                assignments += 1
            else:
                break
        a[j + 1] = key
        assignments += 1
        print(f"Insertion i={i}: {a}")

    return a, comparisons, assignments


if __name__ == "__main__":
    arr = [38, 15, 50, 99, 41, 52, 47, 65, 95]
    arr_copy = arr.copy()
    print("=== Insertion Sort ===")
    res, cmp, asg = insertion_sort(arr_copy)
    print("Відсортований:", res)
    print("Порівнянь:", cmp, "Присвоєнь:", asg)
