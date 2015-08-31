
def mergesort(ls):
    if len(ls) <= 1:
        return ls
    else:
        midpoint = len(ls) / 2
        ls_a = mergesort(ls[:midpoint])
        ls_b = mergesort(ls[midpoint:])
        a = 0
        b = 0
        out = []
        while a < len(ls_a) and b < len(ls_b):
            if ls_a[a] < ls_b[b]:
                out.append(ls_a[a])
                a += 1
            else:
                out.append(ls_b[b])
                b += 1
        out.extend(ls_a[a:])
        out.extend(ls_b[b:])
        return out

print mergesort([1, 6, 3, 9, 2, 7, 4, 10, 5, 3])