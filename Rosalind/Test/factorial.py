#===============================================================================
# def factorial(n):
#     if n == 0 or n ==1:
#         return 1
#     else:
#         return n*(factorial(n-1))
# 
# def nCk(p, k):
#     binom = factorial(p)/(factorial(p-k)*factorial(k))
#     return binom
# 
# print(nCk(21, 7))
#===============================================================================

def solve(n, k):
    tot = 1
    while k > 0:
        tot = tot * n
        n = n - 1
        k = k - 1
    return tot

print(solve(90, 9)%1000000)
        
f = open('rosalind_lgis.txt', 'r')
raw = f.readlines()
print(raw)
        
    