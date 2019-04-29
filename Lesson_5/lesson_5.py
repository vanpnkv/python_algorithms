import collections

# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных
# числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.

company = collections.namedtuple('company', ['name', 'money'])

num = int(input('Введите количество предприятий: '))

corps = []

for i in range(1, num + 1):
    name = input(f'Введите название {i}-го предприятия: ')
    money = 0
    for j in range(1, 5):
        money += (int(input(f"Введите прибыль придприятия {name} за {j} квартал: ")))
    corps.append(company(name=name, money=money/4))

money_average = 0
for i in corps:
    money_average += i.money
money_average /= len(corps)

print(f'Средняя прибыль всех предприятий за год: {money_average}')

rich = []
poor = []
for i in corps:
    if i.money < money_average:
        poor.append(i.name)
    else:
        rich.append(i.name)

print(f'Компании, зарабатывающие ниже среднего: {poor}')
print(f'Компании, зарабатывающие выше среднего: {rich}')
