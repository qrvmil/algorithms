# Из N чисел вывести все упорядоченные сочетания длины k

def gen(i):
    if i > k:
        print(*r[1:])
    else:
        for j in range(r[i - 1] + 1, n - (k - i) + 1):
            r[i] = j
            gen(i + 1)


n = int(input())
k = int(input())
r = [0] * (k + 1)
r[0] = 0
gen(1)
