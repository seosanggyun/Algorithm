N = []
for tc in range(9):
    N += [int(input())]

max = N[0]

for i in N:
    if i > max:
        max = i

count = 0

for j in N:
    count += 1
    if j == max:
        break

print(max, count)
