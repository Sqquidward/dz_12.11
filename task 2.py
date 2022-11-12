n, m = input().split()
list_n = set()
list_m = set()
for i in range(int(n)):
    list_n.add(input())

for j in range(int(m)):
    list_m.add(input())

print(len(list_n & list_m))
print(' '.join(sorted(list(list_n & list_m))))
print(len(list_n - list_m))
print(' '.join(sorted(list(list_n - list_m))))
print(len(list_m - list_n))
print(' '.join(sorted(list(list_m - list_n))))
