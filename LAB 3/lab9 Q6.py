def sum_of_list(L):
    if not L:
        return 0
    else:
        return L[0] + sum_of_list(L[1:])
result = sum_of_list([2, 3, 5, 7])
print(result)