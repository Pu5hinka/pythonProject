# num = int(input('Введите число'))
# if num % 2==0:
#     print('четное число', num)
# else:
#     print('нечетное число')

# letter = input('Введите текст')
# if letter == 'a' or letter == 'e' or letter == 'i':
#     print('глассная буква')
# elif letter == 'y':
#     print('согласная и гласная')
# else:
#     print('согласная')

# for i in range(0, 11):
#     if i % 2 == 0:
#         print(i, end=' ')

# num = int(input('введи целое число'))
# data = []
# while num != 0:
#     data.append(num)
#     num = int(input('введи целое число'))
# data.sort()
# print(data)

# words = input('введи список слов')
# data = []
# while words != "":
#     if words not in data:
#         data.append(words)
#     words = input()
# for item in data:
#     print(item)
# print(data)

# try:
#     i = int(input('Введите число:\t'))
# except ValueError as e:
#     print('Вы ввели неправильное число')
# else:
#     print(f'Вы ввели {i}')
# finally:
#     print('Выход из программы')
#
# S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
# N = 9
#
# # заводим цикл for, в котором мы будем проходить по всем числам от одного до N
# for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#     print("Значение суммы на предыдущем шаге: ", S)
#     print("Текущее число: ", i)
#     S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
#     print("Значение суммы после сложения: ", S)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: сумма равна = ", S)
#
# letter = input('Введи текст ')
# if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'u':
#     print('буквы гласные')
# elif letter == "y":
#     print("глассная и согласная буква")
# else:
#     print("буква согласная")

# for count in range(0, 11):
#     print(count)
#
# for count in range(0, 11, 2):
#     print(count, end=' ')

# def char_frequency():
#    text = """
#    У лукоморья дуб зелёный;
#    Златая цепь на дубе том:
#    И днём и ночью кот учёный
#    Всё ходит по цепи кругом;
#    Идёт направо -- песнь заводит,
#    Налево -- сказку говорит.
#    Там чудеса: там леший бродит,
#    Русалка на ветвях сидит;
#    Там на неведомых дорожках
#    Следы невиданных зверей;
#    Избушка там на курьих ножках
#    Стоит без окон, без дверей;
#    Там лес и дол видений полны;
#    Там о заре прихлынут волны
#    На брег песчаный и пустой,
#    И тридцать витязей прекрасных
#    Чредой из вод выходят ясных,
#    И с ними дядька их морской;
#    Там королевич мимоходом
#    Пленяет грозного царя;
#    Там в облаках перед народом
#    Через леса, через моря
#    Колдун несёт богатыря;
#    В темнице там царевна тужит,
#    А бурый волк ей верно служит;
#    Там ступа с Бабою Ягой
#    Идёт, бредёт сама собой,
#    Там царь Кащей над златом чахнет;
#    Там русский дух... там Русью пахнет!
#    И там я был, и мёд я пил;
#    У моря видел дуб зелёный;
#    Под ним сидел, и кот учёный
#    Свои мне сказки говорил.
#    """
#
#    text = text.lower()
#    text = text.replace(" ", "")
#    text = text.replace("\n", "")
#
#    count = {}  # для подсчета символов и их количества
#    for char in text:
#        if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#            count[char] += 1
#        else:
#            count[char] = 1
#
#    for char, cnt in count.items():
#        print(f"Символ {char} встречается {cnt} раз")
# char_frequency()

#Напишите функцию print_2_add_2, которая будет складывать 2 и 2, а затем печатать этот результат.
# Не забудьте вызвать функцию, чтобы увидеть результат.

# def print_2_add_2():
#     a = 2 + 2
#     print(a)
#
# print_2_add_2()

#Напишите функцию hello_world, которая будет печать приветственную строку "Hello World".

# def hello_world():
#     text = "Hello World"
#     print(text)
# hello_world()

#Напишите функцию, которая проверяет, является ли число n делителем числа a.
# И выводит на экран соответствующее сообщение, является ли число делителем или нет.

# def check_num(a, n):
#    if a % n == 0:
#        print(f"Число {n} является делителем числа {a}")
#    else:
#        print(f"Число {n} не является делителем числа {a}")
#
# check_num(4, 2)  # Число 2 является делителем числа 4
# check_num(5, 2)  # Число 2 не является делителем числа 5

# def print_1(n):
#     for i in range(n, 0, -1):
#         print("*"* i)
# print_1(6)

#Напишите функцию, которая будет возвращать количество делителей числа а.

#Пример ввода: 5

#Пример вывода программы: 2

# def get_multipliers(a):
#    count = 0
#    for n in range(1, a + 1):
#        if a % n == 0:
#            count += 1
#
#    return count
#
# get_multipliers(5)  # 2
# get_multipliers(4)  # 3

