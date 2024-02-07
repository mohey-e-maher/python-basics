# ------------------------------------------------------
# 3 - Fill an array of 5 elements from the user, Sort it in descending and
# ascending orders then display the output
# ------------------------------------------------------

arr = []
for i in range(0,5):
    arr.append(int(input()))
print(arr)
arr.sort()
print(arr)
print(arr[::-1])