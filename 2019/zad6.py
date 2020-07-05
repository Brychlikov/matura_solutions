from dataclasses import dataclass
from collections import defaultdict
from typing import List


@dataclass
class Perfume:
    ident: str
    name: str
    brand: str
    family: str
    price: int
    ingredients: List[str]

brand_dict = {}
with open("marki.txt") as file:
    _ = file.readline()
    for line in file:
        data = line.strip().split("\t")
        # indeksowane stringami!
        brand_dict[data[0]] = data[1]


ingredient_dict = defaultdict(list)
with open("sklad.txt") as file:
    _ = file.readline()
    for line in file:
        data = line.strip().split("\t")
        # indeksowane stringami!
        ingredient_dict[data[0]].append(data[1])

perfumes = []
with open("perfumy.txt") as file:
    _ = file.readline()

    for line in file:
        data = line.strip().split("\t")
        raw_id, name, raw_brand_id, family, raw_price = data
        perfumes.append(Perfume(
            raw_id,
            name,
            brand_dict[raw_brand_id],
            family,
            int(raw_price),
            ingredient_dict[raw_id]
        ))


print("Zadanie 6.1")
print([p.name for p in perfumes if "absolut jasminu" in p.ingredients])
print()

print("Zadanie 6.2")
cheapest_in_family = defaultdict(lambda: (float('inf'), None))
for p in perfumes:
    cheapest_in_family[p.family] = min(cheapest_in_family[p.family], (p.price, p.name))

for name, (price, p_name) in cheapest_in_family.items():
    print(f"Rodzina: {name}\n\tnajtańsze perfumy: {p_name} o cenie {price}")
print()

print("Zadanie 6.3")
# Niczego nie żałuję
print(sorted(list(set([p.brand for p in perfumes if p.brand not in set([p.brand for p in perfumes if any(("paczula" in i for i in p.ingredients))])]))))

print()


print("Zadanie 6.4")
from copy import deepcopy

discounted = [deepcopy(p) for p in perfumes if p.brand == "Mou De Rosine" and p.family == "orientalno-drzewna"]
for p in discounted:
    p.price *= 0.85

discounted.sort(key=lambda p: p.price)
for p in discounted:
    print(p.name, p.price)
print()


print("Zadanie 6.5")

brand_families = defaultdict(set)
for p in perfumes:
    brand_families[p.brand].add(p.family)

for b, f in brand_families.items():
    if len(f) == 1:
        print(b, list(f)[0])

