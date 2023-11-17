def count_items(L):
    if not L:
        return 0
    else:
        return 1 + count_items(L[1:])
result = count_items([2, 3, 5, 7])
print(result)
