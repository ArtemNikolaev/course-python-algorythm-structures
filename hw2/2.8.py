# https://github.com/ArtemNikolaev/course-python-algorythm-structures/issues/16
# Посчитать, сколько раз встречается определенная цифра в введенной последовательности
# чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются
# вводом с клавиатуры.

n = int(input('Введите число: '))
digit = int(input('Введите искомую цифру: '))
count = 0

while n > 0:
    lastDigit = n % 10
    n = n // 10
    if lastDigit == digit:
        count += 1

print(f'Цифра встречается {count} раз!')
