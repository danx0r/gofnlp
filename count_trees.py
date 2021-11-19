from math import factorial as f

#(2n)! / ((n + 1)! * n!) 

for n in range(10):
    x = f(2*n) / (f(n + 1) * f(n))
    x = int(x)
    print (n, x) 
