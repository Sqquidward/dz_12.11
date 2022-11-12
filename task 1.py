list = input().split()

list_2 = set()
digit = 0
for ls in list:
    list_2.add(ls)
    if digit == len(list_2):
        print('Yes')
    else:
        print('No')
        digit+=1

