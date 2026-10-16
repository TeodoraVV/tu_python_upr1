import math


# 1. Цена след две отстъпки
# Отстъпка X% значи плащаш (100 - X)%, затова умножаваме по (1 - X/100).
# Втората отстъпка се прилага върху вече намалената цена.
def task1():
    price = float(input("Първоначална цена: "))
    d1 = float(input("Първа отстъпка (%): "))
    d2 = float(input("Втора отстъпка (%): "))

    price = price * (1 - d1 / 100)
    price = price * (1 - d2 / 100)
    print(f"{price:.2f}")


# 2. Пътуване с два вида транспорт
# Общо разстояние = сбор от двата участъка.
# Цена на участък = километри * цена за км.
def task2():
    bus_km = float(input("Км с автобус: "))
    taxi_km = float(input("Км с такси: "))
    bus_price = float(input("Цена за км с автобус: "))
    taxi_price = float(input("Цена за км с такси: "))

    total_km = bus_km + taxi_km
    total_cost = bus_km * bus_price + taxi_km * taxi_price
    print(f"{total_km:.2f}")
    print(f"{total_cost:.2f}")


# 3. Заплата с бонус и удръжка
# Бонусът увеличава сумата (1 +), удръжката я намалява (1 -).
# Удръжката се смята върху сумата с бонуса.
def task3():
    hours = float(input("Отработени часове: "))
    rate = float(input("Заплащане на час: "))
    bonus = float(input("Бонус (%): "))
    deduction = float(input("Удръжка (%): "))

    salary = hours * rate
    salary = salary * (1 + bonus / 100)
    salary = salary * (1 - deduction / 100)
    print(f"{salary:.2f}")


# 4. Сметка в ресторант
# Храна + напитки, после добавяме таксата отгоре и делим на броя хора.
def task4():
    food = float(input("Стойност на храната: "))
    drinks = float(input("Стойност на напитките: "))
    service = float(input("Такса обслужване (%): "))
    people = int(input("Брой хора: "))

    total = (food + drinks) * (1 + service / 100)
    per_person = total / people
    print(f"{total:.2f}")
    print(f"{per_person:.2f}")


# 5. Обем и повърхнина на правоъгълен паралелепипед
# Обем = a * b * c. Шестте стени са по двойки еднакви,
# затова повърхнината е 2 * (ab + ac + bc). Три знака след запетаята.
def task5():
    a = float(input("Дължина: "))
    b = float(input("Ширина: "))
    c = float(input("Височина: "))

    volume = a * b * c
    surface = 2 * (a * b + a * c + b * c)
    print(f"{volume:.3f}")
    print(f"{surface:.3f}")


# 6. Смесване на два сока
# Средна цена = цената на целия сок / общите литри
# (не просто средното на двете цени).
def task6():
    l1 = float(input("Литри първи сок: "))
    p1 = float(input("Цена за литър първи сок: "))
    l2 = float(input("Литри втори сок: "))
    p2 = float(input("Цена за литър втори сок: "))

    total_liters = l1 + l2
    avg_price = (l1 * p1 + l2 * p2) / total_liters
    print(f"{total_liters:.2f}")
    print(f"{avg_price:.2f}")


# 7. Време за пътуване
# Разстояние / скорост дава часове, * 60 ги прави минути, после + почивката.
def task7():
    distance = float(input("Разстояние (км): "))
    speed = float(input("Средна скорост (км/ч): "))
    rest = float(input("Почивка (минути): "))

    total_minutes = distance / speed * 60 + rest
    print(f"{total_minutes:.2f}")


# 8. Боядисване на стая
# Площ на 4-те стени = 2 * (дължина + ширина) * височина, минус прозорци/врати.
# Литри = площ / покривност, цена = литри * цена за литър.
def task8():
    length = float(input("Дължина: "))
    width = float(input("Ширина: "))
    height = float(input("Височина: "))
    openings = float(input("Площ на прозорци и врати: "))
    coverage = float(input("Покривност (кв.м. за литър): "))
    price = float(input("Цена за литър: "))

    area = 2 * (length + width) * height - openings
    liters = area / coverage
    cost = liters * price
    print(f"{liters:.2f}")
    print(f"{cost:.2f}")


