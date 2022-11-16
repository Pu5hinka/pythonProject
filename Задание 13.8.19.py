ticket = int(input('Введите количество билетов, которые хотите приобрести: '))
cost = 0.0
for i in range(ticket):
    age = int(input('Введите возраст посетителя конференции: '))
    if age < 18:
        cost = cost + 0
    elif 25 <= age <= 18:
        cost = cost + 990
    else:
        cost = cost + 1390
if ticket >= 3:
    cost = cost * 0.9
print('Итого к оплате:' + ' ' + str(round(cost)) + ' ' + 'рублей')