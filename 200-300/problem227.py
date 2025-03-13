import numpy as np

N = 100
con = [1, 8, -18, 8, 1]
M = N >> 1
b = [-36] * M + [0]
a = []
for i in range(M):
    t = [0 for _ in range(M + 1)]
    for j in range(5):
        x = i + j - 2
        t[min(x % N, -x % N)] += con[j]
    a.append(t)
a.append([0] * M + [1])
x = np.linalg.solve(a, b)
ans = x[0]
print("{:.6f}".format(ans))

