
def quicksort_rec(ls, i, j):
    if i >= j:
        return

    p_index = j
    p_val = ls[j]

    for k in reversed(range(i, j)):
        if ls[k] > p_val:
            ls[p_index] = ls[k]
            p_index -= 1
            ls[k] = ls[p_index]
    ls[p_index] = p_val
    quicksort_rec(ls, i, p_index - 1)
    quicksort_rec(ls, p_index + 1, j)

def quicksort(ls):
    quicksort_rec(ls, 0, len(ls) -1)

ls = [1, 6, 3, 9, 2, 7, 4, 10, 5, 8]
quicksort(ls)
print ls