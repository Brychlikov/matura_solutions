from math import factorial
from math import log

def digit_factorial(x):
    return sum(map(lambda d: factorial(int(d)), str(x)))


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def gcd_arr(a):
    if len(a) == 1:
        return a[0]
    head, *tail = a
    return gcd(head, gcd_arr(tail))


assert gcd(100, 35) == 5
assert gcd(10, 20) == 10
assert gcd(11, 1235) == 1


# fname = "przyklad.txt"
fname = "liczby.txt"
data = list(map(int, open(fname)))

print("Zadanie 4.1")
print(sum(map(lambda x: 3 ** round(log(x, 3)) == x, data)))
print()


print("Zadanie 4.2")
print([x for x in data if x == digit_factorial(x)])
print()

print("Zadanie 4.3")

best_range = (None, None)
best_length = 0
best_gcd = -1

for start in range(len(data)):
    for stop in range(start + 1, len(data) + 1):
        if (g := gcd_arr(data[start:stop])) > 1:
            if stop - start > best_length:
                best_length = stop - start
                best_range = (start, stop)
                best_gcd = g
        else:
            break

print(data[best_range[0]], best_length, best_gcd)
