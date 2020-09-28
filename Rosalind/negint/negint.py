from itertools import permutations
from itertools import product

def fac(n):
    if n == 1:
        return 1
    else:
        return n*fac(n-1)

f = open('rosalind_sign.txt')
raw = int(f.read().rstrip('\n'))
lperm = []

for i in range(1, raw + 1):
    lperm.append(int(i))
lperm = permutations(lperm)
fin = []
num = 0
for each in lperm:
    fin.append([[num * mul for num, mul in zip(each, combo)]
           for combo in product([1, -1], repeat=len(each))])
    
print((2**raw)*fac(raw))
for each in fin:
    for per in each:
        for num in per:
            print(num, end = " ")
        print()
    