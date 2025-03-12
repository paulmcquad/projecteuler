from collections import defaultdict

N = 50000
block = 399


def gen():
    a = []
    for i in range(1, 56):
        a.append((100003 - 200003 * i + 300007 * i ** 3) % 1000000)
        yield a[-1]
    while True:
        a.append((a[-24] + a[-55]) % 1000000)
        yield a[-1]


def dfs(f, flag, pre, here):
    s = 0
    for i in range(f, len(here)):
        now = cubes[here[i]]
        x, y, z = max(pre[0], now[0]), max(pre[1], now[1]), max(pre[2], now[2])
        dx = min(pre[0] + pre[3], now[0] + now[3]) - x
        dy = min(pre[1] + pre[4], now[1] + now[4]) - y
        dz = min(pre[2] + pre[5], now[2] + now[5]) - z
        if min(dx, dy, dz) <= 0:
            continue
        s += flag * dx * dy * dz + dfs(i + 1, -flag, [x, y, z, dx, dy, dz], here)
    return s


cubes = []
mp = defaultdict(list)
g = gen()

for m in range(N):
    a, b, c = g.__next__() % 10000, g.__next__() % 10000, g.__next__() % 10000
    x, y, z = g.__next__() % 399 + 1, g.__next__() % 399 + 1, g.__next__() % 399 + 1
    cubes.append((a, b, c, x, y, z))
    for i in range(a // block, (a + x) // block + 1):
        for j in range(b // block, (b + y) // block + 1):
            for k in range(c // block, (c + z) // block + 1):
                mp[i, j, k].append(m)
ans = 0
for pos, here in mp.items():
    ans += dfs(0, 1, [pos[0] * block, pos[1] * block, pos[2] * block, block, block, block], here)
print(ans)

