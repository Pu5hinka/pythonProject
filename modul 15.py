# myFile = open('nameFile.txt', 'w')
# myFile.write('ttt')
# print('zzz', file=myFile)
#Задача: пользователь вводит произвольное целое число, а программа читает некий русский текст из файла
# и зашифровывает его в другой файл со сдвигом, соответствующим этому числу.
# alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# alphaUp = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# number = int(input('Введите число, на которое нужно сдвинуть текст: '))
#
# summary = ''
#
#
# def changeChar(char):
#     if char in alpha:
#         return alpha[(alpha.index(char) + number) % len(alpha)]
#     elif char in alphaUp:
#         return alphaUp[(alphaUp.index(char) + number) % len(alphaUp)]
#     else:
#         return char
#
#
# with open("filename2.txt", encoding="utf8") as myFile:
#     for line in myFile:
#         for char in line:
#             summary += changeChar(char)
#
# with open("output.txt", 'w', encoding="utf8") as myFile:
#     myFile.write(summary)
#
# def found(pathArr, finPoint):
#     weight = 1
#     for i in range(len(pathArr) * len(pathArr[0])):
#         for y in range(len(pathArr)):
#             for x in range(len(pathArr[y])):
#                 if pathArr[y][x] == weight:
#                     # Вниз
#                     if y > 0 and pathArr[y - 1][x] == 0:
#                         pathArr[y - 1][x] = weight + 1
#
#                         # Вверх
#                     if y < (len(pathArr) - 1) and pathArr[y + 1][x] == 0:
#                         pathArr[y + 1][x] = weight + 1
#
#                     # Вправо
#                     if x > 0 and pathArr[y][x - 1] == 0:
#                         pathArr[y][x - 1] = weight + 1
#
#                     # Влево
#                     if x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == 0:
#                         pathArr[y][x + 1] = weight + 1
#
#                     # Конечная точка
#                     if (abs(y - finPoint[0]) + abs(x - finPoint[1])) == 1:
#                         pathArr[finPoint[0]][finPoint[1]] = weight + 1
#                         return True
#         weight += 1
#     return False
#
#
# def printPath(pathArr, finPoint):
#     y = finPoint[0]
#     x = finPoint[1]
#     weight = pathArr[y][x]
#     result = list(range(weight))
#     while (weight):
#         weight -= 1
#         if y > 0 and pathArr[y - 1][x] == weight:
#             result[weight] = 'Вниз'
#             y -= 1
#         elif y < (len(pathArr) - 1) and pathArr[y + 1][x] == weight:
#             result[weight] = 'Вверх'
#             y += 1
#         elif x > 0 and pathArr[y][x - 1] == weight:
#             result[weight] = 'Вправо'
#             x -= 1
#         elif x < (len(pathArr[y]) - 1) and pathArr[y][x + 1] == weight:
#             result[weight] = 'Влево'
#             x += 1
#
#     return result[1:]
#
#
# labirint = []
# with open("labirint.txt") as myFile:
#     for line in myFile:
#         labirint.append(line.replace('\n', '').split(' '))
#
# ii = 0
# for i in labirint:
#     jj = 0
#     for j in i:
#         if j == 'A':
#             labirint[ii][jj] = 1
#             pozIn = (ii, jj)
#         elif j == 'B':
#             labirint[ii][jj] = 0
#             pozOut = (ii, jj)
#         elif j == '1':
#             labirint[ii][jj] = -1
#         else:
#             labirint[ii][jj] = 0
#         jj += 1
#     ii += 1
#
# if not found(labirint, pozOut):
#     print("Путь не найден!")
# else:
#     result = printPath(labirint, pozOut)
#
#     for i in labirint:
#         for line in i:
#             print("{:^3}".format(line), end=" ")
#         print()
#     print(result)

# myfile = open('hello.txt', 'r')
# file = myfile.read()
# print(file)
# myfile.close()
#
# try:
#     somefile = open('hello1.txt', 'w')
#     try:
#         somefile.write('hello, msdfoiu')
#     except Exception as e:
#         print(e)
#     finally:
#         somefile.close()
# except Exception as ex:
#     print(ex)
#
# with open('hello2.txt', 'w') as somefile:
#     somefile.write('iushgesidgj')

# with open('text.txt', 'a') as file:
#     file.write('\nkak dela>')

# with open('12.7.3.txt') as f:
#     a = f.readline()
#     print(a)

# with open('17.txt') as f:
#     a = f.readlines()
#     b = list(map(int, a))
#     print(b)
#
# with open('17.txt') as f:
#     s = f.readlines()
#     a = list(map(int, s))
#     res = []
#     for i in a:
#         if str(i).count('0') >= 2 and i % 7 == 0:
#             res.append(i)
# print(max(res), len(res))

# with open('17-205.txt') as f:
#     s = [int(x) for x in f]
#     res = []
#     for i in range(1, len(s)):
#         if (abs(s[i]) % 10 == 7 or abs(s[i-1]) % 10 ==7) and (s[i] + s[i-1]) % 12 == 0:
#             res.append(s[i] + s[i-1])
# print(len(res), max(res))
