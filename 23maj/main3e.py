data = [0,12,4,56,6,6243,-634, -634, -67- -64]

for a, b in enumerate(data):
    if b < 0:
        data[a] = "Negativ"

print(data)

squares = [x*x for x in range(10)]

print(squares)



with open("forras.txt") as f:
    a = f.read().split()

data = []

for x in range(0, len(a), 6):
    data.append([int(a[x]), int(a[x+1]), int(a[x+2]), int(a[x+3]), a[x+4], a[x+5]])


from collections import Counter

to_count = [d[5] for d in data]

counter = Counter(to_count)



print(counter)