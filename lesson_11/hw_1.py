from random import randint

lst = [randint(10, 50) for _ in range(20)]
print(lst)

for i in range(len(lst) // 2):
    lst[i], lst[len(lst)-1-i] = lst[len(lst)-1-i], lst[i]

print(lst)
