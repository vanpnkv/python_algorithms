# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Для выполнения я взял код из предыдущего урока для хранения информации о компаниях

import sys
import collections


class CompanyClass:
    def __init__(self, name, money):
        self.name = name
        self.money = money


class CompanyClassSlots:
    __slots__ = 'name', 'money'

    def __init__(self, name, money):
        self.name = name
        self.money = money


company_namedtuple = collections.namedtuple('company', 'name money')

company_map = {'name': 'Company', 'money': 1000.5}

print(f'CompanyClass занимает {sys.getsizeof(CompanyClass("Company", 1000.5))} байт в памяти')
print(f'CompanyClassSlots занимает {sys.getsizeof(CompanyClassSlots("Company", 1000.5))} байт в памяти')
print(f'company_namedtuple занимает {sys.getsizeof(company_namedtuple("Company", 1000.5))} байт в памяти')
print(f'company_map занимает {sys.getsizeof(company_map)} байт в памяти')

# Мои результаты несколько разнятся с примерами, которые были даны на уроке
# python версии 3.7.3, x86_64 архитектура
# Вывод на моей машине:
# CompanyClass занимает 56 байт в памяти
# CompanyClassSlots занимает 56 байт в памяти
# company_namedtuple занимает 64 байт в памяти
# company_map занимает 240 байт в памяти
#
# У меня почему-то никакого влияния не оказал атрибут __slots__
# Словарь занимает слишком много памяти
