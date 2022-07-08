--https://wiki.haskell.org/Euler_problems/171_to_180

--k=47547 
--2*k+1=95095 = 5*7*11*13*19
lst=[5,7,11,13,19]
primes=[2,3,5,7,11]
problem_176 =
    product[a^b|(a,b)<-zip primes (reverse n)]
    where
    la=div (last lst+1) 2
    m=map (\x->div x 2)$init lst
    n=m++[la]
