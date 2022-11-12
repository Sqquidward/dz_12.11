digit = int(input())

list = []
for i in range(digit):
    list.append(set(input().split()))

for i in range(1, digit):
    list[0].update(list[i])

print(len(list[0]))
