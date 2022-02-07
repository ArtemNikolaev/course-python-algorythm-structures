# https://github.com/ArtemNikolaev/course-python-algorythm-structures/issues/14
# В программе генерируется случайное целое число от 0 до 100. Пользователь должен
# его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно
# сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести ответ.
from math import ceil
from random import randint

n = randint(0, 101)
count = 0
fromV = 0
toV = 100
result = -1
steps = []

while (result !=n):
    count += 1
    result = fromV + ceil((toV - fromV) / 2)
    steps.append(result)
    if result < n:
        fromV = result
    if result > n:
        toV = result

print(f'Число {n} найдено за {count} шагов: {steps}')
