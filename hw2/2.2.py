# https://github.com/ArtemNikolaev/course-python-algorythm-structures/issues/10
# Посчитать четные и нечетные цифры введенного натурального числа. Например,
# если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

n = int(input('Bведите n: '))
even = 0
odd = 0

while n > 0:
    value = n % 10
    n = n // 10

    if value % 2 == 0:
        even += 1
    else:
        odd += 1

print('Четные: ', even, '\nНечетные: ', odd)
