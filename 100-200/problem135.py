from projecteuler import is_prime
 
nmax = 55992
s = 0
inc=3
for n in range(3, nmax , 4):
  if is_prime(n): s += inc
  if is_prime(n+2): s += (inc-1)
  if n>nmax//16: inc=2
  if n>nmax//4: inc=1

print "Answer to PE135 =", s
