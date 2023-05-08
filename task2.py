"""
1. Дано число - сторона квадрата. Рассчитать периметр, площадь и диагональ.
"""
a = 10  # Сторона квадрата
P = a * 4  # Периметр
S = a ** 2  # Площадь
d = 2 ** 0.5 * a  # Диагональ. Еще можно импортировать math и использовать функцию sqrt(),
# но пока проще заменить квадратный корень на возведение 2 в степень 0.5
print(f'1. У квадрата со стороной {a} периметр = {P}, площадь = {S}, диагональ = {d}.\n')
# В конце вывода в каждом задании использую \n, чтобы отделить результаты на выводе.
"""
2. Дано квадратное уравнение (ax)**2+bx+c=0. Дискриминант больше 0. 
Найти корни уравнения и округлить их до 2х знаков после запятой.
"""
a, b, c = 1.7123, 5, 0.3  # Тут не запутаюсь с 1 строкой, хотя можно в 3 строки задать переменные
print(f'2. Исходное уравнение ({a}x)**2 + {b}x + {c} = 0')
D = b ** 2 - 4 * a * c  # Дискриминант, считаем что в данной задаче он всегда и обязательно больше нуля (по условию).
x1 = round((- b + D ** 0.5) / 2 * a, 2)  # Округление до 2-х знаков после запятой
x2 = round((- b - D ** 0.5) / 2 * a, 2)
print(f'Дискриминант D = {D}. Корни уравнения: x1 = {x1}, x2 = {x2 = }\n')

"""
3. Дано 2 строки. Объединить их в 1 строку и разделить пробелом, а также поменять местами первые 2 символа первой строки
 на первые 2 символа второй строки и наоборот.
"""
text1 = 'Печеные пирожки.'
text2 = 'Моченые яблоки.'
print('3.', text1 + ' ' + text2)  # Объединение первоначальных строк
print(text1.replace(text1[:2], text2[:2]) + ' ' + text2.replace(text2[:2], text1[:2]), '\n')  # Для замены берем срез
# по первым 2 символам в строке и подставляем их в другую строку

"""
4. Дан абсолютный путь до файла. Вывести название файла без расширения, название диска и корневую папку.
"""
path_to_file = r'C:\development\pythonProject\name\task2.py'
print('4. Пусть к файлу -', path_to_file)
print('Имя файла -', path_to_file.split('\\')[-1].split('.')[-2])  # Сначала разделим строку по разделителю \,
# используя экранирование, чтобы получить имя файла с расширением, потом разделяем по точкам и берем срез без расширения
# (расширение всегда идет после точки, поэтому разделяем по точкам), \\ - экранирование для \
print('Диск -', path_to_file.split(':')[0])
print('Корневая папка -', path_to_file.split('\\')[1])
print()  # Пустая строка вместо \n

"""
5. Дано 2 числа a и b. С пом. форматирования строк вывести на экран их сумму и произведение в форматах
'a + b = c' и 'a * b = c'.
"""
a = 123.889
b = 14
print(f'5. {a} + {b} = {a + b}')
print(f'{a} * {b} = {a * b}\n')

"""
6. Дана строка. Удалить символы с нечетными индексами.
"""
my_string = 'Принесла кусочек сала, говорит котенок: "Мало! 1-2-3-4-5 !"№№;;%:     ^^^"'
print('6.', my_string)
print(my_string[::2], '\n')  # Срез с шагом 2 выводит только нечетные символы, т.к. нумерация идет с 0

"""
7. Дано 2 строки из неповторяющихся символов. Первая строка длиной 3 символа, вторая произвольная, но содержит символы
первой строки в любом порядке. Вывести срез минимальной длины во второй строке, 
который содержит все символы первой строки.
"""
first_string = 'wtf'
second_string = 'brick quz jmpy veldt whangs fox'
i1 = second_string.find(first_string[0])  # Индекс первого символа из первой строки во второй строке, т.е. w - инд. 21
i2 = second_string.find(first_string[1])  # Индекс второго символа из первой строки во второй строке, т.е. t - инд. 19
i3 = second_string.find(first_string[2])  # Индекс третьего символа из первой строки во второй строке, т.е. f - инд. 27
print('7.', second_string[min(i1, i2, i3):max(i1, i2, i3)+1])  # Срез от минимального индекса до максимального + 1,
# единицу прибавляем, чтобы символ с максимальным индексом тоже попадал в срез