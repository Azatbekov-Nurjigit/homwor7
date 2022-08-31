a = [14, 2, 73, 6, 5, 11, 87, 8, 9, 10]
a = sorted(a)
print(a)
ferst = 0
val = int(input())
last = len(a) - 1
pos = 0
result = False
while True:
    if ferst <= last and result == False:
        middle = (ferst + last) // 2
        if val == a[middle]:
            ferst = middle
            last = ferst
            result = True
            pos = middle
        else:
            if val > a[middle]:
                ferst = middle + 1
            else:
                last = middle - 1
    else:
        if result == True:
            print('Элемент найден', pos)
            break
        else:
            print('Элемент не найден')
            break

a = [1845, 62, 34, 4, 58, 566, 147, 84, 98, 70]
print(a)
N = 10
for i in range(N - 1):
    for j in range(N - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)
