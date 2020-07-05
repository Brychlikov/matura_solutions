from dataclasses import dataclass
from datetime import date
from math import floor
from collections import Counter, defaultdict


def find(iterable, predicate):
    for i in iterable:
        if predicate(i):
            return i
    return None

@dataclass
class Car:
    name: str
    production_year: int
    buying_price: int
    registration: str
    mileage: int
    last_maintenance_date: date

    def current_price(self, year):
        return self.buying_price - self.distance_amortisation() - self.time_amortisation(year)

    def distance_amortisation(self):
        distance = floor(self.mileage / 100_000)

        return 0.02 * distance * self.buying_price

    def time_amortisation(self, year):
        age = year - self.production_year
        return 0.05 * age * self.buying_price

    def get_name(self):
        return self.name.split()[0]



testcar = Car("Volvo FH", 2015, 70000, "", 350000, None)
print(testcar.current_price(2017))
assert testcar.current_price(2017) == 58800
assert testcar.get_name() == "Volvo"


cars = []
with open("transport.txt") as file:
    _ = file.readline()

    for line in file:
        line = line.strip()

        data = line.split('\t')
        new_car = Car(
            name=data[0],
            production_year=int(data[1]),
            buying_price=int(data[2]),
            registration=data[3],
            mileage=int(data[4]),
            last_maintenance_date=date.fromisoformat(data[5])
        )
        cars.append(new_car)


print("Zad 5.1")


volvo_fh = find(cars, lambda c: c.registration == "ERA 092 TR" and c.name == "Volvo FH")
print(volvo_fh)
print(volvo_fh.time_amortisation(2017), volvo_fh.distance_amortisation(), volvo_fh.current_price(2017))
print()

cheapest = min(cars, key=lambda c: c.current_price(2017))
print(cheapest, cheapest.current_price(2017))
print()

print("Zad 5.2")

a_counter = defaultdict(int)
distance_by_brand = defaultdict(int)

for car in cars:
    a_counter[car.get_name()] += 1
    distance_by_brand[car.get_name()] += car.mileage

for name, amount in a_counter.items():
    average = round(distance_by_brand[name] / a_counter[name])
    print(f"{name}\t{amount}\t{average}")

print("Zad 5.3")

counter = defaultdict(int)

for car in cars:
    if 2006 <= car.production_year <= 2015:
        counter[car.get_name()] += 1

for name, amount in a_counter.items():
    print(name, amount)


print("Zad 5.4")

sorted_cars = sorted(cars, key=lambda c: c.last_maintenance_date)
longest_unmaintained = sorted_cars[:4]

for c in longest_unmaintained:
    print(c.name, c.registration, (date(2017, 1, 1) - c.last_maintenance_date).days, "dni")



