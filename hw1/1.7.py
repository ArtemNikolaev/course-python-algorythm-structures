# https://github.com/ArtemNikolaev/course-python-algorythm-structures/issues/7
# Определить, является ли год, который ввел пользователь, високосным или не високосным.

year = int(input('Введите год: '))

print(True if year % 4 == 0 else False)
