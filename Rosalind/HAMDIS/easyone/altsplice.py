import math

def nCr(n, k):
    
    numerator = int(math.factorial(n))
    denominator =int( math.factorial(n-k) * math.factorial(k) )
    
    return (int(numerator) // int(denominator)) 

print(nCr(6,3))
n = 1824 
k = 1151 
sum = 0

for i in range(n-k + 1):
    q = k + i 
    binom = nCr(n, int(q))
    print(binom)
    sum += binom
    
print(sum % 1000000)
