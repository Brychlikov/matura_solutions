fname = "sygnaly.txt"
lines = [l.strip() for l in open(fname)]

print("Zadanie 4.1")
result = ""
for l in lines[39::40]:
    try:
        result += l[9]
    except Exception as e:
        print(e)
        print(l)

print(result)
print()


print("Zadanie 4.2")
max_length = 0
max_word = "error"
for word in lines:
    if (length := len(set(word))) > max_length:
        max_word = word
        max_length = length
print(max_word, max_length)
print()


print("Zadanie 4.3")

def dist(c1, c2):
    return abs(ord(c1) - ord(c2))


for word in lines:
    good = True
    for c1 in word:
        for c2 in word:
            if dist(c1, c2) > 10:
                good = False
    if good:
        print(word)
