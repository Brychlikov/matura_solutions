from collections import Counter


data = list(map(int, open("dane4.txt")))

luki41 = [abs(x - y) for x, y in zip(data[:-1], data[1:])]

print("Zadanie 4.1")
print(min(luki41), max(luki41))
print()


print("Zadanie 4.2")

def zad42(l):
    luki = [abs(x - y) for x, y in zip(l[:-1], l[1:])]
    current_luka = -1
    start_index = None

    best_count = 0
    best_start = None

    for i, el in enumerate(luki):
        if el != current_luka:
            if start_index != None:
                count = i - start_index
                if count > best_count:
                    best_count = count
                    best_start = start_index
                    best_end = i
            start_index = i
            current_luka = el

    # dodajemy 1 ponieważ 3 luki odpowiadają 4 elementom
    return best_count + 1, l[best_start], l[best_end]


test_data = [4, 11, 4, 1, 4, 7, 11, 12, 13, 14, 7, 0, 3]

assert zad42(test_data) == (4, 4, 7)
print("Długość: {} początek: {} koniec: {}".format(*zad42(data)))
print()


print("Zadanie 4.3")

def zad43(l):
    luki = [abs(x - y) for x, y in zip(l[:-1], l[1:])]
    c = Counter(luki)
    counts = c.most_common()
    result = []
    best = counts[0][1]
    for el in counts:
        if el[1] != best:
            break
        result.append(el)
    return result

assert set(zad43(test_data)) == set([(7, 4), (3, 4)])

res = zad43(data)
print("Krotność najczęstszej luki:", res[0][1])
print("Krotność tę mają luki:", [t[0] for t in res])




