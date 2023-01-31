# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

ticketNumber = int(input('Введите шестизначный номер билета: '))
firstThreeNumbers = 0
secondThreeNumbers = 0
summFirstThreeNumbers = 0
summSecondThreeNumbers = 0

if 99999 < ticketNumber < 1000000:
    firstThreeNumbers = ticketNumber // 1000
    secondThreeNumbers = ticketNumber % 1000
    while firstThreeNumbers > 0 and secondThreeNumbers > 0:
        x = firstThreeNumbers % 10
        summFirstThreeNumbers = summFirstThreeNumbers + x
        firstThreeNumbers = firstThreeNumbers // 10
        y = secondThreeNumbers % 10
        summSecondThreeNumbers = summSecondThreeNumbers + y
        secondThreeNumbers = secondThreeNumbers // 10
    if summFirstThreeNumbers == summSecondThreeNumbers:
        print(f'{ticketNumber} -> yes')
    else:
        print(f'{ticketNumber} -> no')
else:
    print('Вы ввелли некорретное число')
   
        
