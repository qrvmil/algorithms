# разложить чило на слагаемые без повторений


def gen(i, new):
    global r
    if new == 0:
        print(*r[1:])
    else:
        for j in range(min(r[i - 1], new), 0, -1):
            r[i] = j
            gen(i + 1, new - j)


n = int(input())
r = [0] * (n + 1)
r[0] = n
gen(1, n)