#Напишите функцию, которая проверяет, является ли данная строка палиндромом или нет, и возвращает результат проверки. Пример:

#check_palindrome("test")  # False
#check_palindrome("Кит на море не романтик")  # True

# def check_palindrome(str_):
#    str_ = str_.lower()
#    str_ = str_.replace(" ", "")
#
#    if str_ == str_[::-1]:
#        return True
#    else:
#        return False
#
# check_palindrome("test")  # False
# check_palindrome("Кит на море не романтик")  # True

x = 3


# def func():
#
#    x = 5
#    x += 5
#    print(x)
#    return x
#
#
# print(func())

x = 3


# def func():
#    global x # объявляем, что переменная является глобальной
#    print(x)
#    x = 5
#    x += 5
#    return x
#
#
# func()
# print(x)


# def get_my_func():
#    def hello_world():
#        print("Hello")
#    return hello_world
#
# hello_world_func = get_my_func()  # получить функцию в качестве результата
#
# print(type(hello_world_func))  # <class 'function'>
# hello_world_func()  # Hello


# def count(start=1, step=1):
#     counter = start
#     while True:
#         yield counter
#         counter += step
# print(count)

# def repeat_list(list_):
#    list_values = list_.copy()
#    while True:
#        value = list_values.pop(0)
#        list_values.append(value)
#        yield value
#
# for i in repeat_list([1, 2, 3]):
#    print(i)
#
# def my_decorator(a_function_to_decorate):
#     # Здесь мы определяем новую функцию - «обертку». Она нам нужна, чтобы выполнять
#     # каждый раз при вызове оригинальной функции, а не только один раз
#     def wrapper():
#         # здесь поместим код, который будет выполняться до вызова, потом вызов
#         # оригинальной функции, потом код после вызова
#         print("Я буду выполнен до основного вызова!")
#
#         result = a_function_to_decorate()  # не забываем вернуть значение исходной функции
#
#         print("Я буду выполнен после основного вызова!")
#         return result
#
#     return wrapper
# def my_function():
#    print("Я - оборачиваемая функция!")
#    return 0
#
# print(my_function())
# # Я - оборачиваемая функция!
# # 0
#
# decorated_function = my_decorator(my_function)  # декорирование функции
# print(decorated_function())
# # Я буду выполнен до основного вызова!
# # Я - оборачиваемая функция!
# # Я буду выполнен после основного вызова!
# # 0

#
# import time
#
#
# def decorator_time(fn):
#    def wrapper():
#        print(f"Запустилась функция {fn}")
#        t0 = time.time()
#        result = fn()
#        dt = time.time() - t0
#        print(f"Функция выполнилась. Время: {dt:.10f}")
#        return dt  # задекорированная функция будет возвращать время работы
#    return wrapper
#
#
# def pow_2():
#    return 10000000 ** 2
#
#
# def in_build_pow():
#    return pow(10000000, 2)
#
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
#
# pow_2()
# # Запустилась функция <function pow_2 at 0x7f938401b158>
# # Функция выполнилась. Время: 0.0000011921
#
# in_build_pow()
#
# import time
#
# N = 100
#
#
# def decorator_time(fn):
#    def wrapper():
#        t0 = time.time()
#        result = fn()
#        dt = time.time() - t0
#        return dt
#    return wrapper
#
#
# def pow_2():
#    return 10000000 ** 2
#
#
# def in_build_pow():
#    return pow(10000000, 2)
#
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
#
# mean_pow_2 = 0
# mean_in_build_pow = 0
# for _ in range(N):
#    mean_pow_2 += pow_2()
#    mean_in_build_pow += in_build_pow()
#
# print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
# print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / 100:.10f}")
#
# def linear_solve(a, b):
#     return b/a
# print(linear_solve(2, 9))
# print(linear_solve(0,1))
#
# def linear_solve(a, b):
#     if a:
#         return b/a
#     elif not a and not b: # снова используем числа в логических выражениях
#         return "Бесконечное количество корней"
#     else:
#         return "Нет корней"
# # print(linear_solve(0,1))
# def D(a,b,c):
#     return b**2 - 4*a*c
# def quadratic_solve(a,b,c):
#     if D(a,b,c) < 0:
#         return "Нет вещественных корней"
#     elif D(a,b,c) == 0:
#         return -b/(2*a)
#     else:
#         return (-b-D(a,b,c)**0.5)/(2*a), (-b+D(a,b,c)**0.5)/(2*a)-b/(2*a)
# print(quadratic_solve(1, 8, 4))
# print(type(D))


# def min_list(L):
#     if len(L) == 1:
#         return L[0]
#     return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])
# print(min_list([2, 3, 5]))


