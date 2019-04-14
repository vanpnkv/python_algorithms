# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь. 
num = ''
while len(num) != 3:
    num = input("Введите трехзначое число: ")
    if num.isdigit() is False:
        num = ''
        continue
a = 0
b = 1
for i in num:
    a += int(i)
    b *= int(i)
print(f"Произведение равно {b}, сумма равна {a}")

# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
x1 = int(input("Введите координату x первой точки: "))
y1 = int(input("Введите кооринату y первой точки: "))
x2 = int(input("Введите координату x второй точки: "))
y2 = int(input("Введите кооринату y второй точки: "))

k = (y2 - y1) / (x2 - x1)
b = y1 - k * x1

print(f'y = {k}x + {b}')

# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
english_alphabet = 'abcdefghijklmnopqrstuvwxyz'

a = ''
b = ''
while len(a) != 1:
    a = input("Введите первую букву")
    if a.isalpha() is False:
        a = ''
        continue
while len(b) != 1:
    b = input("Введите вторую букву")
    if b.isalpha() is False:
        b = ''
        continue

i = 0
k = 0
j = 0

a = a.lower()
b = b.lower()

for word in russian_alphabet:
    i += 1
    if a == word:
        j = i
        print(f"Буква {a} - {j} по счету")
    if b == word:
        k = i
        print(f"Буква {b} - {k} по счету")

if (k != 0) and (j != 0):
    m = abs(j - k) - 1
    if m >= 0:
        print(f"Между буквой {a} и буквой {b} {m} символов")
    else:
        print(f"Это одна и та же буква")

i = 0
k = 0
j = 0
for word in english_alphabet:
    i += 1
    if a == word:
        j = i
        print(f"Буква {a} - {j} по счету")
    if b == word:
        k = i
        print(f"Буква {b} - {k} по счету")

if (k != 0) and (j != 0):
    m = abs(j - k) - 1
    if m >= 0:
        print(f"Между буквой {a} и буквой {b} {m} символов")
    else:
        print(f"Это одна и та же буква")
elif k != j:
    print("Буквы из разных алфавитов")

# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
while True:
    a = input("Введите номер буквы")
    if a.isdigit() is False:
        a = ''
        continue
    else:
        break

a = int(a)
if a < 27:
    print(f"Номер {a} - буква {russian_alphabet[a - 1]} в русском и {english_alphabet[a - 1]} в английском алфавите")
elif a < 34:
    print(f"Номер {a} - буква {russian_alphabet[a - 1]} в русском алфавите")
else:
    print(f"Буквы под таким номерм не существует")


# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
a = ''
while len(a) != 4:
    a = input("Введите год: ")
    if a.isdigit() is False:
        a = ''
        continue
    else:
        a = int(a)
        if a < 0:
            a = ''
            continue
        else:
            break

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print("Год високосный")
else:
    print("Год невисокосный")


# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
a = ''
b = ''
c = ''

while a.isdigit() is False:
    a = input("Введите первое число: ")
while b.isdigit() is False:
    b = input("Введите второе число: ")
while c.isdigit() is False:
    c = input("Введите третье число: ")

a = int(a)
b = int(b)
c = int(c)

print("Среднее:")
if a > b:
    if a < c:
        print(a)
    elif b > c:
        print(b)
    else:
        print(c)
else:
    if b < c:
        print(b)
    elif a > c:
        print(a)
    else:
        print(c)
