from random import randint

lst1 = [0] * 20
print(lst1)

rows = 10
cols = 12

lst2 = [[randint(10, 99) for _ in range(cols)] for _ in range(rows)]
print(lst2)

for i in range(rows):
    for j in range(cols):
        print(lst2[i][j], end=' ')
    print()
