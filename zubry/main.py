from datetime import timedelta, date
import numpy as np
import matplotlib.pyplot as plt

def possible(zubr_count):

    hay_stock = 100_000
    acorn_stock = 5_000

    hay_spending = zubr_count * 40
    acorn_spending = 20 * zubr_count

    day = date(2012, 12, 1)


    while day < date(2013, 3, 1):

        if hay_stock >= 50_000:
            hay_stock -= hay_spending

        else:
            acorn_stock -= acorn_spending

        if day.weekday() == 4:
            hay_stock += 15_000

        if day.weekday() == 1:
            acorn_stock += 4_000

        if hay_stock < 0 or acorn_stock < 0:
            return False
        day += timedelta(days=1)
    return True

hay_stock = 100_000
acorn_stock = 5_000

hay_spending = 90 * 40
acorn_spending = 20 * 90

day = date(2012, 12, 1)

zad_a_hay = 0
zad_a_acorns = 0

zad_b_day = None

zad_c_hay = 0
zad_c_acorns = 0

recording_days = [
        date(2012, 12, 31),
        date(2013, 1, 31),
        date(2013, 2, 28),
]
record_labels = []
record_data_hay = []
record_data_acorns = []

while day < date(2013, 3, 1):

    if day in recording_days:
        record_labels.append(day.isoformat())
        record_data_hay.append(hay_stock)
        record_data_acorns.append(acorn_stock)


    if hay_stock >= 50_000:
        hay_stock -= hay_spending
        zad_c_hay += 1

    else:
        acorn_stock -= acorn_spending
        zad_c_acorns += 1
        if zad_b_day is None:
            zad_b_day = day

    if day.weekday() == 4:
        hay_stock += 15_000
        zad_a_hay += 1

    if day.weekday() == 1:
        acorn_stock += 4_000
        zad_a_acorns += 1

    day += timedelta(days=1)

print("ZADANIE A", zad_a_hay, zad_a_acorns)
print("ZADANIE B", zad_b_day.isoformat())
print("ZADANIE C", zad_c_hay, zad_c_acorns)

width = 0.35
indices = np.arange(len(record_labels))
ax = plt.subplot(111)
b1 = ax.bar(indices - width/2, record_data_hay, width, label='siano')
b2 = ax.bar(indices + width/2, record_data_acorns, width, label='żołędzie')
ax.set_xticks(indices)
ax.set_xticklabels(record_labels)
ax.set_xlabel('data')
ax.set_ylabel('stan magazynu')
ax.legend()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f"{height/1000:.1f}t",
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha="center", va="bottom")

autolabel(b1)
autolabel(b2)

i = 90
while True:
    if not possible(i):
        break
    i += 1
print("ZADANIE E", i)

plt.show()
