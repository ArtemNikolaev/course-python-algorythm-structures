# https://github.com/ArtemNikolaev/course-python-algorythm-structures/issues/8
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

values = ['a', 'b', 'c']

for i in range(0, len(values)):
    values[i] = int(input('Введите ' + values[i] + ': '))

print(sum(values) - min(values) - max(values))
