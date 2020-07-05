from dataclasses import dataclass
from datetime import datetime


@dataclass 
class Computer:
    ident: int
    section: str
    capacity: int

    def __hash__(self):
        return self.ident


@dataclass
class Issue:
    ident: int
    computer: Computer
    timestamp: datetime
    priority: int

    def __hash__(self):
        return self.ident


@dataclass
class Fix:
    issue_id: int
    timestamp: datetime
    kind: str


computers = {}
with open("komputery.txt") as file:
    _ = file.readline()
    for line in file:
        data = line.strip().split("\t")
        i = int(data[0])
        computers[i] = Computer (
            i,
            data[1],
            int(data[2])
        )

issues = {}
with open("awarie.txt") as file: 
    _ = file.readline()
    for line in file:
        data = line.strip().split("\t")
        i = int(data[0])
        comp_id = int(data[1])
        raw_time = data[2].replace(' ', 'T')
        timestamp = datetime.fromisoformat(raw_time)
        priority = int(data[3])
        issues[i] = Issue(
                i,
                computers[comp_id],
                timestamp,
                priority
        )

fixes = []
with open("naprawy.txt") as file:
    _ = file.readline()
    for line in file:
        data = line.strip().split("\t")
        issue_id = int(data[0])
        raw_time = data[1].replace(' ', 'T')
        timestamp = datetime.fromisoformat(raw_time)
        kind = data[2]
        fixes.append(Fix(issue_id, timestamp, kind))
    
        

# Zad 6.1
from collections import defaultdict

count_dict = defaultdict(int)
for i, c in computers.items():
    count_dict[c.capacity] += 1

occurance_list = [(count, drive) for (drive, count) in count_dict.items()]
occurance_list.sort(reverse=True)

print("Zadanie 6.1")
for i in occurance_list[:10]:
    print(i)

print()

# Zad 6.2

print("Zadanie 6.2")
a_section = [c for c in computers.values() if c.section == "A"]
for c in a_section:
    computer_issues = [i for i in issues.values() if i.computer is c]
    computer_fixes = [f for f in fixes if f.issue_id in [i.ident for i in computer_issues] and f.kind == "wymiana"]
    if len(computer_fixes) >= 10:
        print(c, len(computer_fixes))
print()


# Zad 6.3

print("Zadanie 6.3")

count_dict = defaultdict(int)

for i, issue in issues.items():
    day = issue.timestamp.date()
    section = issue.computer.section
    count_dict[(section, day)] += 1

totals_dict = defaultdict(int)
for c in computers.values():
    totals_dict[c.section] += 1

for (section, day), val in count_dict.items():
    if val == totals_dict[section]:
        print(section, day, val)

print()

# Zad 6.4

print("Zad 6.4")
issue_fix_tuples = []
for f in fixes:
    issue_fix_tuples.append((issues[f.issue_id], f))

# maximum jest łączne więc
longest = max(((f.timestamp - i.timestamp, i, f) for i, f in issue_fix_tuples))
print(longest)
print()


# Zad 6.5

print("Zad 6.5")
sad_computer_set = set()

for i in issues.values():
    if i.priority >= 8:
        sad_computer_set.add(i.computer)

print(len(computers) - len(sad_computer_set))



