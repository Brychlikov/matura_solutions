import random

def next_mandate(so_far, votes):
    coeficients = [(k, votes[k] / (2 * so_far[k] + 1)) for k in range(len(votes))]
    coeficients.sort(key=lambda x: x[1], reverse=True)
    so_far[coeficients[0][0]] += 1

with open('dane_wybory.txt') as file:
    constituancies = {}
    for line in file:
        data = line.strip().split()
        constituancies[data[0]] = [int(i) for i in data[1:]]
