#===============================================================================
# 
# f = open('rosalind_seto.txt')
# raw = f.readlines()
# lines = []
# for each in raw:
#     lines.append(each)
# n = int(lines[0].rstrip('\n'))
# allem = []
# for i in range(1, n+1):
#     s = str(i)
#     allem.append(s)
# f.close()
# allm = allem.copy()
# 
# 
# oneraw = lines[1].rstrip('\n')
# tworaw = lines[2].rstrip('\n')
# oneraw = oneraw.replace("{", "")
# oneraw = oneraw.replace("}", "")
# oneraw = oneraw.replace(",", "")
# onesplit = oneraw.split(" ")
# 
# tworaw = tworaw.replace("{", "")
# tworaw = tworaw.replace("}", "")
# tworaw = tworaw.replace(",", "")
# twosplit = tworaw.split(" ")
# 
# for each in onesplit:
#     each = int(each)
# for each in twosplit:
#     each = int(each)
# if len(twosplit) >= len(onesplit):
#     long = twosplit.copy()
#     short = onesplit.copy()
# else:
#     long = onesplit.copy()
#     short = twosplit.copy()
#      
# union = []
# overlap = []
# amb = []
# for each in onesplit:
#     amb.append(each)
# 
# bma = []
# for each in twosplit:
#     bma.append(each)
#     
# acom = allem
# bcom = allm
#     
# for each in long:
#     union.append(each)
# for each in short:
#     if each not in union:
#         union.append(each)
# 
# for each in long:
#     if each in short:
#         overlap.append(each)
# 
# for each in twosplit:
#     if each in onesplit:
#         amb.remove(each)
# 
# for each in onesplit:
#     if each in twosplit:
#         bma.remove(each)
# 
# for each in onesplit:
#     if each in allem:
#         allem.remove(each)
# for each in twosplit:
#     if each in allm:
#         allm.remove(each)
# a = ""
# s = ""
# for each in union:
#     s += each + ', '
# o = ("{" + s +"}")
# o = o.replace(", }", "}")
# 
# a += o +'\n'
# s = ""
# for each in overlap:
#     s += each + ', '
# o = ("{" + s +"}")
# o = o.replace(", }", "}")
# a += o +'\n'
# 
# s = ""
# for each in amb:
#     s += each + ', '
# o = ("{" + s +"}")
# o = o.replace(", }", "}")
# a += o +'\n'
# 
# s = ""
# for each in bma:
#     s += each + ', '
# o = ("{" + s +"}")
# o = o.replace(", }", "}")
# a += o +'\n'
# 
# s = ""
# for each in allem:
#     s += each + ', '
# o = ("{" + s +"}")
# o = o.replace(", }", "}")
# a += o +'\n'
# 
# 
# s = ""
# for each in allm:
#     s += each + ', '
# o = ("{" + s +"}")
# o = o.replace(", }", "}")
# a += o +'\n'
# 
# print(a, file=open("output.txt", "w"))
#==================================================
from Bio import SeqIO

f = SeqIO.parse('rosalind_cat.txt','fasta')
line =  []
for each in f:
    line.append(each.seq)
seq = line[0]
print(seq)
l = int(len(seq)/2)

def cn(n):
    if n==0 or n==1:
        return 1
    
    c = [0 for i in range(n+1)]
    
    c[0] = 1
    c[1] = 1
    
    for i in range(2, int(n)+1):
        c[i]=0
        for j in range(i):
            c[i] += c[j]*c[i-j-1]
    return c[n]
print(cn(l)%1000000)
print(cn(136))

def solve(rna):
    """
    An input RNA consisting of {A, U, C, G}
    The number of non-overlapping perfect 
    matchings.
    """
    return helper(rna, 0, len(rna) - 1, {})


def helper(rna, lo, hi, dp):
    
    mapping = {
    "A" : "U",
    "U" : "A",
    "G" : "C",
    "C" : "G"
    }
    characters = hi - lo + 1
    
    # if there are an odd number of nucleotides, 
    # this is an invalid matching.
    if characters % 2 == 1:
        return 0

    # handles tricky edge cases.
    if lo >= hi or lo >= len(rna) or hi < 0:
        return 1

    # return answer if it is memoized.    
    if (lo, hi) in dp:
        return dp[(lo, hi)]
    else:
        curr = rna[lo]
        target = mapping[curr]
        acc = 0
        for i in range(lo + 1, hi + 1, 2):
            if rna[i] == target:
                left = helper(rna, lo + 1, i - 1, dp)
                right = helper(rna, i + 1, hi, dp)
                acc += (left * right) % 1000000
        dp[(lo, hi)] = acc
        return acc


rna = "CAUAUG"

print(solve(str(seq)) % 1000000)
            
    
    
