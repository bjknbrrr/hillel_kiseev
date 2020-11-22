h = int(input('Please enter height: '))     # 5

i = 0
while i < h:
    j = 0
    while j < h * 2:
        if h - 1 - i <= j <= h - 1 + i:
            print('* ', end='')
        else:
            print('  ', end='')
        j += 1
    print()
    i += 1
print()
