#http://wiki.san-ss.com.ar/project-euler-problem-142
from itertools import count, takewhile
 
is_square = lambda x: int(x ** 0.5) ** 2 == x
 
if __name__ == '__main__':
    for a in count(6):
        a_2 = a ** 2
        for f in (f for f in takewhile(lambda f: f < a, count(4)) if is_square(a_2 - f ** 2)):
            f_2 = f ** 2
            c_2 = a_2 - f_2
            setoff = 3 if (f & 1) else 2
            for e in (e for e in takewhile(lambda e: e ** 2 < c_2, count(setoff, 2)) if is_square(c_2 - e ** 2) and is_square(a_2 - e ** 2)):
                e_2 = e ** 2
                b_2 = c_2 - e_2
                d_2 = a_2 - e_2
                z = -(d_2 - c_2) // 2
                y = -(-d_2 - c_2 + 2 * b_2) // 2
                x = (d_2 + c_2) // 2
                print('The result is: (x){0} + (y){1} + (z){2} = {3}'.format(x, y, z, x + y + z))
                exit(0)
