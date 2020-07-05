from dataclasses import dataclass

@dataclass
class Entry:
    day: int
    temperature: float
    rain: int
    category: str
    cloud_indensity: int


data = []
with open("pogoda.txt") as file:
    _ = file.readline()

    for line in file:
        line_data = line.strip().replace(",", ".").split(";")
        data.append(Entry(
            int(line_data[0]),
            float(line_data[1]),
            int(line_data[2]),
            line_data[3],
            int(line_data[4])
        ))

print("Zadanie 5.1")
print(sum([e.temperature >= 20 and e.rain <= 5 for e in data]))
print()


print("Zadanie 5.2")

good = [data[i].temperature > data[i - 1].temperature for i in range(1, len(data))]
longest = 0
best_start = None
best_stop = None
start = None
for i, x in enumerate(good):
    if not x and start is not None:
        if i - start > longest:
            best_start = start
            best_stop = i
            longest = i - start
        start = None
    elif start is None:
        start = i

longest += 1
print(best_start + 1, best_stop + 1)
print()

print("Zadanie 5.3")
import matplotlib.pyplot as plt

cloud_names = ["C1", "C2", "C3", "C4", "C5", "S1", "S2", "S3", "S4", "S5"]
index_dict = {n: i for i, n in enumerate(cloud_names)}

average_data = [0 for i in range(10)]
for entry in data[:300]:
    if entry.cloud_indensity == 0:
        continue
    name = entry.category + str(entry.cloud_indensity)
    average_data[index_dict[name]] += entry.rain / 300


plt.bar(cloud_names, average_data)
plt.ylabel("Średnie opady [mm]")
plt.xlabel("Rodzaj chmury")
plt.show()


print("Zadanie 5.4")

simulated_data = [data[0]]
prev_entry = data[0]
increase_cd = -1
for real_entry in data[1:]:
    if prev_entry.cloud_indensity == 5:
        if prev_entry.rain >= 20:
            category = "0"
            cloud_indensity = 0
            increase_cd = -1
        else:
            category = prev_entry.category
            cloud_indensity = 5

    elif prev_entry.cloud_indensity == 0:
        if real_entry.temperature >= 10:
            category = "C"
        else:
            category = "S"
        cloud_indensity = 1
        increase_cd = 3

    elif increase_cd == 0 and prev_entry.cloud_indensity != 5:
        category = prev_entry.category
        cloud_indensity = prev_entry.cloud_indensity + 1
        increase_cd = 3


    else:
        category = prev_entry.category
        cloud_indensity = prev_entry.cloud_indensity


    increase_cd -= 1
    current_entry = Entry(real_entry.day, real_entry.temperature, real_entry.rain, category, cloud_indensity)
    simulated_data.append(current_entry)
    prev_entry = current_entry


a_arr = [0 for i in range(6)]
b_count = 0
c_count = 0
for s, d in zip(simulated_data[:20], data[:20]):
    assert s == d

for s, d in zip(simulated_data[:300], data[:300]):
    b_count += s.cloud_indensity == d.cloud_indensity
    c_count += s.category == d.category

for s, d in zip(simulated_data, data):
    a_arr[s.cloud_indensity] += 1


print("a: ")
for i, x in enumerate(a_arr):
    print(f"{i}: {x}")
print()
print("b: ", b_count)
print("c: ", c_count)



