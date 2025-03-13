from math import asin, sin

f = lambda x: sum(abs(x * (1 << n) - round(x * (1 << n))) / (1 << n) for n in range(60))
g = lambda x: 0.5 - (x / 2 - x * x) ** 0.5


def I(x):
    if x < 1e-13:
        return 0
    if x <= 0.5:
        return I(2 * x) / 4 + x * x / 2
    else:
        return 0.5 - I(1 - x)


l, r = 0, 0.5
for _ in range(100):
    mid = (l + r) * 0.5
    if f(mid) > g(mid):
        r = mid
    else:
        l = mid
xl, xr = l, 0.5
yl, yr = g(xl), g(xr)
cr = 1 / 4
d = ((xl - xr) ** 2 + (yl - yr) ** 2) ** 0.5
theta = 2 * asin(d / (2 * cr))
arc_area = cr * cr / 2 * (theta - sin(theta))
circle_integral = (yl + yr) * (xr - xl) / 2 - arc_area
ans = I(xr) - I(xl) - circle_integral
print("{:.8f}".format(ans))

