from dataclasses import dataclass
from typing import List

class NoImageException(Exception):
    pass

class EndOfFileException(Exception):
    pass

@dataclass 
class Image:
    data: List[List[int]]
    row_parity: List[int]
    col_parity: List[int]

def readimage(f):
    firstline = f.readline()

    if not firstline:
        raise EndOfFileException
    else:
        firstline = firstline.strip()

    size = len(firstline) - 1

    if size == -1:
        raise NoImageException

    data = []
    row_parity = []
    col_parity = []

    for i in range(size):
        row = list(map(int, firstline[:-1]))
        data.append(row)
        row_parity.append(int(firstline[-1]))
        firstline = f.readline().strip()
    col_parity = list(map(int, firstline))

    return Image(data, row_parity, col_parity)

def is_reverse(im):
    return sum(sum(row) for row in im.data) > 200

def is_recurrential(im):
    for x_offset, y_offset in ((10, 0), (0, 10), (10, 10)):
        for x in range(10):
            for y in range(10):
                if im.data[y][x] != im.data[y + y_offset][x + x_offset]:
                    return False
    return True

def correctness(im):
    wrong_row = 0
    wrong_col = 0

    for row, parity in zip(im.data, im.row_parity):
        wrong_row += not (sum(row) % 2 == parity)

    for x, parity in zip(range(20), im.col_parity):
        s = 0
        for y in range(20):
            s += im.data[y][x]
        wrong_col += not(s % 2 == parity)
    return wrong_row == 0 and wrong_col == 0

with open("dane_obrazki.txt") as file:
    images = []
    while True:
        try:
            images.append(readimage(file))
        except NoImageException:
            pass
        except EndOfFileException:
            break


    print("zadanie 1", sum(map(is_reverse, images)))
    print("zadaine 2", sum(map(is_recurrential, images)))
    print("zadanie 3", sum(map(correctness, images)))


