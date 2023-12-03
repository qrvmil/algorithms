f = open('26-120.txt')
m, n = map(int, f.readline().split())
total = [int(x) for x in f.readline().split()]
busy = [0] * m
count = [0] * m
time = [0] * m
a = [[int(y) for y in x.split()] for x in f]
a.sort()
b = []
for i in a:
    j = len(b) - 1
    while j > -1 and b[j][0] <= i[0]:
        busy[b[j][1]] -= 1
        del b[j]
        j -= 1
    if len(b) == 0:
        right = 0
    else:
        left = -1
        right = len(b)
        while left != right - 1:
            center = (left + right) // 2
            if b[center][0] <= i[0] + i[1]:
                right = center
            else:
                left = center
    category = -1
    for j in range(i[2], m):
        if total[j] > busy[j]:
            category = j
            break
    if category != - 1:
        b.insert(right, [i[0] + i[1], category])
        busy[category] += 1
        count[category] += 1
        time[category] = max(time[category], i[0] + i[1])
mx = 0
for i in range(1, m):
    if count[i] > count[mx]:
        mx = i
print(time[mx], count[mx])