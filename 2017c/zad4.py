from math import sqrt, ceil



def is_prime(n):
    bound = ceil(sqrt(n) + 1)

    for i in range(2, bound):
        if n % i == 0:
            return False

    return True


assert is_prime(5)
assert is_prime(17)
assert is_prime(13)
assert not is_prime(25)
assert not is_prime(19*17)


def is_cyfropodobna(x, y):
    x_set = set(str(x))
    y_set = set(str(y))

    return x_set == y_set


point_list = []
for line in open("punkty.txt"):
    x, y = map(int, line.strip().split())
    point_list.append((x, y))

print("Zad4.1")
zad1_counter = 0
zad2_counter = 0
for x, y in point_list:
    zad1_counter += is_prime(x) and is_prime(y)
    zad2_counter += is_cyfropodobna(x, y)

print(zad1_counter)


print("Zad 4.2")
print(zad2_counter)


print("zad 4.3")


def dist_sq(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


max_pair = None, None
max_sq_dist = 0

for i in range(len(point_list) - 1):
    for j in range(i+1, len(point_list)):
        d = dist_sq(point_list[i], point_list[j])
        if d > max_sq_dist:
            max_sq_dist = d
            max_pair = point_list[i], point_list[j]

print(max_pair)
print(sqrt(max_sq_dist))


print("zad 4.4")


a_counter = 0
b_counter = 0
c_counter = 0

for p in point_list:
    x_diff = abs(p[0])
    y_diff = abs(p[1])

    if x_diff < 5000 and y_diff < 5000:
        a_counter += 1
    elif x_diff == 5000 or y_diff == 5000:
        b_counter += 1
    else:
        c_counter += 1

print(a_counter, b_counter, c_counter)
