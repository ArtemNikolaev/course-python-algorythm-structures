# https://github.com/ArtemNikolaev/course-python-algorythm-structures/issues/10
# Посчитать четные и нечетные цифры введенного натурального числа. Например,
# если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

n = int(input('Bведите n: '))
result = ''

while n > 0:
    result += str(n % 10)
    n = n // 10

print(result)
