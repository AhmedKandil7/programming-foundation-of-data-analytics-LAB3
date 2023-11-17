def sum_of_series(N):
    if N == 1:
      return 1
    else:
      return N ** 2 + sum_of_series(N - 1)
result = sum_of_series(5)
print(result)
