# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input('Введите трехзначное число:'))
summ = 0
if abs(n) < 100:
    print(f'{n} это не трехзначное число')
else:
    while abs(n) > 0:
        x = abs(n) % 10
        summ = summ + x
        n = abs(n) // 10
    print(summ) 