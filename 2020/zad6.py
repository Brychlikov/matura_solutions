from dataclasses import dataclass
from typing import List
import datetime
from collections import defaultdict

@dataclass
class Client:
    ident: str
    first_name: str
    last_name: str

    def __hash__(self):
        return hash(self.ident)


@dataclass
class Service:
    ident: str
    family: str
    name: str
    cost: int

    def __hash__(self):
        return hash(self.ident)

@dataclass
class Visit:
    ident: str
    date: datetime.date
    nr: int
    client: Client
    services: List[Service]

    def __hash__(self):
        return hash(self.ident)

client_dict = {}
file = open("klienci.txt")
_ = file.readline()
for line in file:
    data = line.strip().split("\t")
    c = Client(*data)
    client_dict[c.ident] = c

service_dict = {}
file = open("zabiegi.txt")
_ = file.readline()
for line in file:
    data = line.strip().split("\t")
    data[3] = int(data[3])
    s = Service(*data)
    service_dict[s.ident] = s


visit_services = defaultdict(list)
file = open("wizytyzabiegi.txt")
_ = file.readline()
for line in file:
    v, s = line.strip().split("\t")
    visit_services[v].append(service_dict[s])


visit_dict = {}
file = open("wizytydane.txt")
_ = file.readline()
for line in file:
    data = line.strip().split()
    v = Visit(
        data[0],
        datetime.date.fromisoformat(data[1]),
        int(data[2]),
        client_dict[data[3]],
        visit_services[data[0]]
    )
    visit_dict[v.ident] = v


print("Zadanie 6.1")
alicja_kowalska_id = [c.ident for c in client_dict.values() if c.first_name == "Alicja" and c.last_name == "Kowalska"][0]

res = sum(
        [sum((s.cost for s in v.services)) for v in visit_dict.values() if v.client.ident == alicja_kowalska_id]
)
print(res, "zł")
print()


print("Zadanie 6.2")
visit_counter = defaultdict(int)
for v in visit_dict.values():
    visit_counter[v.client] += 1
r = sorted([(count, client) for client, count in visit_counter.items()], reverse=True, key=lambda x: x[0])
print(r[0])
print()


print("Zadanie 6.3")

res = [v for v in visit_dict.values() if "Magia Hawajow" in [s.name for s in v.services]]
res.sort(key=lambda x: x.date, reverse=True)
for entry in res:
    print(entry.date.isoformat())

print("łącznie:", len(res))
print()

print("Zadanie 6.4")


discounted = [
        v for v in visit_dict.values() if\
                v.client.ident[0] == "X" and\
                datetime.date(2017, 12, 6) <= v.date <= datetime.date(2018, 1, 15) and\
                "MAKIJAZ" in [s.family for s in v.services]
        ]

total_cost = 0
women = set([v.client for v in discounted])
print("\n".join(map(str, women)))
print(len(women))
for entry in discounted:
    for s in entry.services:
        if s.family == "MAKIJAZ":
            total_cost += 0.8 * s.cost

print(total_cost)
print()


print("Zadanie 6.5")

used = set()
for v in visit_dict.values():
    for s in v.services:
        used.add(s)

for s in service_dict.values():
    if s not in used and s.family == "FRYZJER MESKI":
        print(s.name)

