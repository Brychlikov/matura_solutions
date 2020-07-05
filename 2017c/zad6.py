from dataclasses import dataclass, field
from typing import List


Bundle = object


class ConstructorAdapter:

    adapters = []

    @classmethod
    def init_from_str(cls, *args):
        new_args = [f(a) for f, a in zip(cls.adapters, args)]
        return cls(*new_args)


def ident(x):
    return x


@dataclass
class Program(ConstructorAdapter):
    id: int
    name: str
    type: str
    price: int
    in_bundles: List[Bundle] = field(default_factory=list)

    adapters = [int, ident, ident, int, ident]


@dataclass
class Bundle(ConstructorAdapter):
    id: int
    name: str
    company: str
    programs: List[Program] = field(default_factory=list)

    adapters = [int, ident, ident, ident]

    def __hash__(self):
        return hash(id)

    def value(self):
        return sum(p.price for p in self.programs)

    def free_program_count(self):
        return sum(p.price == 0 for p in self.programs)

    def comercial_program_count(self):
        return sum(p.price != 0 for p in self.programs)


program_dict = {}
with open("programy.txt") as file:
    _ = file.readline()
    for line in file:
        line = line.strip()

        data = line.split('\t')
        new_program = Program.init_from_str(*data)

        new_program2 = Program(
            id=int(data[0]),
            name=data[1],
            type=data[2],
            price=int(data[3])
        )
        program_dict[new_program.id] = new_program


bundle_dict = {}
with open("pakiety.txt") as file:
    _ = file.readline()
    for line in file:
        data = line.strip().split('\t')
        new_bundle = Bundle.init_from_str(*data)
        bundle_dict[new_bundle.id] = new_bundle

with open("zestawy.txt") as file:

    _ = file.readline()
    for line in file:
        data = line.strip().split("\t")
        bundle_id = int(data[0])
        program_id = int(data[1])

        program = program_dict[program_id]
        bundle = bundle_dict[bundle_id]

        program.in_bundles.append(bundle)
        bundle.programs.append(program)


print("Zad 6.1")

in_two_or_more = [program for program in program_dict.values()
                  if program.type == "edytor dokumentow tekstowych"
                  and len(program.in_bundles) >= 2]

for p in in_two_or_more:
    print(p.name, len(p.in_bundles))


print("Zad 6.2")

unique = set((b for b in bundle_dict.values() if any(("zarzadzanie" in p.type for p in b.programs))))
for b in unique:
    print(b)


print("Zad 6.3")

sorted_bundles = sorted(bundle_dict.values(), key=lambda b: b.value())
for b in sorted_bundles[-3:]:
    print(b.name, b.company, b.value())


print("Zad 6.4")

sad_programs = [p for p in program_dict.values() if len(p.in_bundles) == 0]

for p in sad_programs:
    print(p)


print("Zad 6.5")

diverse_bundles = [b for b in bundle_dict.values() if b.comercial_program_count() != 0 and b.free_program_count() != 0]

for b in diverse_bundles:
    print(b.name, b.free_program_count(), b.comercial_program_count())