# 9. Среднопретеглена оценка
# Всяка оценка * тежестта ѝ, сумираме и делим на 100 (тежестите са в %).
def task9():
    g1 = float(input("Оценка 1: "))
    w1 = float(input("Тежест 1 (%): "))
    g2 = float(input("Оценка 2: "))
    w2 = float(input("Тежест 2 (%): "))
    g3 = float(input("Оценка 3: "))
    w3 = float(input("Тежест 3 (%): "))

    result = (g1 * w1 + g2 * w2 + g3 * w3) / 100
    print(f"{result:.2f}")


# 10. Спестявания с проста лихва
# Всяка година носи една и съща лихва: сума * процент / 100.
def task10():
    principal = float(input("Начална сума: "))
    rate = float(input("Годишна лихва (%): "))
    years = float(input("Брой години: "))

    interest = principal * rate / 100 * years
    total = principal + interest
    print(f"{interest:.2f}")
    print(f"{total:.2f}")


# 11. Преобразуване на секунди
# // е целочислено деление (колко пъти се побира), % е остатъкът.
def task11():
    total = int(input("Общ брой секунди: "))

    hours = total // 3600
    minutes = total % 3600 // 60
    seconds = total % 60
    print(hours)
    print(minutes)
    print(seconds)


# 12. Поръчка на плочки
# Площ на пода / площ на плочка, + резерв (1 +), закръгляне нагоре с ceil.
def task12():
    length = float(input("Дължина на пода (м): "))
    width = float(input("Ширина на пода (м): "))
    tile_area = float(input("Площ на една плочка (кв.м.): "))
    reserve = float(input("Резерв (%): "))
    tile_price = float(input("Цена на една плочка: "))

    needed = length * width / tile_area * (1 + reserve / 100)
    tiles = math.ceil(needed)
    cost = tiles * tile_price
    print(tiles)
    print(f"{cost:.2f}")


# 13. Разход на електроенергия
# Ватове / 1000 = киловати; киловати * часове * дни = киловатчасове.
def task13():
    watts = float(input("Мощност (W): "))
    hours_per_day = float(input("Часове на ден: "))
    days = int(input("Брой дни: "))
    price_kwh = float(input("Цена за кВтч: "))

    kwh = watts / 1000 * hours_per_day * days
    cost = kwh * price_kwh
    print(f"{kwh:.2f}")
    print(f"{cost:.2f}")


# 14. Средна скорост за два участъка
# Време = разстояние / скорост за всеки участък.
# Средна скорост = общо разстояние / общо време (не средното на скоростите).
def task14():
    d1 = float(input("Разстояние 1 (км): "))
    v1 = float(input("Скорост 1 (км/ч): "))
    d2 = float(input("Разстояние 2 (км): "))
    v2 = float(input("Скорост 2 (км/ч): "))

    total_time = d1 / v1 + d2 / v2
    avg_speed = (d1 + d2) / total_time
    print(f"{total_time:.2f}")
    print(f"{avg_speed:.2f}")


# 15. Печалба от продажби
# Приход = брой * продажна цена; разход = брой * доставна цена + допълнителни.
# Печалба = приход - разход (отрицателна при загуба).
def task15():
    count = int(input("Брой продадени продукти: "))
    sell_price = float(input("Продажна цена: "))
    buy_price = float(input("Доставна цена: "))
    extra = float(input("Допълнителни разходи: "))

    income = count * sell_price
    expenses = count * buy_price + extra
    profit = income - expenses
    print(f"{income:.2f}")
    print(f"{expenses:.2f}")
    print(f"{profit:.2f}")


tasks = [task1, task2, task3, task4, task5, task6, task7, task8,
         task9, task10, task11, task12, task13, task14, task15]

choice = int(input("Изберете задача (1-15): "))
if 1 <= choice <= 15:
    tasks[choice - 1]()
else:
    print("Няма такава задача.")
