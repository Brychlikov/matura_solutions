
digit_codes = []
with open("cyfra_kodkreskowy.txt") as digit_code_file:
    _ = digit_code_file.readline()  # wiersz nagłówkowy
    for line in digit_code_file:
        line = line.strip()
        data = line.split("\t")
        digit_codes.append(data[1])


def control_subsum(num: str) -> (int, int):
    even = 0
    odd = 0
    for i, digit in enumerate(num[::-1]):
        if i % 2 == 0:
            even += int(digit)

        else:
            odd += int(digit)

    return even, odd


def control_digit(num: str) -> int:

    even, odd = control_subsum(num)
    control = 3 * even + odd
    control %= 10
    control = 10 - control
    control %= 10

    return control

def encode(num: str) -> str:
    start = "11011010"
    stop = "11010110"

    res = start
    for digit in num:
        res += digit_codes[int(digit)]

    control = control_digit(num)
    res += digit_codes[control]
    res += stop

    return res

assert encode("764321") == "110110101010101110111010111011101010101011101011101110111010101010111010101110111010101011101010101110111011010110"

print("110110101010101110111010111011101010101011101011101110111010101010111010101110111010101011101010101110111011010110")
print(encode("764321"))


assert control_subsum("764321") == (10, 13)
assert control_subsum("10101010101010") == (0, 7)

# print(list(enumerate(digit_codes)))

print("Zad 6.1")

with open("kody1.txt", "w") as outfile_zad1:
    for line in open("kody.txt"):
        line = line.strip()
        outfile_zad1.write(" ".join(map(str, control_subsum(line))) + "\n")


print("Zad 6.2")


with open("kody2.txt", "w") as outfile_zad2:
    for line in open("kody.txt"):
        line = line.strip()

        even, odd = control_subsum(line)
        control = control_digit(line)

        control_str = str(control)

        outfile_zad2.write(control_str + " " + digit_codes[control] + "\n")


with open("kody3.txt", "w") as outfile_zad3:
    for line in open("kody.txt"):
        line = line.strip()

        outfile_zad3.write(encode(line) + "\n")
