# уровень 1
work = 10 # пользователь заполнит список из 10 значений
sp = []
povt = [] # создаем список повторяющихся
while work > 0: 
	a = input('Введите любое значение: ')
	sp.append(a)
	work -= 1
for a in sp: # поиск повторяющихся
	if sp.count(a) > 1:
		povt.append(a)  
print(set(povt)) # вывод только повторяющихся 

# уровень 2
from random import randint

n = 5
m = [[randint(0,100) for i in range(n)] for j in range(n)] # генерация матрицы

maximum = 0 # задаем переменную максимума
for a in m: # берем каждый список
	if max(a) > maximum: # находим среди него максимум и сравниваем
		maximum = max(a)
print(maximum) # вывод максимума


# уровень 3
d = {'auto': 'audi', 'plane': 'mig', 'helicopter': 'mi'}
print({v:k for k, v in d.items()})

