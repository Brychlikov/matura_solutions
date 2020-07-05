from datetime import date, timedelta
from copy import copy

KOSTKA = 0
ORZECH = 1
MIAL = 2

prices = [
    685,  # kostka
    620,  # orzech
    380   # mial
]

daily_usage = [
    200,
    260,
    200 * 1.6
]
data = []
with open("piastek.txt") as file:
    for line in file:
        line = line.strip()
        line_data = list(map(int, line.split()))
        data.append(line_data)



print("Zad 4.1")
monthly_deliveries = [[0, 0, 0] for i in range(13)]  # index 0 pozostaje pusty, 1-12 to miesiace

day = date(2014, 10, 14)  # dzien przed pierwsza dostawa
for kostka, orzech, mial in data:
    day += timedelta(days=1)
    monthly_deliveries[day.month][KOSTKA] += kostka
    monthly_deliveries[day.month][ORZECH] += orzech
    monthly_deliveries[day.month][MIAL] += mial

print("\n".join(map(str, enumerate(monthly_deliveries[:]))))


print("Zad4.2")

with open("zad42_dane.csv", "w") as outfile:
    for i in range(1, 13):
        outfile.write(f"{i};{';'.join(map(str, monthly_deliveries[i]))}\n")


print("Zad4.3")

day = date(2014, 10, 14)
total_cost = 0
for kostka, orzech, mial in data:
    total_cost += kostka * prices[KOSTKA]
    total_cost += orzech * prices[ORZECH]
    total_cost += mial * prices[MIAL]

print(total_cost)


print("Zad4.4 - 4.6")

day = date(2014, 10, 14)
stock = [80, 80, 80]

days_with_kostka = 0
days_with_orzech = 0
days_with_mial = 0

mial_used = 0

first_day_mial = None

no_coal_counter = 0

for kostka, orzech, mial in data:
    day += timedelta(days=1)

    stock[KOSTKA] += kostka
    stock[ORZECH] += orzech
    stock[MIAL] += mial

    if stock[KOSTKA] >= daily_usage[KOSTKA]:
        days_with_kostka += 1
        stock[KOSTKA] -= daily_usage[KOSTKA]

    elif stock[ORZECH] >= daily_usage[ORZECH]:
        days_with_orzech += 1
        stock[ORZECH] -= daily_usage[ORZECH]

    elif stock[MIAL] >= daily_usage[MIAL]:
        days_with_mial += 1

        if first_day_mial is None:
            first_day_mial = copy(day)

        mial_used += daily_usage[MIAL]
        stock[MIAL] -= daily_usage[MIAL]

    else:
        no_coal_counter += 1

print("Zad 4.4")
print(days_with_kostka, days_with_orzech, days_with_mial)
print()

print("Zad 4.5")
print(first_day_mial.isoformat())
print()

print("Zad 4.6")
print(no_coal_counter)


print("kontrola")
print(mial_used)
assert mial_used == 9280

