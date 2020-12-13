# while True:
#     try:
#         a = int(input('Please enter first number: '))
#         if a == 0:
#             break
#         b = int(input('Please enter second number: '))
#         print(a / b)
#     except ZeroDivisionError:
#         print('Попытка деленияна ноль')
#     except ValueError:
#         print('Неверные входные данные')
#     else:
#         print('Ошибок нет!')


# finally
file = None
try:
    file = open('test.txt')
    file.write('Some text')
    # file.close()
except Exception as ex:
    print('error', ex)
finally:
    print('Finally')
    if not file:
        file.close()

