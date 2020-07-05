from datetime import date, timedelta
from collections import defaultdict
data = []
for line in open("woda.txt"):
    raw_timestamp, raw_flow = line.strip().split("\t")
    data.append((date.fromisoformat(raw_timestamp), int(raw_flow)))


print("Zadanie 5.1")
flow_by_year = defaultdict(int)
for day, flow in data:
    flow_by_year[day.year] += flow

print(max((f, y) for y, f in flow_by_year.items()))
print()


print("Zadanie 5.2")

longest = timedelta()
best_start = None
best_end = None
start = None
end = None
threshold = 10_000

for date, flow in data:
    if start is None and flow > threshold:
        start = date

    if flow < threshold:
        if start is not None:
            end = date
            length = end - start
            if length > longest:
                best_start = start
                best_end = end
            start = None
print(best_start)
print(best_end - timedelta(days=1))
print(best_end - best_start)
print()


print("Zadanie 5.3")
import matplotlib.pyplot as plt

by_month_2008 = [0 for i in range(12)]
for date, flow in data:
    if date.year == 2008:
        by_month_2008[date.month - 1] += flow

month_names = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"]

plt.bar(month_names, by_month_2008)
plt.xlabel("Miesiąc")
plt.ylabel("Woda dopływająca [m3]")
plt.show()


print("Zadanie 5.4")
from math import ceil

total = 500_000
first_overflow = None
b_counter = 0 

for date, flow in data:
    delta = ceil(total * 0.02)
    if total > 1_000_000:
        total = 1_000_000
        if first_overflow is None:
            first_overflow = date

    if total > 800_000:
        b_counter += 1

    total -= delta
    total += flow

total = 500_000
max_capacity = 0
for date, flow in data:
    delta = ceil(total * 0.02)

    max_capacity = max(total, max_capacity)

    total -= delta
    total += flow

print("a: ", first_overflow.isoformat())
print("b: ", b_counter)
print("c: ", max_capacity)





