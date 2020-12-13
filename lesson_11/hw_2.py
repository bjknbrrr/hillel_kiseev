from string import ascii_uppercase
from string import digits

src = digits + ascii_uppercase
# print(src)


def converter(num, system):
    res_str = []
    while num:
        res_str.insert(0, src[num % system])
        num //= system

    res_str = ''.join(res_str)
    return res_str


n = int(input('Please enter a number: '))
s = int(input('Please enter system: '))

r = converter(n, s)
print('Result:', r)
