import collections


a = {1, 2, 3, 1, 1, 4} #set
print(a)
print(type(a))

b = (1, 2, 3, 4, 5, 1) #tuple
print(b)
print(type(b))

c = [1, 2, 3, 3, 2, 1] #list
c.sort()
print(c)
print(type(c))

d = {'Russia': 'Moscow', 'Kazakhstan': 'Nursultan'} #dict
print(d['Kazakhstan'])
print(type(d))

# e = collections.deque([1, 2, 3, 4, 5]) #deque
# print(a)
# print(type(e))

company = collections.namedtuple('company', ['name', 'money'])

num = int(input('Введите количество предприятий: '))

corps = []

for i in range(1, num + 1):
    name = input(f'Введите название {i}-го предприятия: ')
    money = []
    for j in range(1, 5):
        money.append(int(input(f"Введите прибыль придприятия {name} за {j} квартал: ")))
   corps.append(company(name, money[0], money[1], money[2], money[3]))

print(corps)

