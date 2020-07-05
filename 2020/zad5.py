from datetime import date, timedelta
from math import ceil
from copy import deepcopy
from collections import defaultdict

class Zbiornik:

    def __init__(self):
        self.contains = 25_000
        self.total = 0

    def vaporize(self, temperature):
        self.contains = max(self.contains - ceil(0.0003 * temperature ** 1.5 * self.contains), 0)

    def rain(self, intensity):
        self.contains = min(ceil(700 * intensity) + self.contains, 25_000)

    def fill(self):
        self.total += 25_000 - self.contains
        self.contains = 25_000

    def have_to_fill(self, temperature, intensity):
        if 30 >= temperature > 15 and intensity < 0.61:
            return self.contains < 12_000
        if temperature > 30 and intensity < 0.61:
            return self.contains < 24_000

    def water(self, temperature):
        used = 0
        if temperature <= 30:
            if self.contains < 12_000:
                used = 25_000 - self.contains
                self.fill()
            self.contains -= 12_000
        else:
            if self.contains < 24_000:
                used = 25_000 - self.contains
                self.fill()
            self.contains -= 24_000
        return used


z = Zbiornik()
day = date(2015, 3, 31)

file = open("pogoda.txt")
_ = file.readline()  # pozbyc sie wiersza naglowkowego

data = []
for line in file:
    line = line.strip().replace(",", ".")
    data.append(tuple(map(float, line.split("\t"))))

print("Zadanie 5.1")
counter1 = 0
counter2 = 0
counter3 = 0

for temperature, intensity in data:
    if temperature <= 15:
        counter1 += 1
    if temperature > 15 and intensity <= 0.61:
        counter2 += 1
    if temperature > 15 and intensity > 0.61:
        counter3 += 1

print(counter1, counter2, counter3)
print()


# symulacja

zad52_first = None

plot_data = []
plot_labels = []

cost_dict = defaultdict(int)

for temperature, intensity in data:
    day += timedelta(days=1)
    if intensity != 0:
        z.rain(intensity)
    else:
        z.vaporize(temperature)

    bought = 0
    if z.have_to_fill(temperature, intensity):
        if zad52_first is None:
            zad52_first = day
    if temperature > 15 and intensity < 0.61:
        bought = z.water(temperature)
    plot_data.append(z.contains)
    plot_labels.append(deepcopy(day))

    cost_dict[(day.year, day.month)] += bought / 1000

assert z.total == 743_427

print("Zadanie 5.2:", zad52_first.isoformat())
print()


import matplotlib.pyplot as plt

plt.plot(plot_labels, plot_data)
plt.ylabel("Stan zbiornika w litrach")
plt.xlabel("Data")
plt.show()


print("Zadanie 5.4")

for (year, month), bought in sorted(cost_dict.items()):
    cost = ceil(bought) * 11.74 
    cost = round(cost, 2)
    print(month, year, cost, "zł")


