# расставить ферзей, чтобы они не били дргу друга
def check(i, j):
    if not h[j] and not d1[j - i + 7] and not d2[i + j]:
        return True
    return False


def gen(i):
    global f
    if i > 8:
        f = True
        print(*r)
    else:
        for j in range(1, 9):
            if check(i, j):
                r[i] = j
                h[j] = 1
                d1[j - i + 7] = 1
                d2[i + j] = 1
                gen(i + 1)
                if f:
                    break
                h[j] = 0
                d1[j - i + 7] = 0
                d2[i + j] = 0


f = False
d1 = [0] * 17
d2 = [0] * 17
h = [0] * 9
r = [0] * 9
gen(1)
