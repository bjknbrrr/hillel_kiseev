num = int(input('Please enter a number: '))

print('Your number:', num)

dig1 = num % 10
dig2 = num // 10 % 10
dig3 = num // 100

print(dig1, dig2, dig3)

num1 = dig1 * 100 + dig2 * 10 + dig3
print('Result:', num1)

print('Result1:', num % 10 * 100 + num // 10 % 10 * 10 + num // 100)
