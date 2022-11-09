
x = 0.1
y = 21.5
e = x - y
print(e)
print(type(x))
# <class 'float'>
print(type(y))
# <class 'float'>
print(type(e))
z = y / x
print(z)
print(type(z))
print (0.1+0.1*5-0.3*4)
print ((3.14+0.3)/2+0.15)

a = -13
b = 7

a = a - b
b = a + b

print(b)
print(a)

introducing = "I'm Ivan"
action = 'Я читаю "Изучаем python" Марка Лутца'
print(action, ',', introducing)



long_text = '''Здесь может
               находиться
               большой "кусок" кода'''
other_long_text = """Таким образом тоже
                     можно записать"""

print(long_text)
print(other_long_text)

s = "python"
print(s[0])
# p
print(s[1:4])
# yth

t = True
f = False
print(3 > 10)
# False

print(3 < 10)
# True

print(3 == 10)
# равны ли объекты?
# False
print('r' in 'world') # проверяем отдельный символ
# True

print('th' in 'python') # проверяем целую подстроку
# True

print('the' in 'python')
# False
print(1.57*3/1.5==3.14)
print('PY'in"Python")

date = (1, 'january', 2022)
print(date[0])
# 1
print(date[1])
# january
print(date[2])

s1 = "foo"
s2 = "bar"
s1 = s1+s2
print(s1)
s1 = "foo"
print(id(s1), s1) #проверяем идентификатор
# 139953609727144, foo

s2 = "bar"
print(id(s2), s2) #проверяем идентификатор
# 139953609727088, bar

s1 = s1+s2
print(id(s1), s1) #проверяем идентификатор
# 139953459591296, foobar

a = 5/2
print(a)
print(1 % 3)
print (31 % 2 + 31 % 2)
print (13 % 3 * 3 - 3**2)

f = 653
g = 123
print(f**g)
print(a**100)
print(round(11*2.5/3, 2))
pi=3.14159
print(round(pi**2/2))
colors = 'red blue green'

print(colors.split())
path = '/home/user/documents/file.txt'

print(path.split('/')) # разделитель можно указать в качестве аргумента
# ['', 'home', 'user', 'documents', 'file.txt']

pi = 31.4159265
print ("%.4e" % (pi))

s = 0, 'hello', (1, 'a')
print(s)

spisok = input("Введите числа через пробел:")

list_of_spisok = spisok.split() # список строковых представлений чисел
arr = list(map(int, list_of_spisok)) # список чисел
print(arr)
arr[0], arr[-1] = arr[-1], arr[0]
print(arr)
arr.append(sum(arr))
print(arr) # sum() вычисляет сумму элементов списка


