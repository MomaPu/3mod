# уровень 1
x = int(input('Введите сумму вклада: '))
p = (int(input('Введите ежегодный %: ')))/100 # Получаем проценты для счета
y = int(input('Введите конечную сумму вклада: '))
years = 0 # Счетчик кол-ва лет вклада
while x < y:
	x += x*p
	years += 1
print(years)


# уровень 2
n = int(input('Введите значение n: ')) 
while n > 0:
	print('for - частный случай цикла while') 
	n -= 1

# уровень 3
chislo = input('Введите число: ')
summa = 0 # создаем переменну подсчета 
for i in chislo: 
	summa += int(i)
print(summa)
