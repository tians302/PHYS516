def quicksort(a):
    if len(a) <=1 :
        return a
    pivot = a[len(a) // 2]

    left = []
    right = []
    center = []

    for x in a:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            center.append(x)
        else:
            right.append(x)

    return quicksort(left) + center + quicksort(right)

example = [9, 6, 1, 9, 16, 2, 5]
print(quicksort(example))
