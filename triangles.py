
def triangles():
    L=[1]

    while True:
        yield L
        L = [1] + [L[n] + L[n+1] for n in range(len(L) - 1)] + [1]

        # print(len(L))

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break