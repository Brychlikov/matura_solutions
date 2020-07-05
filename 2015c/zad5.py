from dataclasses import dataclass

from datetime import date

from typing import List, Optional
from collections import Counter, defaultdict, namedtuple

@dataclass
class CrimeType:
    id: int
    name: str
    fine: int
    points: int

    def __hash__(self):
        return hash(self.id)


crimetype_dict = {}
file = open("wykroczenia.txt")
_ = file.readline()  # zignorować wiersz nagłówkowy

for line in file:
    data = line.split('	')
    entry = CrimeType(
        int(data[0]),
        data[1],
        int(data[2]),
        int(data[3])
    )
    crimetype_dict[entry.id] = entry

@dataclass
class CrimeInstance:
    pesel: str
    date: date
    type: CrimeType



@dataclass
class Driver:
    pesel: str
    licence_date: date
    city: str
    wykroczenia: List[CrimeInstance]


driver_dict = {}
file = open("kierowcy.txt")
_ = file.readline()

for line in file:
    data = line.split('	')
    entry = Driver(
        pesel=data[0],
        licence_date=date.fromisoformat(data[1]),
        city=data[2],
        wykroczenia=[]
    )
    driver_dict[entry.pesel] = entry

instance_list = []

file = open("mandaty.txt")
_ = file.readline()

for line in file:
    data = line.split('	')
    entry = CrimeInstance(
        pesel=data[0],
        date=date.fromisoformat(data[1]),
        type=crimetype_dict[int(data[2])]
    )
    driver_dict[entry.pesel].wykroczenia.append(entry)
    instance_list.append(entry)



print("Zad 5.1")

counter = Counter()
for instance in instance_list:
    counter[instance.type] += 1

result = counter.most_common(1)
print(result[0][0].name, result[0][1])


print("Zad 5.2")

filtered_drivers = [driver for driver in driver_dict.values() if
                    driver.licence_date.year == 2013 and
                    sum([i.type.points for i in driver.wykroczenia]) > 20
                    ]

for driver in filtered_drivers:
    s = sum((i.type.points for i in driver.wykroczenia))
    print(f"{driver.pesel}\t{s}")



print("Zad 5.3")

for crime in crimetype_dict.values():
    if "naruszenie zakazu" in crime.name.lower():
        print(crime.name)

print("Zad 5.4")



@dataclass
class Month:
    num: int = 0
    count: int = 0
    total_fine: int = 0


by_month = [Month(num=i) for i in range(1, 13)]

for i in instance_list:
    by_month[i.date.month - 1].count += 1
    by_month[i.date.month - 1].total_fine += i.type.fine

for i in by_month:
    print(i)

print()
print(min(by_month, key=lambda x: x.count))


print("Zad 5.5")

print(sum((1 for d in driver_dict.values() if len(d.wykroczenia) == 0)))

city_counter = Counter()
for d in driver_dict.values():
    if len(d.wykroczenia) == 0:
        city_counter[d.city] += 1

print(city_counter.most_common(1))


